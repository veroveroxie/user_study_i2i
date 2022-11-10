import numpy as np
import os
import pandas as pd

input_images = sorted(os.listdir('testA'))[:100]
qs_images = sorted(os.listdir('qsattn'))[:100]
ours_images = sorted(os.listdir('ours'))[:100]
negcut_images = sorted(os.listdir('negcut'))[:100]

input_urls = []
for fname in input_images:
    input_urls.append('https://raw.githubusercontent.com/veroveroxie/user_study_i2i/main/testA/'+fname)

qs_urls = []
for fname in qs_images:
    qs_urls.append('https://raw.githubusercontent.com/veroveroxie/user_study_i2i/main/qsattn/'+fname)

ours_urls = []
for fname in ours_images:
    ours_urls.append('https://raw.githubusercontent.com/veroveroxie/user_study_i2i/main/ours/'+fname)

negcut_urls = []
for fname in negcut_images:
    negcut_urls.append('https://raw.githubusercontent.com/veroveroxie/user_study_i2i/main/negcut/'+fname)

df = pd.DataFrame()
df['input_image_url'] = input_urls
df['image_A_url'] = qs_urls
df['image_B_url'] = ours_urls
df['image_C_url'] = negcut_urls

df.to_csv('my_dict_cat2dog.csv', index=False)
