# Question answering using GPT-2
For the question answering subproject, we attempted to fine-tune GPT-2 models on scientific papers and abstracts and then used few-shot prompts to ask the trained models specific questions relevant to the area of expertise covered by the papers.

We used two main approaches here, one using gpt-2-simple, as documented in [this notebook](./gpt-2-simple.ipynb) and another using aitextgen, documented in [this notebook](./aitextgen.ipynb).

For preprocessing we tried three different methods of merging the full-text papers. For the first one we simply joined all the text files into a single one. For the next one we attempted to remove new lines within paragraphs, as those appeared often as an artefact of the previous pdf format. For the last method we also removed short lines (>50 chars) that didn't appear to be part of any paragraph but instead headlines, tables or sources, all of which would have only polluted the dataset.

The different preprocessing scripts are documented in [merge_full_texts_3_approaches](./merge_full_texts_3_approaches.py).