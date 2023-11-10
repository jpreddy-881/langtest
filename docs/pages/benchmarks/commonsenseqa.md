---
layout: docs
header: true
seotitle: CommonsenseQA Benchmark | LangTest | John Snow Labs
title: CommonsenseQA
key: benchmarks-commonsenseqa
permalink: /docs/pages/benchmarks/commonsenseqa/
aside:
    toc: true
sidebar:
    nav: benchmarks
show_edit_on_github: true
nav_key: benchmarks
modify_date: "2019-05-16"
---

### CommonsenseQA
Source: [CommonsenseQA: A Question Answering Challenge Targeting Commonsense Knowledge](https://arxiv.org/abs/1811.00937)

The CommonsenseQA dataset is a multiple-choice question answering dataset that aims to test the ability of natural language processing models to answer questions that require commonsense knowledge. The dataset consists of questions with five choices each. The questions were generated by Amazon Mechanical Turk workers, who were asked to create questions based on a given source concept and three target concepts related to it. The questions require different types of commonsense knowledge to predict the correct answers. The dataset covers various topics such as science, history, and everyday life.
You can see which subsets and splits are available below.

{:.table2}
| Split Name                        | Details                                                                                                                                                                |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CommonsenseQA-test**            | Testing set from the CommonsenseQA dataset, containing 1140 questions. This dataset does not contain labels and accuracy & fairness tests cannot be run with it.       |
| **CommonsenseQA-test-tiny**       | Truncated version of CommonsenseQA-test dataset which contains 50 questions. This dataset does not contain labels and accuracy & fairness tests cannot be run with it. |
| **CommonsenseQA-validation**      | Validation set from the CommonsenseQA dataset, containing 1221 question and answer examples.                                                                           |
| **CommonsenseQA-validation-tiny** | Truncated version of CommonsenseQA-validation dataset which contains 50 question and answer examples.                                                                  |

Here is a sample from the dataset:

{:.table2}
| question                                                                                     | answer |
| -------------------------------------------------------------------------------------------- | ------ |
| If you jump in any of the oceans you will get? A. tanned B. wet C. wide D. very deep E. fish | B. wet |