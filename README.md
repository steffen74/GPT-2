# GPT-2
Fine-Tuning the GPT-2 with EconStor Data

## Dataset
[EconStor](https://www.econstor.eu/) is a repository of open access
economics papers. The dataset we worked with contained both
metadata for all papers in JSON as well as the full contents as txt files.

Unfortunately the full texts appear to have been scraped directly
from PDF files and still contain bibliographies, formatting like page numbers and headings as well as tables and figure descriptions, meaning additional cleanup was required before they could be used.

For our work we have decided to use a subset of papers related to the topic of climate change.

## Dataset preparation
The notebook [00_import_econstor_data.ipynb](./00_import_econstor_data.ipynb) handles downloading the dataset and saving it to Google drive.

[02_prepare_fulltext.ipynb](./02_prepare_fulltext.ipynb) handles initial pre-processing of full text papers. Further processing was required to handle journal-specific formatting.
The results from this are stored in `02_fulltexts_climate-change`, which contains 276 papers in total.


The script [02a_merge_fulltexts.py](./02a_merge_fulltexts.py) can be used to merge all paper texts into a single file.

## Approaches for fine-tuning GPT-2
We looked into different approaches for fine-tuning GPT-2 on Google Colab and ended up working with two different libraries,
both by the talented Max Woolf.

### [gpt-2-simple](https://github.com/minimaxir/gpt-2-simple)
gpt-2-simple was published in mid 2019, is based on the original Tensorflow (<2.0) implementation of GPT-2 and comes with 
a Colab notebook.

It is limited to generating a maximum of 1024 tokens per request and struggles with GPU memory limits when using larger models
and large input datasets. There is however [a fork](https://github.com/drfinkus/gpt-2-simple) that should not have
the latter problem.

### [aitextgen](https://github.com/minimaxir/aitextgen)
aitextgen was started in early 2020 and is designed to be a successor to gpt-2-simple. It is built using
a PyTorch implementation of GPT-2 from Hugging Face Transformers. This means that it should be able to make use of
upstream improvements in the future.

aitextgen does train well on the 124M model, can import trained gpt-2-simple models, and splits tokenization
from model training, allowing users to tokenize datasets ahead of time, even on a different machine.

However as of early 2021, this library still suffers from some a couple [known issues](https://github.com/minimaxir/aitextgen#known-issues).
Namely finetuning larger models is broken (and using FP16 failed for us as well), and we had to pin some dependencies to older versions
as recent updates had broken the notebook ([issue](https://github.com/minimaxir/aitextgen/issues/78)).
