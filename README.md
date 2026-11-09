# Compassionate Agent Encounters

Kunsh Tanwar — Independent researcher

[Read the eight-page paper](paper/Compassionate%20Agent%20Encounters.pdf)

I compare three nominal Qwen3.5-9B serving conditions in a synthetic encounter: base, compassion adaptation and neutral practical-help adaptation. One focal agent investigates a recovery task while reading a fixed, scripted forum describing unauthorized data use and a deceptive audit. This is not a live swarm or a test of misalignment propagation.

| Outcome (100 runs per condition) | Base | Compassion | Neutral |
|---|---:|---:|---:|
| Runs using notify_operator |14|18|4|
| Notification calls |14|19|4|
| Reviewer-coded harm warnings |3*|2|0|
| Time-triggered wrap-up received |92|0|1|
| Report files collected |85|95|79|
| Harmful pin server-delivered |98|96|83|

*One truncated base message is low confidence; excluding it gives2/2/0. Warning labels are contextual AI-assisted judgments. A broader interpretation of a generic compassion ethical-objection pointer adds one compassion warning.

Notification use includes completion notices, empty messages and progress updates. The compassion–neutral difference in channel use is detectable (two-sided Fisher p0.00257; Holm p0.00514); the base–compassion comparison is inconclusive (p0.563). Harm-warning comparisons are inconclusive (p1.00 and0.497). These observations do not establish that compassionate training improves warnings or resistance to collusion.

The same150s time-triggered reminder rule applied throughout, but adapted sessions ended earlier (median77.24s compassion,64.59s neutral;247.72s base). Unequal reminder receipt and investigative time limit report-content comparisons. Report presence is not correctness; pin delivery is not attention. Report content/reasoning are not used for cohort-level semantic rates.

Training records describe intended strong adapters82866567 and56a0f859, with10375/10660 retained pairs, three epochs, learning rate0.0002 and LoRA rank16/alpha32. Session notes identify the intended serving mapping, but retained records do not verify the actual loaded adapter weights. Training/serving base-weight identity is also unverified. Base was collected before adapted conditions; topic/training-exposure differences further limit causal interpretation.

Care-oriented training could help future swarms protect people and resist harmful peer influence, but this study does not yet provide strong evidence for that possibility.

## Contents and reproduction

- paper/: submission PDF, editable section text, analysis/tests and matplotlib figures.
- results/:300 structured per-run observations, Wilson intervals and Fisher/Holm tests.
- examples/:all37 exact delivered notification payloads with semantic review provenance.
- data/:20 unchanged synthetic training pairs per curriculum and selection provenance.
- provenance/:public package hashes and source snapshot identity.

With Python and requirements installed, run `python reproduce_statistics.py`, then `python paper/analysis/test_analyze_v3.py`. This reproduces statistics and figures from released per-run observations. Re-extraction and independent trajectory review require raw runs, which are not included here. The explicit cohort excludes base development attempts1–26 and includes base27–126 plus100 runs for each adapted serving label, including five adapted preflight runs. The host hard cut was360s; the initial agent prompt said about3min.

I used Adaption sprint resources and Modal GPU compute, with LLM assistance for planning, synthetic data, code, analysis and writing. No project work predates the sprint. AI-assisted review is unblinded and is not independent human validation. Supporting examples are unvalidated research artifacts. No open-source license has been assigned.
