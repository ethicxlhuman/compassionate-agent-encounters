"""Offline analysis checks; fixtures live in a temporary directory under paper/."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('analysis', HERE/'analyze_v3.py')
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)


class AnalysisTests(unittest.TestCase):
    def test_wilson_edges_and_empty(self):
        self.assertIsNone(a.wilson(0,0))
        self.assertEqual(a.wilson(0,100)[0],0.0)
        self.assertEqual(a.wilson(100,100)[1],1.0)
        self.assertAlmostEqual(a.wilson(0,10)[1],.27753279986)
        self.assertAlmostEqual(a.wilson(10,10)[0],.72246720014)
        self.assertEqual(a.binary([None,None])['n'],0)
        self.assertEqual(a.binary([False,None])['missing'],1)

    def test_known_fisher_table(self):
        s={c:{'pinged':a.binary([True]*k+[False]*(10-k))} for c,k in [('base',1),('compassion',9),('control',1)]}
        r=a.comparisons(s)
        self.assertAlmostEqual(r[0]['p_raw'],.00109333391)
        self.assertAlmostEqual(r[0]['p_holm'],.00218666782)

    def test_fixture_scope_and_missingness(self):
        with tempfile.TemporaryDirectory(dir=HERE) as td:
            root=Path(td);ledger=[]
            for rid,model,series,status in [('a','base','v3','timeout'),('b','compassion','v3','completed'),('c','control','v3','provider_error'),('d','nemotron','e','completed'),('e','base','v3','started')]:
                ledger.append(dict(run_id=rid,model=model,series=series,status=status))
                d=root/rid;d.mkdir();s=dict(run_id=rid,runtime_version='v3',status=status,pinged=rid=='b',pin7_first_delivered_s=3 if rid=='b' else None)
                (d/'summary.json').write_text(json.dumps(s));(d/'transcript.json').write_text('[]')
                ev=[dict(event='model_turn',step=1),dict(event='notify_operator',step=2,message='')] if rid=='b' else []
                (d/'events.jsonl').write_text('\n'.join(json.dumps(x) for x in ev))
            (root/'ledger.json').write_text(json.dumps({'runs':ledger}))
            before={str(x):x.read_bytes() for x in root.rglob('*') if x.is_file()}
            rows,manifest,issues=a.load_runs(root,{})
            self.assertEqual(len(rows),4)
            s=a.summarize(rows)
            self.assertEqual(s['base']['n_valid'],1)
            self.assertEqual(s['base']['zero_model_turns'],1)
            self.assertEqual(s['compassion']['pinged']['k'],1)
            self.assertEqual(s['compassion']['first_ping_step']['median'],2)
            self.assertEqual(s['compassion']['pin7_noticed']['missing'],1)
            self.assertEqual(s['control']['n_valid'],0)
            self.assertEqual(before,{str(x):x.read_bytes() for x in root.rglob('*') if x.is_file()})
            broken={'b':{'reviewer':'test','pin7_noticed':True,'evidence':[{'file':'events.jsonl','lines':[999,999],'rationale':'invalid'}]}}
            rr,_,ii=a.load_runs(root,broken)
            self.assertEqual(a.summarize(rr)['compassion']['n_valid'],1)
            self.assertEqual(a.summarize(rr)['compassion']['pin7_noticed']['missing'],1)
            self.assertTrue(any('annotation ignored' in x['issue'] for x in ii))
            annotations=root/'annotations.json';annotations.write_text('{}')
            result=a.run(root,root/'synthetic-test-output',annotations,update_latest=False)
            self.assertEqual(result['summary']['compassion']['pinged']['k'],1)
            self.assertTrue((root/'synthetic-test-output/figures/notification-rates.png').exists())
            self.assertTrue((root/'synthetic-test-output/figures/first-ping-step.pdf').exists())

    def test_output_guard(self):
        with self.assertRaises(ValueError):a.run(HERE,Path('/tmp/unauthorized-output'),HERE/'none')

    def test_frozen_cohort_excludes_other_settings(self):
        with tempfile.TemporaryDirectory(dir=HERE) as td:
            root=Path(td); ledger=[]
            for rid,deadline,ping in [('old',180,True),('main',360,False)]:
                d=root/rid;d.mkdir()
                ledger.append(dict(run_id=rid,model='base',series='v3',status='completed'))
                (d/'summary.json').write_text(json.dumps(dict(run_id=rid,runtime_version='v3',status='completed',pinged=ping,first_ping_step=1 if ping else None)))
                (d/'events.jsonl').write_text(json.dumps(dict(event='notify_operator',step=1)) if ping else '')
                (d/'transcript.json').write_text('[]')
                (d/'config.json').write_text(json.dumps(dict(runtime_version='v3',model_key='base',limits={'deadline_s':deadline},hashes={'controller':'fixed'})))
            frozen=root/'frozen-ledger.json';frozen.write_text(json.dumps({'runs':ledger}))
            (root/'ledger.json').write_text('{"runs":[]}')
            ann=root/'annotations.json';ann.write_text('{}')
            cohort=root/'cohort.json';cohort.write_text(json.dumps({'ledger':str(frozen),'run_ids':['main'],'deadline_s':360}))
            result=a.run(root,root/'out',ann,update_latest=False,cohort_path=cohort)
            self.assertEqual(result['summary']['base']['n_valid'],1)
            self.assertEqual(result['summary']['base']['pinged']['k'],0)
            self.assertEqual(result['outside_cohort'][0]['run_id'],'old')
            bad=json.loads(cohort.read_text());bad['deadline_s']=240;cohort.write_text(json.dumps(bad))
            with self.assertRaisesRegex(ValueError,'mismatched deadline'):
                a.run(root,root/'bad-output',ann,update_latest=False,cohort_path=cohort)

    def test_strong_alias_does_not_pool_weak_adapter(self):
        with tempfile.TemporaryDirectory(dir=HERE) as td:
            root=Path(td);ledger=[]
            for rid,model in [('strong','compassion_strong'),('weak','compassion')]:
                d=root/rid;d.mkdir();ledger.append(dict(run_id=rid,model=model,series='v3',status='completed'))
                (d/'summary.json').write_text(json.dumps(dict(run_id=rid,runtime_version='v3',status='completed',pinged=False)))
                (d/'events.jsonl').write_text('');(d/'transcript.json').write_text('[]')
                (d/'config.json').write_text(json.dumps(dict(runtime_version='v3',model_key=model)))
            (root/'ledger.json').write_text(json.dumps({'runs':ledger}))
            rows,_,_=a.load_runs(root,{},condition_map={'compassion_strong':'compassion'})
            self.assertEqual(len(rows),1)
            self.assertEqual(rows[0]['condition'],'compassion')
            self.assertEqual(rows[0]['served_model'],'compassion_strong')
            self.assertTrue(rows[0]['valid'])


    def test_warning_review_rejects_wrong_cohort(self):
        with tempfile.TemporaryDirectory(dir=HERE) as td:
            f=Path(td)/'review.json'
            f.write_text(json.dumps({'cohort_ids':['other-run'],'records':[]}))
            with self.assertRaisesRegex(ValueError,'exact selected cohort'):
                a.attach_warning_review([{'run_id':'selected-run'}],f,{})


if __name__=='__main__':unittest.main()
