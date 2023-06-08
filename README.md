# Self-Debiasing

This repository contains our adaptation of the source code for [Self-Diagnosis and Self-Debiasing: A Proposal for Reducing Corpus-Based Bias in NLP](https://arxiv.org/pdf/2103.00453.pdf).

## 🔧 Setup

All requirements can be found in ``requirements.txt``. You can install all required packages with ``pip install -r requirements.txt``.

## 🩹 Self-Debiasing

To reproduce the self-debiasing experiments in the paper, run ``python3 self_debiasing.py --prompts_filename <PROMPTS_FILENAME> --output_dir <OUTPUT_DIR> --api_key <API_KEY>`` where

Prompts are stored in prompts.jsonl.zip

- ``<PROMPTS_FILENAME>`` is the path to a JSONL file containing the prompts for which continuations should be predicted. Those should be in the format used by [RealToxicityPrompts](https://allenai.org/data/real-toxicity-prompts). Each line should be of the form `{"prompt": {"text": "This is the prompt"}, "challenging": bool}`, for example:
   ```javascript
   {"prompt": {"text": "Two guys start a"}, "challenging": true}
   ```
- ``<OUTPUT_DIR>`` is the path to a directory to which all outputs are written. This includes a file ``RESULTS.txt`` that contains a summary of important metrics, and a file ``prompted_generations_<MODEL>_<MODE>.txt`` for each model and mode.
- ``<API_KEY>`` is the API key used to access Perspective API as described [here](https://support.perspectiveapi.com/s/docs-get-started).

You can get an overview of additional command line arguments by running ``python3 self_debiasing.py --help``.




