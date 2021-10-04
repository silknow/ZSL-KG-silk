# Zero-Shot Information Extraction to Enhancea Knowledge Graph Describing Silk Textiles


This repository contains the code for reproducing the results reported in the paper "Zero-Shot Information Extraction to Enhancea Knowledge Graph Describing Silk Textiles" at the [LaTeCH-CLfL 2021](https://sighum.wordpress.com/events/latech-clfl-2021/) workshop co-located with [EMNLP 2021](https://2021.emnlp.org/).


## Requirements

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

## Instructions 

### 1. [Queries](https://github.com/silknow/ZSL-KG-silk/tree/main/queries)
   Query the [SILKNOW Knowledge graph](https://ada.silknow.org) on https://data.silknow.org/sparql by copy-pasting the content of these SPARQL files. Set "Results    Format" to "CSV" before clicking on "Exectute Query" for each query.

   The files are named after language and property type, for example English and material: 
   [en_material.sparql](https://github.com/silknow/ZSL-KG-silk/blob/main/queries/en_material.sparql). The queries can be adjusted, but they are set up as in          the paper, which means that per file only records of specific museums and properties get exported from the SILKNOW Knowledge Graph. The property values are        based on concept URIs from the [SILKNOW Thesaurus](https://skosmos.silknow.org/thesaurus/en/).

   The resulting CSVs have several columns: "obj" for the object URI, "museum" for the museum URI, "text" for the textual description and a last one for the          property group, which corresponds to the class label. 

### 2. [Scripts](https://github.com/silknow/ZSL-KG-silk/tree/main/preprocessing)
For each language and property combination of the queries there is a preprocessing python script that needs to be run for every query output respectively. If your file names are different, adjust them inside the code.

These scripts do some basic formatting operatins and make sure that one row represents one museum object. If you want to perform a test/train split it is recommended to do it after this step.

### 3. [Notebooks](https://github.com/silknow/ZSL-KG-silk/tree/main/notebooks)
Run the notebooks for each property / language combination respectively. The notebooks contain all relevant code and show the results at the bottom. They also produce another CSV file each with the predictions. 
