import pandas as pd

def quarter_volume(file):

    data = pd.read_csv(file, header=0)
    s = data.Volume
    s.index = pd.to_datetime(data.Date)
    second_volume = s.resample('Q').sum().sort_values()[-2]

    return second_volume


data = 'C:\\Users\\Administrator\\Documents\\GitHub\\shiyanlou_0001\\news\\Code\\apple.csv'
print(quarter_volume(data))
