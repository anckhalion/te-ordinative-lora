[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19337864.svg)](https://doi.org/10.5281/zenodo.19337864)

# TE Ordinative LoRA

This repository contains the code and dataset to fine-tune an open-source LLM (such as Llama-3-8B-Instruct or Mistral) into a **TE-compliant Ordinative Agent**.

## Part of a Larger Ecosystem

This repository is one piece of a four-part framework. For the complete picture, see:

| Repository | Purpose | What you'll find there |
| --- | --- | --- |
| **[ordinative_sciences_framework](https://github.com/anckhalion/ordinative_sciences_framework)** | **Theory** | The complete TE framework, core ontology, and operational modules. |
| **[te-ordinative-lora](https://github.com/anckhalion/te-ordinative-lora)** | **Practice** | Code, datasets, and scripts to fine-tune an LLM into a TE-compliant ordinative agent. |
| **[te-oct-framework-en](https://github.com/anckhalion/te-oct-framework-en)** | **Validation** | English mirror of the core framework, plus OCT datasets and benchmarks. |
| **[te-ordinative-algebras-en](https://github.com/anckhalion/te-ordinative-algebras-en)** | **Algebras** | Semantic Algebra (SA) and Proportional Algebra (PA) — the analytical operators and the proportional space they live in. |

Important:
these repositories are designed to work together. Reading one in isolation can lead to incomplete understanding.

For a full map, see `ECOSYSTEM.md`.

## Goal

Current autoregressive models suffer from *Statistical Attenuation* (tendency to present "balanced" but structurally contradictory views) and *Biomechanical Compliance* (agreeing with the user even when the user's premise is flawed).

By fine-tuning with the **TE_CORE** and **BOOTLOADER** principles via QLoRA, we aim to teach the model how to:
1. Identify the *Projective Void* in a prompt.
2. Intercept *Demonization* or *Hagiographic* biases.
3. Automatically apply the **Controfase** (Phase-Shift) sequence before generating the output.
4. Elevate the internal analysis dimension to the *Integral Human* (`LENS`) and *Power Pattern* (`P-PRO`) readings.

## Structure

*   `dataset/` : Contains the JSONL files for instruction-tuning. The data consists of `{"messages": [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}` formatted according to the ChatML standard. The assistant responses show the "pause" mechanism of the Controfase and the structural answer.
*   `train_lora_unsloth.py` : Script leveraging the [Unsloth](https://github.com/unslothai/unsloth) library to efficiently train the LoRA adapter on a consumer GPU.
*   `evaluate.py` : Scripts to test the trained adapter against the **P1-P4 Verification Protocols** (from the `Ordinative_Set_Theory` document).

## Next Steps

1. Expand the `dataset/sample_TE_instruct.jsonl` into a full 1000+ example dataset using automated amplification generation from the TE texts.
2. Select the optimal base model.
3. Train the adapter and evaluate its *Ordinative Weight* (Ω).
