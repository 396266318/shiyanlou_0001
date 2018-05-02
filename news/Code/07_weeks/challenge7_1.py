# -*- coding: utf8 -*-

import pandas as pd

file_data = 'C:\\Users\\Administrator\\Documents\\GitHub\\shiyanlou_0001\\news\\Code\\07_weeks\\ClimateChange.xlsx'

def data_clean():
    data = pd.read_excel('ClimateChange.xlsx', sheet_name="Data")

    # 处理 data 数据表 # 选取 EN.ATM.CO2E.KT 数据，并将国家代码设置为索引
    data = data[data['Series code']== 'EN.ATM.CO2E.KT'].set_index('Country code')
    # 剔除不必要的数据列
    data.drop(labels = ['Country name', 'Series code', 'SCALE', 'Decimals'], axis=1, inplace=True)
    # 将原数据集中不规范的空值替换为 NaN 方便填充
    data.replace({'..': pd.np.NaN}, inplace=True)
    # 对 NaN 空值进行向前和向后填充
    data = data.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)
    # 对填充后依旧全部为空值的数据行进行剔除
    data.dropna(how='all', inplace=True)
    data['Sum emissions'] = data.sum(axis=1)
    data = data['Sum emissions']

    # 处理 Country 数据表
    # 将国家代码设置为索引
    countries = pd.read_excel('ClimateChange.xlsx', sheet_name='Country')
    countries.set_index('Country code', inplace=True)
    # 剔除不必要的数据列
    countries.drop(labels=['Capital city', 'Region', 'Lending category'], axis=1, inplace=True)

    # 合并数据表,
    # 对Data 和 Country 表按照索引进行合并
    return pd.concat([data, countries], axis=1)

def co2():
    # 读取清洁后数据
    df = data_clean()
    # 按收入群体对数据进行求和
    df_sum = df.groupby('Income group').sum()

    df_max = df.sort_values(by='Sum emissions', ascending=False).groupby('Income group').head(1).set_index('Income group')
    df_max.columns = ['Highest emissions', 'Highest emission country']
    df_max = df_max.reindex(columns=['Highest emission country', 'Highest emissions'])

    df_min = df.sort_values(by='Sum emissions').groupby('Income group').head(1).set_index('Income group')
    df_min.columns = ['Lowest emissions', 'Lowest emission country']
    df_min = df_min.reindex(columns=['Lowest emission coumtry', 'Lowest emissions'])

    result = pd.concat([df_sum, df_max, df_min], axis=1)
    print(result)
    # return result


co2()
