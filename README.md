# A-CUT Technical IQA

#### A-CUT Capstone Project — Mobile Image Quality and Aesthetic Assessment

> Umbrella repository for evaluating multiple Technical IQA models against the production baseline.

## Introduction

Umbrella repository for evaluating multiple Technical IQA models against the production baseline. It serves as the primary benchmark evidence for A-CUT technical scoring decisions.

- **Role**: Umbrella benchmark for technical quality assessment.
- **Task**: Image Quality and Aesthetic Assessment.

## Model / Method

Evaluates various technical quality models including KonIQ, FLIVE, TOPIQ, and MDIQA using the official 4,967-image protocol. The production technical_score remains the default choice until log-only profiling is completed for candidates.

- **Artifacts**: Inferred from scripts

## Dataset and Benchmark

- Benchmark results are summarized below. See `docs/benchmark_summary.md` for detailed per-dataset analysis.
- Note: Large datasets are excluded due to size/license constraints.

## Model Weights / Artifacts

- Due to size constraints, artifacts larger than 50MB are not included in this repository.
- Recommended hosting: GitHub Releases.
- See `models/download.md`.

## Repository Structure

```
.
├── configs/
├── docs/
├── models/
├── results/
├── scripts/
└── requirements.txt
```

## Requirements

Please refer to `requirements.txt`. Minimal dependencies include `torch`, `tensorflow`, `numpy`, and `pillow`.

## Quick Start

```bash
pip install -r requirements.txt
python scripts/benchmark_technical_iqa_signals_20260604.py
```
*(Verify path assumptions in `docs/reproduction_notes.md`)*

## Results

| Dataset | Metric | Value | Evidence Path | Decision |
|---------|--------|-------|---------------|----------|
| Official Protocol | production_existing SRCC | 0.7168 | outputs/official_protocol_technical_signal_benchmark_20260604/report.md | Production |
| Official Protocol | topiq_existing SRCC | 0.7975 | outputs/official_protocol_technical_signal_benchmark_20260604/report.md | Log-Only |
| Official Protocol | student_14105 SRCC | 0.7436 | outputs/official_protocol_technical_signal_benchmark_20260604/report.md | Evaluated |
| Official Protocol | topiq_flive_60_40 SRCC | 0.8069 | outputs/official_protocol_technical_signal_benchmark_20260604/report.md | Log-Only Candidate |
| Official Protocol | c6_topiq_koniq_cap SRCC | 0.7314 | outputs/official_protocol_technical_signal_benchmark_20260604/report.md | Rejected |

## Limitations

- Results are based on local reproduction and may not exactly match original papers.
- See `docs/model_card.md` for detailed limitations.

## Citation

```bibtex
@misc{acut_technical_iqa_2026,
  title        = {A-CUT Technical IQA: Mobile Image Quality and Aesthetic Assessment Model},
  author       = {Kim, Gwanjung},
  year         = {2026},
  note         = {Capstone project repository}
}
```
### Original References

- KonIQ-10k Paper
- FLIVE Paper
- SPAQ Paper

## Related Repositories

- [A-CUT Public Model Repositories](..)
