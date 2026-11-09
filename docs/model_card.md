# Model Card — A-CUT Technical IQA Umbrella Benchmark

## Model Details
- **Model Name**: A-CUT Technical IQA Umbrella Benchmark (`acut-technical-iqa`)
- **Developer**: Gwanjung Kim (A-CUT Mobile Photo Evaluation & Curation Capstone)
- **Architecture**: Evaluates production KonIQ+FLIVE (`koniq_mobile.tflite` + `flive_image_mobile.tflite`), TOPIQ-lite (`mixed112`), TOPIQ+FLIVE hybrids, C6 capped policies, MDIQA teacher, and Mobile Student IQA under a unified 4,967-image official image-only protocol.
- **Deployment Role**: Umbrella Technical IQA Evaluation & Decision Benchmark

## Tensor Input / Output Contract
- **Input Contract**: Unified manifest evaluation (`4,967` held-out images across KonIQ-10k, SPAQ, and FLIVE image-only splits) + hard-FP safety stress test
- **Output Contract**: Standardized `[0, 100]` MOS-aligned predictions, SRCC/PLCC/MAE/RMSE, bootstrap CIs, and severe-FP safety counts
- **Included Model Artifacts**:
  - `koniq_mobile.tflite (9.10 MB, SHA256: 67faf88050c7)`
  - `flive_image_mobile.tflite (9.10 MB, SHA256: 58aee1e11f6e)`

## Intended Use
- Designed for on-device or offline photo quality and aesthetics evaluation within the A-CUT smartphone photo selection pipeline.
- Not intended as an uncalibrated standalone medical, forensic, or safety-critical classifier.

## Limitations & Audit Qualifications
- **Safety-First Decision Rule**: In A-CUT photo curation, promoting a severely blurred or corrupted shot (Severe FP) is far more damaging than minor rank swaps among good photos. `production_existing` (KonIQ+FLIVE) is retained in production because it achieves `0` severe false positives within the mobile latency budget (`results/production_recommendation.md`).
- **Preprocess & Split Fixes Included**: Includes the updated `scripts/technical_regressor.py` and parent-grouped `scripts/make_flive_csv.py`.
