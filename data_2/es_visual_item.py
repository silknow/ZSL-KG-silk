import pandas as pd
import numpy as np
import os
import re

from urllib.parse import urlparse


df = pd.read_csv('es_visual_item.csv', low_memory=False)






weave = 'twill|satin|tabby'
figured_weave = 'embroidery|velvet|damask|printed_fabric|damasse|lampas|patterned_fabric|brocatelle'
plain = 'cannele|metal_weft|rippled_effect_fabric|gauze'
weft = 'effect'
other_depict = 'other_depict'

paper = 'paper'
metal_silk = 'metal_thread|gold_thread|silver_thread|metal'
fibres = 'vegetal_fibre|animal_fibre|mixed_fibre|synthetic_fibre'
other = 'other_material'


conditions_tech = [
df['depict_group'].astype(str).str.contains(weave),
df['depict_group'].astype(str).str.contains(figured_weave),
df['depict_group'].astype(str).str.contains(plain),
df['depict_group'].astype(str).str.contains(weft),
df['depict_group'].astype(str).str.contains(other_depict)]
    

choices_tech = ['weave', 'figured_weave','plain', 'weft', 'other_depict']
choices_mat = ['paper', 'metal_silk', 'fibre', 'other']

    


df['museum'] = df['museum'].apply(lambda x: urlparse(x).path.rsplit("/", 1)[-1])
df['depict_group'] = df['depict_group'].apply(lambda x: urlparse(x).path.rsplit("/", 1)[-1] if type(x) != float else x)




df = df.groupby(['obj'], as_index=False)['museum','text','depict_group'].agg(lambda x: list([i for i in x if pd.notna(i)]))

df = df.reindex(columns=['obj','museum','text','depict_group'])
df = df.sort_values(by=['museum'])


df['museum'] = df['museum'].str[0]

df = df.drop(columns=['obj', 'museum'])
df = df.drop(df[df['depict_group'].astype(str).str.contains("',")].index)
df = df[df['depict_group'].astype(str).str.contains('|'.join(['flower','plant','geometrical_shape']))]



df['text'] = df['text'].str.get(0)
df['depict_group'] = df['depict_group'].astype(str).str.strip('[]')
df['depict_group'] = df['depict_group'].astype(str).str.strip("'")
df['depict_group'] = df['depict_group'].astype(str).str.strip()
df = df.rename(columns={"depict_group": "label"})

df.to_csv('es_visual_item_post2.csv', index=False)
