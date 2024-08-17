import pandas as pd
import numpy as np
import os


path = '/home/ubuntu/proj/rt-dataset/src/data'

# demo

df = pd.read_csv(os.path.join(path, 'demographic.csv'))


# 删除民族列
df = df.drop('ethnicity', axis=1)

# 翻译
gender_translation = {
    '女': 'female',
    '男': 'male'
}

edu_translation = {
    '本科': "bachelor's degree",
    '大专': "associate degree",
    '硕士': "master's degree",
    '博士': "doctorate degree",
}

smoke_translation = {
    '从不抽烟': "never smokes",
    '偶尔吸（累计吸烟＜10包）': "occasional smoker (cumulative smoking <10 packs)",
    '现在吸（累计吸烟＞10包）': "current smoker (cumulative smoking >10 packs)",
    '以前吸（累计吸烟＞10包），但近一年不吸': "former smoker (cumulative smoking >10 packs), but not in the past year"
}

drink_translation = {
    '从不饮酒': "never drinks",
    '偶尔饮（每周＜1次）': "drinks occasionally (less than once a week)",
    '以前饮（每周＞1次），近1年不饮': "drank in the past (more than once a week), but not in the past year",
    '现在习惯饮（每周＞1次）': "current regular drinker (more than once a week)"
}

# Now we'll replace the values in the dataframe using the mapping dictionaries
df['gender'] = df['gender'].map(gender_translation)
df['edu'] = df['edu'].map(edu_translation)
df['smoke'] = df['smoke'].map(smoke_translation)
df['drink'] = df['drink'].map(drink_translation)

df.head()

df.to_csv(os.path.join(path, 'demographic.csv'), index=False)