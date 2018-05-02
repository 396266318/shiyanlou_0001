import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


courses_ori = pd.read_table('courses.txt', sep=',', header=0)

courses_ori.head()
i = pd.to_datetime(courses_ori['创建时间'])
courses_ts = pd.DataFrame(data=courses_ori.values, columns=courses_ori.columns, index=i)
courses_ts = courses_ts.drop('创建时间', axis=1)

courses_ts_A = courses_ts.copy()

courses_ts_W = courses_ts.resample('W').sum()

courses_ts_W['id'] = range(0, len(courses_ts_W.index.values))

courses_ts_A['平均学习时间'] = courses_ts_A['学习时间'] / courses_ts_A['学习人数']


# plt.plot_date(courses_ts_W.index, courses_ts_W['学习时间'], '-')
#sns.regplot('id', '学习时间', data=courses_ts_W, scatter_kws={'s': 3}, order=8, ci=None, truncate=True)
#sns.regplot('id', '学习人数', data=courses_ts_W, x_bins=12)

color = sns.color_palette()[5]
# print(color[0])
sns.jointplot('平均学习时间', '学习人数', kind='scatter', data=courses_ts_A, color=color[1], size=6, ratio=5, space=.2)
plt.xlabel('Time Series')
plt.ylabel('Study Time')
plt.show()
