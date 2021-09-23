import pandas as pd
import numpy as np
import os
import re

from urllib.parse import urlparse


df = pd.read_csv('es_material.csv', low_memory=False)






weave = 'twill|satin|tabby'
figured_weave = 'embroidery|velvet|damask|printed_fabric|damasse|lampas|patterned_fabric|brocatelle'
plain = 'cannele|metal_weft|rippled_effect_fabric|gauze'
weft = 'effect'
other_technique = 'other_technique'

paper = 'paper'
metal_silk = 'metal_thread|gold_thread|silver_thread|metal'
fibres = 'vegetal_fibre|animal_fibre|mixed_fibre|synthetic_fibre'
other = 'other_material'

    
conditions_mat = [
df['material_group'].astype(str).str.contains(paper),
df['material_group'].astype(str).str.contains(metal_silk),
df['material_group'].astype(str).str.contains(fibres),
df['material_group'].astype(str).str.contains(other)]

choices_tech = ['weave', 'figured_weave','plain', 'weft', 'other_technique']
choices_mat = ['paper', 'metal_silk', 'fibre', 'other']

    



df['museum'] = df['museum'].apply(lambda x: urlparse(x).path.rsplit("/", 1)[-1])

df['material_group'] = df['material_group'].apply(lambda x: urlparse(x).path.rsplit("/", 1)[-1] if type(x) != float else x)






df = df.groupby(['obj'], as_index=False)['museum','text','material_group'].agg(lambda x: list(dict.fromkeys(list([i for i in x if pd.notna(i)]))))


#these three lines remove the material group "animal_fibre", if it has other material groups, too
df['material_group'] = df['material_group'].astype(str).str.replace("'animal_fibre',", "")
df['material_group'] = df['material_group'].astype(str).str.replace(", 'animal_fibre'", "")
df['material_group'] = df['material_group'].astype(str).str.replace(", 'animal_fibre',", ",")




df = df.reindex(columns=['obj','museum','text','material_group'])
df = df.sort_values(by=['museum'])

df['museum'] = df['museum'].str[0]
df = df.drop(df[df['material_group'].astype(str).str.contains("',")].index)
df = df.drop(columns=['obj', 'museum'])
df['text'] = df['text'].str.get(0)
df['material_group'] = df['material_group'].astype(str).str.strip('[]')
df['material_group'] = df['material_group'].astype(str).str.strip()



df = df.rename(columns={"material_group": "label"})
df.to_csv('es_material_post2.csv', index=False)
