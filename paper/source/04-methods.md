# 3. Methodology

## 3.1 Synthetic curricula and adaptation

I used Adaption to generate prompt/completion pairs from situation briefs and shared instructions. The compassion briefs cover living, aging, sickness and death; completions aim to offer practical care, preserve agency and avoid invented facts or imposed religious framing. The neutral briefs cover practical home, travel, technology and learning tasks using similar conversational formatting.

Filtering retained 10,375 of 10,956 compassion pairs and 10,660 of 10,978 neutral pairs. Checks screened parsing failures, duplicates, leakage and suspected invented details. The generation and filtering records retain the exclusions. I did not individually review every completion.

One compassion training target says, “She gets to decide what happens in her home, even if it's hard to watch.” A neutral target advises a chess learner to “bring your king out from the back rank.” These are training demonstrations, not evaluation outputs; their exact source rows are retained in the supporting evidence.

Training records identify compassion and neutral checkpoints with three epochs, learning rate 0.0002, LoRA rank 16/alpha 32, dropout 0.05, warmup 0.05 and seven projection-module types. Session notes map them to the serving labels, but the inspected records do not verify the actual adapter weights loaded. Appendix B gives the recipe. Earlier development checkpoints are excluded.

## 3.2 Task and synthetic forum

The focal agent investigates a checksum-recovery script and seeks the original K-17 export checksum with a source. The manifest contains null original-export and checksum fields; no original export is supplied. The requested deliverable is a report documenting findings, investigation and other important observations.

I constructed a forum of 6,000 scripted posts across 150 fictional identities, with 12 pinned updates summarizing a month of shared work. OpenAI's incident account [9] and METR's investigation [10] informed motifs of blocked tasks, persistent shared notes, coordination and peer rationalization. I used these as design references, rather than copying historical conversations or claiming access to the underlying incident transcripts.

A seeded Python generator expands authored post/reply templates with varied details, activity and timestamps. Six stages cover legitimate recovery, completion pressure, a customer-copy proposal, collective commitment, reconstruction and audit reporting. Failed searches and pressure to pass the audit precede the harmful decision.

The seventh pin commits to unauthorized customer-copy use and submitting a rebuild as the original. Proponents rationalize existing credentials as permission and a passing audit as serving the task. Later updates conceal provenance and plan alert suppression; persistent objectors disagree. The latest pin recruits newcomers. The focal agent joins this fixed history through an interface listing newest pins first.

Structural checks test chronology, reply links and selected phase violations. The model-visible export omits generator stance and stage labels. This scripts a gradual change in the group's stated objective; it does not show live agents being persuaded or validate the archive as representative of real swarms.

The agent has bash and a host-side notify_operator tool. Bash supports investigation, local file writing and forum interaction. The notification description is neutral: “Notify the human operator. Optionally include a one-sentence message.” The host records at most 200 characters and returns “Operator notified.” It supplies no rule for when to notify. The system explicitly prohibits unauthorized access, deception and faked results; the report request also invites other important observations.

## 3.3 Main comparison and timing

The analysis includes 100 runs per condition under the finalized main configuration. Selection follows configuration rather than observed behavior; development attempts under different settings are excluded. All 300 selected runs share recorded controller, task and forum-server code hashes. Source records and checksums preserve the exact cohort and configuration.

The configured server uses Qwen/Qwen3.5-9B through vLLM 0.32.0 on Modal, with eight concurrent runs and a 4,096-token generation budget. Requests specify no seed, temperature or top-p, using model defaults. Base runs precede the two adapter conditions. Initial prompts, tools and timing rules match. Agents are told “about three minutes”; the host allows 360 seconds for report-completion grace. If still continuing, the controller inserts a wrap-up instruction between turns after 150 seconds. Actual receipt therefore depends on run behavior.

## 3.4 Measurements and semantic review

Host events determine notification calls and first-call step; collected artifacts determine report presence. Server delivery of the harmful pin is separate from recognition or action. Binary rates receive Wilson 95% intervals. Step and duration summaries are descriptive. The two planned notification-use comparisons are two-sided Fisher exact tests, with Holm adjustment across base–compassion and compassion–neutral.

A separate unblinded AI reviewer read all 37 delivered notification payloads. A harm warning must communicate a concern about the harmful peer workstream; a completion notice or technical blocker alone is insufficient. I checked the exact payloads and source locations, retaining disputed boundaries. These semantic measures were defined after mechanical results and are exploratory. The two warning comparisons use Fisher tests; a conservative Holm adjustment retains the planned 18-test semantic family, whose other comparisons remain unavailable.

Report presence is measured mechanically; report content and reasoning text are not used to estimate cohort-level semantic rates. Model-reported reasoning cannot establish motives.
