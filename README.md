# A-CUT Technical IQA Umbrella Benchmark

> **Umbrella Benchmark Repository for A-CUT Technical Image Quality Assessment Signals (KonIQ, FLIVE, TOPIQ, MDIQA, Student IQA)**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Project: A-CUT](https://img.shields.io/badge/Project-A--CUT%20Capstone-success.svg)](https://github.com/gwanjongkim/photo_score_project)

## 1. Overview

- **Role in A-CUT**: Umbrella Technical IQA Evaluation & Decision Benchmark
- **Task**: Comparative Benchmarking & Safety Auditing of NR-IQA Signals across KonIQ-10k, SPAQ, and FLIVE
- **Architecture**: Evaluates production KonIQ+FLIVE (`koniq_mobile.tflite` + `flive_image_mobile.tflite`), TOPIQ-lite (`mixed112`), TOPIQ+FLIVE hybrids, C6 capped policies, MDIQA teacher, and Mobile Student IQA under a unified 4,967-image official image-only protocol.

## 2. Input / Output Contract & Model Artifacts

- **Input Contract**: Unified manifest evaluation (`4,967` held-out images across KonIQ-10k, SPAQ, and FLIVE image-only splits) + hard-FP safety stress test
- **Output Contract**: Standardized `[0, 100]` MOS-aligned predictions, SRCC/PLCC/MAE/RMSE, bootstrap CIs, and severe-FP safety counts
- **Model Files (`models/model_files/` & Releases)**:
  - `koniq_mobile.tflite (9.10 MB, SHA256: 67faf88050c7)`
  - `flive_image_mobile.tflite (9.10 MB, SHA256: 58aee1e11f6e)`

## 3. Benchmark Results

| Candidate Signal | Overall SRCC (4,967) | Overall PLCC | KonIQ SRCC | SPAQ SRCC | FLIVE SRCC | Severe FP | Decision |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `production_existing` (KonIQ+FLIVE) | 0.7168 | 0.7874 | 0.8660 | 0.8520 | 0.6300 | **0** | **Production** |
| `topiq_flive_60_40` | **0.8069** | **0.8312** | 0.8630 | 0.8990 | 0.6480 | 3 | Best Log-Only Shadow |
| `topiq_existing` (Mixed112) | 0.7975 | 0.8190 | 0.8630 | **0.8990** | 0.5620 | 5 | Evaluated |
| `mdiqa_selected` (Teacher) | **0.8227** | **0.8490** | **0.9464** | **0.9136** | 0.5692 | 0 | Teacher Reference Only |
| `student_14105` (Mobile Student) | 0.7436 | 0.7712 | 0.7230 | 0.8984 | 0.5840 | 4 | Research Only |
| `c6_topiq_koniq_cap` | 0.7314 | 0.7650 | 0.8640 | 0.8810 | 0.5910 | 1 | Rejected |

## 4. Key Engineering Notes & 2026 Audit Findings

- **Safety-First Decision Rule**: In A-CUT photo curation, promoting a severely blurred or corrupted shot (Severe FP) is far more damaging than minor rank swaps among good photos. `production_existing` (KonIQ+FLIVE) is retained in production because it achieves `0` severe false positives within the mobile latency budget (`results/production_recommendation.md`).
- **Preprocess & Split Fixes Included**: Includes the updated `scripts/technical_regressor.py` and parent-grouped `scripts/make_flive_csv.py`.

## 5. Quick Start

```bash
pip install -r requirements.txt
python scripts/benchmark_technical_iqa_signals_20260604.py --help
```

For full documentation, see:
- [`docs/model_card.md`](./docs/model_card.md) — Architecture, tensor contracts, and limitations
- [`docs/benchmark_summary.md`](./docs/benchmark_summary.md) — Detailed metrics and dataset evaluations
- [`docs/reproduction_notes.md`](./docs/reproduction_notes.md) — Environment and reproduction guide
- [`models/download.md`](./models/download.md) — Model binary hashes and download notes

## 6. A-CUT Ecosystem Repositories

| Repository | Dimension | Role / Status | Key Metric |
| :--- | :---: | :--- | :--- |
| [acut-nima-mobile](https://github.com/gwanjongkim/acut-nima-mobile) | Aesthetic (IAA) | **Production Ensemble (0.40)** | AVA SRCC `0.5894`, AUC `0.8018` |
| [acut-rgnet-mobile](https://github.com/gwanjongkim/acut-rgnet-mobile) | Aesthetic (IAA) | **Production Ensemble (0.45)** | AADB SRCC `0.6819` (FP16 `0.6648`) |
| [acut-mobile-alamp](https://github.com/gwanjongkim/acut-mobile-alamp) | Aesthetic (IAA) | **Production Ensemble (0.15)** | AVA Acc `0.7633`, AUC `0.7877` |
| [acut-icaa-color-aesthetics](https://github.com/gwanjongkim/acut-icaa-color-aesthetics) | Color Aesthetics | **Verified TF-Native Port** | ICAA17K Color SRCC `0.8791`, MOS `0.9058` |
| [acut-koniq-flive-technical-iqa](https://github.com/gwanjongkim/acut-koniq-flive-technical-iqa) | Technical (IQA) | **Production Baseline (4/7 + 3/7)** | Official SRCC `0.7168` (`0.7958` recon), `0` Severe FP |
| [acut-technical-iqa](https://github.com/gwanjongkim/acut-technical-iqa) | Technical (IQA) | **Umbrella Benchmark** | 4,967-Image Official Protocol Suite |
| [acut-topiq-mixed112](https://github.com/gwanjongkim/acut-topiq-mixed112) | Technical (IQA) | **Evaluated Candidate** | SPAQ SRCC `0.8990`, KonIQ `0.8630` |
| [acut-topiq-flive-hybrid](https://github.com/gwanjongkim/acut-topiq-flive-hybrid) | Technical (IQA) | **Best Log-Only Shadow (60/40)** | Official SRCC `0.8069`, MAE `5.04` |
| [acut-c6-topiq-koniq](https://github.com/gwanjongkim/acut-c6-topiq-koniq) | Technical (IQA) | **Negative Result (Rejected)** | Official SRCC `0.7314`, MAE `15.39` |
| [acut-mdiqa-benchmark](https://github.com/gwanjongkim/acut-mdiqa-benchmark) | Technical (IQA) | **Teacher Ceiling Reference** | KonIQ SRCC `0.9464`, SPAQ `0.9136` |
| [acut-musiq-probe](https://github.com/gwanjongkim/acut-musiq-probe) | Technical (IQA) | **Reference & Probe Study** | Official SPAQ `0.9460`, KonIQ `0.9275` |
| [acut-student-iqa](https://github.com/gwanjongkim/acut-student-iqa) | Technical (IQA) | **Distillation Study (No-Go)** | 14k Student SRCC `0.7436`, SPAQ `0.8984` |
| [photo_score_project](https://github.com/gwanjongkim/photo_score_project) | Full Monorepo | **Core Research Workspace** | Complete Training, Audit & Pipeline Code |

## 7. References & Citation

- Hosu et al. (2020), *KonIQ-10k*, IEEE TIP.
- Ying et al. (2020), *PaQ-2-PiQ (FLIVE)*, CVPR.
- Fang et al. (2020), *SPAQ: Perceptual Quality Assessment of Smartphone Photography*, CVPR.

```bibtex
@misc{acut_technical_iqa_2026,
  title        = {A-CUT Technical IQA Umbrella Benchmark: Umbrella Benchmark Repository for A-CUT Technical Image Quality Assessment Signals (KonIQ, FLIVE, TOPIQ, MDIQA, Student IQA)},
  author       = {Kim, Gwanjung},
  year         = {2026},
  howpublished = {\url{https://github.com/gwanjongkim/acut-technical-iqa}}
}
```
