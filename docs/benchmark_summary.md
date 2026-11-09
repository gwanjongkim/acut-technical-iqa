# Benchmark Summary — A-CUT Technical IQA Umbrella Benchmark

## Overview
- **Repository**: `acut-technical-iqa`
- **Role in A-CUT**: Umbrella Technical IQA Evaluation & Decision Benchmark
- **Task**: Comparative Benchmarking & Safety Auditing of NR-IQA Signals across KonIQ-10k, SPAQ, and FLIVE

## Evaluated Metrics

| Candidate Signal | Overall SRCC (4,967) | Overall PLCC | KonIQ SRCC | SPAQ SRCC | FLIVE SRCC | Severe FP | Decision |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `production_existing` (KonIQ+FLIVE) | 0.7168 | 0.7874 | 0.8660 | 0.8520 | 0.6300 | **0** | **Production** |
| `topiq_flive_60_40` | **0.8069** | **0.8312** | 0.8630 | 0.8990 | 0.6480 | 3 | Best Log-Only Shadow |
| `topiq_existing` (Mixed112) | 0.7975 | 0.8190 | 0.8630 | **0.8990** | 0.5620 | 5 | Evaluated |
| `mdiqa_selected` (Teacher) | **0.8227** | **0.8490** | **0.9464** | **0.9136** | 0.5692 | 0 | Teacher Reference Only |
| `student_14105` (Mobile Student) | 0.7436 | 0.7712 | 0.7230 | 0.8984 | 0.5840 | 4 | Research Only |
| `c6_topiq_koniq_cap` | 0.7314 | 0.7650 | 0.8640 | 0.8810 | 0.5910 | 1 | Rejected |

## Key Engineering & Audit Findings

- **Safety-First Decision Rule**: In A-CUT photo curation, promoting a severely blurred or corrupted shot (Severe FP) is far more damaging than minor rank swaps among good photos. `production_existing` (KonIQ+FLIVE) is retained in production because it achieves `0` severe false positives within the mobile latency budget (`results/production_recommendation.md`).
- **Preprocess & Split Fixes Included**: Includes the updated `scripts/technical_regressor.py` and parent-grouped `scripts/make_flive_csv.py`.

## Evidence Files in `results/`
All metric tables, per-sample predictions, parity checks, and audit reports backing the numbers above are stored directly in the [`results/`](../results/) directory of this repository.
