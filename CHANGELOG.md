# Changelog

All notable changes to this repository should be documented in this file.

The format is inspired by Keep a Changelog and semantic versioning principles for documentation releases.

> **Note**: This changelog was added on 2026-05-06. Entries before that date are reconstructed retrospectively from git history; full diff context lives in `git log`. Future entries are written at the time of the change.

## [0.3.0] - 2026-05-06

### Updated
- `ECOSYSTEM.md` extended from 3-pillar to 4-pillar architecture to include the new `te-ordinative-algebras-en` repository (SA + PA frameworks).
- `README.md` "Part of a Larger Ecosystem" table updated from three-part to four-part, with row added for `te-ordinative-algebras-en`.

### Added
- `CHANGELOG.md` (this file).

### Notes
- The new repository [`te-ordinative-algebras-en`](https://github.com/anckhalion/te-ordinative-algebras-en) was published on 2026-05-06 with initial release `v1.0.0`. It provides the analytical operator-level grammar (SA + PA) that the LoRA training pipeline aims to teach the fine-tuned model to recognise and apply.

## [0.2.1] - 2026-04-20

### Added
- Ecosystem cross-links between this repository and the other public repositories of the Ordinative Sciences programme.
- Shared `ECOSYSTEM.md` map.

## [0.2.0] - 2026-03-30

### Added
- DOI badge linked to Zenodo deposit for the LoRA dataset and training pipeline.

## [0.1.2] - 2026-03-29

### Added
- Google Colab Jupyter Notebook for Unsloth training (`Creato con Colab`).
- Colab-ready training notebook for low-resource environments.

## [0.1.1] - 2026-03-29

### Added
- English translation of `TE_instruct.jsonl` dataset, with ordinative terminology preserved.

## [0.1.0] - 2026-03-28

### Added
- Initial commit: dataset and training script for fine-tuning an open-source LLM into a TE-compliant Ordinative Agent.
- `dataset/` with JSONL instruction-tuning examples (ChatML format).
- `train_lora_unsloth.py` — Unsloth-based QLoRA training script.
