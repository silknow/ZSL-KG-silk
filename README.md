# Zero-Shot Information Extraction to Enhance a Knowledge Graph Describing Silk Textiles


This repository contains the code for reproducing the results reported in the paper ["Zero-Shot Information Extraction to Enhancea Knowledge Graph Describing Silk Textiles"](https://aclanthology.org/2021.latechclfl-1.16/) at the [LaTeCH-CLfL 2021](https://sighum.wordpress.com/events/latech-clfl-2021/) workshop co-located with [EMNLP 2021](https://2021.emnlp.org/).


## Requirements

```
install -r requirements.txt
```

or

```
conda install --file requirements.txt
```

## Instructions 




### 1. [Language-specific sub-graphs](https://doi.org/10.5281/zenodo.5660501)
   First, you need to download two language-specific sub-graphs (English and Spanish) based on the ConceptNet Knowledge Graph hosted on 
   [Zenodo](https://doi.org/10.5281/zenodo.5660501). The code in the notebook (see 4. Notebooks) expects them to be in a folder named "neighborhoods", but this can be changed.



### 2. [Queries](https://github.com/silknow/ZSL-KG-silk/tree/main/queries)
   Query the [SILKNOW Knowledge graph](https://ada.silknow.org) on https://data.silknow.org/sparql by copy-pasting the content of thes SPARQL file in the folder      ["queries"](https://github.com/silknow/ZSL-KG-silk/tree/main/queries). Set "Results Format" to "CSV" before clicking on "Exectute Query" for each query.

   The files are named after language and property type, for example English and material: 
   [en_material.sparql](https://github.com/silknow/ZSL-KG-silk/blob/main/queries/en_material.sparql). The queries can be adjusted, but they are set up as in          the paper, which means that per file only records of specific museums and properties get exported from the SILKNOW Knowledge Graph. The property values are        based on concept URIs from the [SILKNOW Thesaurus](https://skosmos.silknow.org/thesaurus/en/). "http://data.silknow.org/vocabulary/627" stands for "Gold thread" e.g.

   The resulting CSVs have several columns: "obj" for the object URI, "museum" for the museum URI, "text" for the textual description and a last one for the          property group, which corresponds to the class label. 

### 3. [Scripts](https://github.com/silknow/ZSL-KG-silk/tree/main/preprocessing)
For each language and property combination of the queries there is a preprocessing python script in the folder ["scripts"](https://github.com/silknow/ZSL-KG-silk/tree/main/preprocessing) that needs to be run for every query output respectively. If your file names are different, adjust them inside the code.

These scripts do some basic formatting operations and make sure that one row represents one museum object. If you want to perform a test/train split it is recommended to do it after this step.

### 4. [Notebooks](https://github.com/silknow/ZSL-KG-silk/tree/main/notebooks)
Run the notebooks for each property / language combination respectively. The notebooks contain all relevant code and show the results at the bottom. They also produce another CSV file each with the predictions. 


### Cite this work
```
@inproceedings{schleider-troncy-2021-zero,
    title = "Zero-Shot Information Extraction to Enhance a Knowledge Graph Describing Silk Textiles",
    author = "Schleider, Thomas  and
      Troncy, Raphael",
    booktitle = "Proceedings of the 5th Joint SIGHUM Workshop on Computational Linguistics for Cultural Heritage, Social Sciences, Humanities and Literature",
    month = nov,
    year = "2021",
    address = "Punta Cana, Dominican Republic (online)",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.latechclfl-1.16",
    pages = "138--146",
}
```
