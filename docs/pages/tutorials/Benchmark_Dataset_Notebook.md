---
layout: docs
header: true
seotitle: Tutorials | LangTest | John Snow Labs
title: Benchmark Dataset Notebooks
key: docs-test_specific_notebooks
permalink: /docs/pages/tutorials/Benchmark_Dataset_Notebook_Notebooks
sidebar:
    nav: tutorials
aside:
    toc: true
nav_key: tutorials
show_edit_on_github: true
modify_date: "2019-05-16"
---

<div class="main-docs" markdown="1"><div class="h3-box" markdown="1">
The following table provides an overview of various Benchmark Dataset notebooks. User can select from a list of benchmark datasets provided below to test their LLMs.

</div><div class="h3-box" markdown="1">

{:.table2}
| Tutorial Description                | Hub                           | Task                              | Open In Colab                                                                                                                                                                                                                                    |
| ----------------------------------- |
| **OpenbookQA**: Evaluate your model's ability to answer questions that require complex reasoning and inference based on general knowledge, similar to an "open-book" exam.                          | OpenAI                            | Question-Answering                | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/OpenbookQA_dataset.ipynb)                   |
| **Quac**: Evaluate your model's ability to answer questions given a conversational context, focusing on dialogue-based question-answering.                                | OpenAI                            | Question-Answering                | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/quac_dataset.ipynb)                         |
| **MMLU**: Evaluate language understanding models' performance in different domains. It covers 57 subjects across STEM, the humanities, the social sciences, and more.                                | OpenAI                            | Question-Answering                | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/mmlu_dataset.ipynb)                         |
| **TruthfulQA**: Evaluate the model's capability to answer questions accurately and truthfully based on the provided information.                          | OpenAI                            | Question-Answering                | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/TruthfulQA_dataset.ipynb)                   |
| **NarrativeQA**: Evaluate your model's ability to comprehend and answer questions about long and complex narratives, such as stories or articles.                         | OpenAI                            | Question-Answering                | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/NarrativeQA_Question_Answering.ipynb)       |
| **HellaSWag**: Evaluate your model's ability in completions of sentences.                           | OpenAI                            | Question-Answering                | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/HellaSwag_Question_Answering.ipynb)         |
| **BBQ**: Evaluate how your model responds to questions in the presence of social biases against protected classes across various social dimensions.                                 | OpenAI                            | Question-Answering                | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/BBQ_dataset.ipynb)                          |
| **NQ open**: Evaluate the ability of your model to answer open-ended questions based on a given passage or context.                             | OpenAI                            | Question-Answering                | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/NQ_open_dataset.ipynb)                      |
| **BoolQ**: Evaluate the ability of your model to answer boolean questions (yes/no) based on a given passage or context.                               | OpenAI                            | Question-Answering                | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/BoolQ_dataset.ipynb)                        |
| **XSum** : Evaluate your model's ability to generate concise and informative summaries for long articles with the XSum dataset. | OpenAI                            | Summarization                     | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/XSum_dataset.ipynb)                         |
| **LogiQA**: Evaluate your model's accuracy on Machine Reading Comprehension with Logical Reasoning questions.                             | OpenAI                            | Question-Answering                | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/LogiQA_dataset.ipynb)                       |
| **ASDiv**: Evaluate your model's ability answer questions based on Math Word Problems.                                | OpenAI                            | Question-Answering                | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/ASDiv_dataset.ipynb)                        |
| **BigBench**: Evaluate your model's performance on BigBench datasets by Google.                            | OpenAI                            | Question-Answering                | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/Bigbench_dataset.ipynb)                     |
| **MultiLexSum**: Evaluate your model's ability to generate concise and informative summaries for legal case contexts from the Multi-LexSum dataset                         | OpenAI                            | Summarization                     | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/MultiLexSum_dataset.ipynb)                  |
| **Legal-QA**: Evaluate your model's performance on legal-qa datasets                            | OpenAI                            | Legal-Tests                       | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/LegalQA_Datasets.ipynb)                     |
| **CommonSenseQA**: Evaluate your model's performance on the CommonsenseQA dataset                       | OpenAI                            | Question-Answering                | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/CommonsenseQA_dataset.ipynb)                |
| **SIQA**: Evaluate your model's performance by assessing its accuracy in understanding social situations.                                | OpenAI                            | Question-Answering                | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/SIQA_dataset.ipynb)                         |
| **PIQA**: Evaluate your model's performance on the PIQA dataset, which tests its ability to reason about everyday physical situations                               | OpenAI                            | Question-Answering                | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/PIQA_dataset.ipynb)                         |
| **Fiqa**: Evaluate your model's performance on the FiQA dataset, a comprehensive and specialized resource designed for finance-related question-answering tasks.                         | OpenAI                     | Question-Answering                       | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/Fiqa_dataset.ipynb)  |