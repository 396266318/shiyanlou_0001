import json
import pandas as pd
from matplotlib import pyplot as plt

'''
1、使用 Pandas 读取JOSN 文件数据
2、获取重复的用户ID数据
3、求解每位用户的对应的总学习时长
4、绘制线性图
5、设置图标题及坐标轴名称
'''

def data_plot():
    fig = plt.figure()
    ax = 0
    plt.show()

    return ax

def analysis_try(file):
    times = 0
    minutes = 0
    try:
        f = open(file)
        records = json.load(f)
        for item in records:
            times += 1
            minutes += item['minutes']
            # print(times, minutes)
            print(item)
            # df = pd.read_json(file)
            # df = df[df['user_id'] == user_id].minutes
            # print(user_id, df.count(), df.sum())
        f.close()
    except:
        pass
    print(times, minutes)


data = 'C:\\Users\\Administrator\\Documents\\GitHub\\shiyanlou_0001\\news\\Code\\user.json'

# analysis_try(data)

def analysis_plt(file):
    df = pd.read_json(file)
    data = df.groupby('user_id').sum()
    # print(data)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel('User ID')
    ax.set_ylabel('Study Time')
    ax.set_title("StudyData")
    ax.plot(data.index, data.minutes)
    plt.show()
    return ax


analysis_plt(data)
