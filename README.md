# Research Paper Summarization System

## Problem Statement
The problem we're trying to address is that research papers, which contain important scientific or academic information, can be very long and difficult to understand. Reading them thoroughly takes a lot of time and can be quite tedious. Typically, people might only read the abstract (a short summary at the beginning of the paper) to get an idea of the research, but the abstract alone may not provide all the necessary details. 
Our goal is to create a special computer program or model that can take these lengthy research papers and generate concise, easy-to-understand summaries. These summaries will not miss out on any crucial information, ensuring that all the important points from the paper are captured accurately. This way, someone who wants to understand the content of a research paper can simply look at our summary, saving them the trouble of reading the entire paper. It's like having a shortcut to grasp the key findings and insights of a research paper quickly and efficiently.

## Our Project
We designed and implemented a research paper summarization system using a fine-tuned T5 model, achieving high ROUGE scores. To streamline user access, we deployed the model on Streamlit for enhanced interaction.

## Dataset Description
The Random Research Papers Dataset comprises a collection of over 600 research papers sourced from various sources on the web. Through a meticulous selection process, approximately 350 of the most relevant and high-quality papers have been curated for inclusion in this dataset.

### Contents
The dataset includes research papers covering a wide range of topics and disciplines, reflecting the diverse nature of academic research. Each paper is accompanied by relevant metadata such as title, authors, publication source, abstract, and publication date (if available). The papers cover various fields of study, including but not limited to, computer science, medicine, engineering, social sciences, and more.

## Getting Started

### Prerequisites
- Python 3.x
- Streamlit
- Transformers library from Hugging Face

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/rohan12345a/ResearchPaperSummarization
   cd research-paper-summarization
