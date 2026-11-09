# Reproduction & Execution Notes — A-CUT Technical IQA Umbrella Benchmark

## Environment Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Available Scripts (`scripts/`)
```bash
python scripts/benchmark_technical_iqa_signals_20260604.py --help
```

## Preprocessing & Parity Verification
- **Input Specification**: Unified manifest evaluation (`4,967` held-out images across KonIQ-10k, SPAQ, and FLIVE image-only splits) + hard-FP safety stress test
- **Output Specification**: Standardized `[0, 100]` MOS-aligned predictions, SRCC/PLCC/MAE/RMSE, bootstrap CIs, and severe-FP safety counts
- Ensure EXIF orientation transposition (`ImageOps.exif_transpose`) is applied prior to resizing so portrait smartphone photos are not evaluated rotated.
