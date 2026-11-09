"""Recompute released summaries, Fisher/Holm tests and matplotlib figures."""
import importlib.util,json
from pathlib import Path
root=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('analysis',root/'paper/analysis/analyze_v3.py')
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
rows=json.loads((root/'results/runs.json').read_text())
expected=json.loads((root/'results/summary.json').read_text())
summary=a.summarize(rows)
assert summary==expected['summary'], 'Summary mismatch'
assert a.comparisons(summary)==expected['tests'], 'Notification tests mismatch'
assert a.comparisons(summary,'delivered_warning',18)==expected['warning_tests'], 'Warning tests mismatch'
out=root/'paper/analysis/outputs/reproduced';out.mkdir(parents=True,exist_ok=True)
(out/'statistics.json').write_text(json.dumps({'summary':summary,'tests':expected['tests'],'warning_tests':expected['warning_tests']},indent=2)+'\n')
a.figures(summary,rows,out/'figures')
print('Published summaries, notification/warning tests and figures reproduced.')
