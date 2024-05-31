# Thesis Appendix
### Thesis 🎓 Development of a Complex of Neural Networks for Linked Generation of Large Texts

This repository is devoted to a bachelor's thesis that proposes a novel pipeline for dataset creation for the NLP NN tasks. It proposes generating a half-synthesized dataset with the help of SOTA LLM GPT-4 API. This pipeline facilitates the development of an innovative dataset, which is anticipated to advance future research in the field of long-text generation.   
  
An experimental dataset, distinguished by its novel two-level structure and the extensive collection of metadata, was generated using the proposed pipeline. Future experiments which could be conducted using this dataset have the potential to yield insights that are advantageous for both academic research and practical applications.


### Files 📁 provided descriprion

##### 📄 `book_processing.py`

This file contains code for segmenting a book into parts, which are intended to serve as the target data for the dataset.

##### 📄 `OpenAI_API.ipynb`

This file outlines the comprehensive process of extracting elements for the dataset from API requests, encompassing the parsing of data, creating the final prompt, sending requests, collecting the dataset, and providing an example of the output.

### Dataset 📊 collected

The dataset created using this pipeline comprises two stages or sub-datasets: the first stage is dedicated to generating plots from summaries, and the second stage is focused on producing the final text. Metadata such as the authors and titles of the books, locations from the passages, characters involved, and one of six action types are collected to facilitate a broad spectrum of future experiments. The complete dataset is available on [HuggingFace](https://huggingface.co/datasets/Fleur-roar/Thesis_Development_of_a_Complex_of_Neural_Networks_for_Linked_Generation_of_Large_Texts/settings).
