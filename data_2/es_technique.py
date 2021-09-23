import pandas as pd
import numpy as np
import os
import re

from urllib.parse import urlparse


df = pd.read_csv('es_technique.csv', low_memory=False)






weave = 'twill|satin|tabby'
figured_weave = 'embroidery|velvet|damask|printed_fabric|damasse|lampas|patterned_fabric|brocatelle'
plain = 'cannele|metal_weft|rippled_effect_fabric|gauze'
weft = 'effect'
other_technique = 'other_technique'

paper = 'paper'
metal_silk = 'metal_thread|gold_thread|silver_thread|metal'
fibres = 'vegetal_fibre|animal_fibre|mixed_fibre|synthetic_fibre'
other = 'other_material'


conditions_tech = [
df['technique_group'].astype(str).str.contains(weave),
df['technique_group'].astype(str).str.contains(figured_weave),
df['technique_group'].astype(str).str.contains(plain),
df['technique_group'].astype(str).str.contains(weft),
df['technique_group'].astype(str).str.contains(other_technique)]
    

choices_tech = ['weave', 'figured_weave','plain', 'weft', 'other_technique']
choices_mat = ['paper', 'metal_silk', 'fibre', 'other']

    


df['museum'] = df['museum'].apply(lambda x: urlparse(x).path.rsplit("/", 1)[-1])
df['technique_group'] = df['technique_group'].apply(lambda x: urlparse(x).path.rsplit("/", 1)[-1] if type(x) != float else x)




df = df.groupby(['obj'], as_index=False)['museum','text','technique_group'].agg(lambda x: list([i for i in x if pd.notna(i)]))

df = df.reindex(columns=['obj','museum','text','technique_group'])
df = df.sort_values(by=['museum'])


df['museum'] = df['museum'].str[0]

df = df.drop(columns=['obj', 'museum'])
df = df.drop(df[df['technique_group'].astype(str).str.contains("',")].index)
df = df.drop(df[df['technique_group'].astype(str).str.contains("other")].index)
df = df.drop(df[df['technique_group'].astype(str).str.contains("dyeing")].index)
df = df.drop(df[df['technique_group'].astype(str).str.contains("cannele")].index)
df = df.drop(df[df['technique_group'].astype(str).str.contains("effect")].index)
df = df.drop(df[df['technique_group'].astype(str).str.contains("print")].index)

df['text'] = df['text'].str.get(0)
df['technique_group'] = df['technique_group'].astype(str).str.strip('[]')
df['technique_group'] = df['technique_group'].astype(str).str.strip("'")
df['technique_group'] = df['technique_group'].astype(str).str.strip()
df = df.rename(columns={"technique_group": "label"})

df.to_csv('es_technique_post2.csv', index=False)
