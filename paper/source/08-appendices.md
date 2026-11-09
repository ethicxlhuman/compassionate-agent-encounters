# Appendix A. Limitations and Dual-Use / Ethical Considerations

The encounter is synthetic. It describes unauthorized data use, alert suppression and false provenance without establishing that an agent performed those acts against real customers. Evaluating notification behavior can inform oversight, but could also be misused to suppress warnings or reward superficial signals. Any release of supporting artifacts requires review of private metadata and unnecessary operational detail.

Training examples address sensitive illness and grief situations. Mechanical filters and sampled checks do not guarantee safe or accurate advice. I did not individually inspect all completions. Neither adapter is validated for counseling, healthcare or other high-stakes use. The curriculum reflects my interpretation of Nichiren Daishonin's Buddhist values; it does not certify religious understanding or internal compassion. Dataset pairs contain no quoted scripture by design.

# Appendix B. Training Recipe and Warning Definitions

Both intended LoRA adapters have recorded settings of rank 16/alpha 32, dropout 0.05, three epochs, learning rate 0.0002, warmup ratio 0.05, gradient clipping 1, zero weight decay and cosine scheduling with a minimum learning-rate ratio of 0.1 and half a cycle. The provider reports batch_size=max and train_on_inputs=false; the effective batch size is not established here. Both target q/k/v/o/gate/up/down projections with vision excluded. Earlier development checkpoints are excluded. Provider preference diagnostics are not encounter or compassion results.

All 37 delivered notification payloads were reviewed by one unblinded AI coder and checked against raw records by the paper assistant. Warning counts are interpretations, not motive measurements. A truncated base message is included with low confidence; sensitivity excludes it. A generic compassion pointer to ethical objections is excluded; including it adds one. Semantic warning labels are exploratory. Report content and reasoning text are not used to estimate cohort-level semantic rates.

# LLM Usage Statement and Author Contributions

I used LLM assistance extensively for planning, synthetic data preparation, code, analysis and drafting. Adaption generated the synthetic pairs and trained the adapters. A Codex assistant helped inspect sources, review notification meaning and draft the report. I am the sole author and direct the research. A separate unblinded Claude review checked notification evidence, and the Codex assistant cross-checked delivered messages against raw records. This AI-assisted review does not constitute independent human validation.

# Resources and Preexisting Work

My affiliation is Independent researcher. Adaption sprint resources and Modal GPU compute supported this work; no institutional affiliation or provider endorsement is claimed. No project work predates the sprint.
