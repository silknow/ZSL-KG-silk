# Zero-Shot Information Extraction to Enhancea Knowledge Graph Describing Silk Textiles


This repository contains the code for reproducing the results reported in the paper "Zero-Shot Information Extraction to Enhancea Knowledge Graph Describing Silk Textiles" at the [LaTeCH-CLfL 2021](https://sighum.wordpress.com/events/latech-clfl-2021/) workshop co-located with [EMNLP 2021](https://2021.emnlp.org/).


## Requirements:

* python 3
* multiprocessing
* string
* pickle
* numpy
* pandas
* nltk
* tqdm
* matplotlib
* seaborn
* sklearn
* notebook

## Instructions: 

1.[Queries](https://github.com/silknow/ZSL-KG-silk/tree/main/queries): Query the [SILKNOW Knowledge graph](https://ada.silknow.org) on https://data.silknow.org/sparql by copy-pasting the content of these SPARQL files. Set "Results Format" to "CSV" before clicking on "Exectute Query" for each query.

The files are named after language and property type, for example English and material: [en_material.sparql](https://github.com/silknow/ZSL-KG-silk/blob/main/queries/en_material.sparql). The queries can be adjusted, but they are set up as in the paper, which means that per file only records of specific museums and properties get exported from the SILKNOW Knowledge Graph. The property values are based on concept URIs from the [SILKNOW Thesaurus](https://skosmos.silknow.org/thesaurus/en/).

2.[Scripts](https://github.com/silknow/ZSL-KG-silk/tree/main/preprocessing): Run the three Python scripts in the folder. If your file names are different, adjust them inside the code.

3.[Notebooks](https://github.com/silknow/ZSL-KG-silk/tree/main/notebooks): Run the notebooks for each property / language combination respectively. The notebooks contain all relevant code and show the results at the bottom. They also produce another CSV file each with the predictions. 
