# Fine-Tuning the GPT-2 with Abstracts and Full Papers from the EconStor Database

## Summary
The overall goal of the two projects documented in this repository are the comparison of different fine-tuned GPT-2 models and the GPT-3 model without fine-tuning. The results might thereby give a hint to what extent fine-tuning is still a very worthwhile thing to do, or it might be more to focus on the integration of larger models and the design of the prompts for these models.  
This question will be even more pressing when estimated models comparable to GPT-3 or even better get fully open source, which is very probable looking at initiatives such as [EleutherAI](https://www.eleuther.ai/).

We compared the abilities of the different approaches via the following two projects.

### Abstract-Based Generation of TL;DRs
In this project, we provided the GPT models with the abstract of a fulltext paper and asked it to generate a Too-Long;Didn't-Read (TL;DR) summary of it, that is a one sentence summary of the corresponding full text paper.
#### Data
We used 148 open source papers with a focus on climate change from the EconStor database for fine-tuning the GPT-2 (including those used for validation) and five abstracts from papers on climate change that were not included in this database and served as test data.
#### Method
We compared three different models:
- a GPT-2 fine-tuned only with the abatracts of the papers
- a GPT-2 fine-tuned with the full texts of the papers (with title page and bibliography excluded)
- an untrained GPT-3
Further, we compared two different prompt approaches:
- a one-ohot approach, with only one example abstract and TL;DR provided
- a few-shot approach, with two example abstracts and TL;DRs provided
For each model and each approach five TL;DRs were generated. The generated TL;DRs were than compared using the [ROUGE score](https://en.wikipedia.org/wiki/ROUGE_(metric)) and four independent human ratings. The categories for the human ratings were defined to vary from 0 ("really bad") to 3 ("quite ok or better").

#### Results
Figure 1 and Figure 2 provide a summary of the results on the ROUGE score and on the quality according to the human ratings.
(I would propose to include the tables as screenshots from Excel and refer to the Excel in the GitHub for details.)

Figure 1
![Results of the ROUGE Score](03_tldr/figure1_ROUGE-score.png)


Figure 2
![Results of the Human Ratings](03_tldr/figure2_human-ratings.png)


### Answering of (Cimate Cange) Eonomic Specific Questions
In this project ...

#### Data
We used 148 open source papers with a focus on climate change from the EconStor database for fine-tuning the GPT-2 (including those used for validation).

#### Method


#### Results


## Details

### Dataset
[EconStor](https://www.econstor.eu/) is a repository of open access
economics papers. The dataset we worked with contained both
metadata for all papers in JSON as well as the full contents as txt files.

Unfortunately the full texts appear to have been scraped directly
from PDF files and still contain bibliographies, formatting like page numbers and headings as well as tables and figure descriptions, meaning additional cleanup was required before they could be used.

For our work we have decided to use a subset of papers related to the topic of climate change.

### Dataset preparation
The notebook [00_import_econstor_data.ipynb](./00_import_econstor_data.ipynb) handles downloading the dataset and saving it to Google drive.

[02_prepare_fulltext.ipynb](./02_prepare_fulltext.ipynb) handles initial pre-processing of full text papers. Further processing was required to handle journal-specific formatting.
The results from this are stored in `02_fulltexts_climate-change`, which contains 276 papers in total.


The script [02a_merge_fulltexts.py](./02a_merge_fulltexts.py) can be used to merge all paper texts into a single file.

### Approaches for fine-tuning GPT-2
We looked into different approaches for fine-tuning GPT-2 on Google Colab and ended up working with two different libraries,
both by the talented Max Woolf.

#### [gpt-2-simple](https://github.com/minimaxir/gpt-2-simple)
gpt-2-simple was published in mid 2019, is based on the original Tensorflow (<2.0) implementation of GPT-2 and comes with 
a Colab notebook.

It is limited to generating a maximum of 1024 tokens per request and struggles with GPU memory limits when using larger models
and large input datasets. There is however [a fork](https://github.com/drfinkus/gpt-2-simple) that should not have
the latter problem.

#### [aitextgen](https://github.com/minimaxir/aitextgen)
aitextgen was started in early 2020 and is designed to be a successor to gpt-2-simple. It is built using
a PyTorch implementation of GPT-2 from Hugging Face Transformers. This means that it should be able to make use of
upstream improvements in the future.

aitextgen does train well on the 124M model, can import trained gpt-2-simple models, and splits tokenization
from model training, allowing users to tokenize datasets ahead of time, even on a different machine.

However as of early 2021, this library still suffers from some a couple [known issues](https://github.com/minimaxir/aitextgen#known-issues).
Namely finetuning larger models is broken (and using FP16 failed for us as well), and we had to pin some dependencies to older versions
as recent updates had broken the notebook ([issue](https://github.com/minimaxir/aitextgen/issues/78)).

#### [GPT-3 api](https://openai.com/blog/openai-api/)
Generative Pre-trained Transformer 3 (GPT-3) is an autoregressive language model that uses deep learning to produce human-like text. It is the third-generation language prediction model in the GPT-n series (and the successor to GPT-2) created by OpenAI, a San Francisco-based artificial intelligence research laboratory.

You need to request the access in order to use the OpenAI API. opencampus.sh has an access to the API. So, we used the GPT-3 OpenAI API to generate the short answers for the climate change economics related questions and to generate the TL;DR for the abstract from the journals related to climate change economics.

The script [04a_GPT_3_QA.ipynb](./04a_GPT_3_QA.ipynb) is used to generate short answers for the climate change economics related questions and the script [04b_GPT_3_TLDR.ipynb](./04_GPT_3_TLDR.ipynb) is used to generate the TL;DR for the abstract from the journals related to climate change economics. 
