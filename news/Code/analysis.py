import json
import pandas as pd

def analysis_json(file):
    times = 0
    minutes = 0
    with open(file, 'r') as f:
        records = json.load(f)
        for i in records:
            # if item['user_id'] != user_id:
            #     continue
            times += 1
            minutes += i['minutes']
            
            print(i['user_id'], times, minutes)


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
            user_id = item['user_id']
            # return user_id
            df = pd.read_json(file)
            df = df[df['user_id'] == user_id].minutes
            # print(user_id, df.count(), df.sum())
        f.close()
    except:
        pass 
    print(times, minutes)


def analysis_pd(file, user_id):
    df = pd.read_json(file)
    df = df[df['user_id'] == user_id].minutes
    print(df.count(), df.sum())


data = 'C:\\Users\\Administrator\\Documents\\GitHub\\shiyanlou_0001\\news\\Code\\user.json'

# analysis_json(data)
# user_list = analysis_try(data)
# print(user_list)
# analysis_pd(data, user_id)
analysis_pd(data, 2451)

# analysis_try(data)


