import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


data = 'C:\\Users\\Administrator\\Documents\\GitHub\\shiyanlou_0001\\news\\Code\\courses.txt'

def query_syl(file):

    courses_ori = pd.read_table(data, sep=',', header=0)  # pandas 导入文件，以',' 分割
    i = pd.to_datetime(courses_ori['创建时间'])  # 制作时间索引
    # 修改时间搓为 索引
    courses_ts = pd.DataFrame(data=courses_ori.values, columns=courses_ori.columns, index=i)
    # 删除之前的创建时间-列
    courses_ts = courses_ts.drop("创建时间", axis=1)
    # 按照周的频次-降采样
    courses_tx_W = courses_ts.resample('W').sum()
    courses_tx_W['id'] = range(0, len(courses_tx_W.index.values))

    courses_ts_A = courses_ts.copy()
    courses_ts_A['平均学习时间'] = courses_ts_A['学习时间'] / courses_ts_A['学习人数']
    # courses_ts_A.sort_values(by="平均学习时间", ascending=False).head()  # 前5条数据
    # courses_ts_A.sort_values(by="平均学习时间", ascending=False).tail()  # 后5条数据

    # 绘制线型图
    # plt.plot_date(courses_tx_W.index, courses_tx_W['学习时间'], '-') # 折线图
    # sns.regplot("id", "学习时间", data=courses_tx_W, scatter_kws={'s': 8}, order=10, ci=None, truncate=True)  # 趋势拟线图
    # sns.regplot('id', '学习人数', data=courses_tx_W, x_bins=10)  # 上升下降趋势图

    sns.jointplot("平均学习时间", "学习人数", kind='scatter', data=courses_ts_A)
    plt.xlabel('Time Series')
    plt.ylabel("Study Time")
    plt.show()

query_syl(data)