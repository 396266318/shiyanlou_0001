#!/usr/bin/env python3
import sys

def calculator(num):
    wuxian = num - (num * 0.165) - 3500
    if wuxian <= 0:
       tax = 0
    elif wuxian <= 1500:
        tax = wuxian * 0.03
    elif wuxian <= 4500:
        tax = wuxian * 0.1 - 105
    elif wuxian <= 9000:
        tax = wuxian * 0.2 - 555
    elif wuxian <= 35000:
        tax = wuxian * 0.25 - 1005
    elif wuxian <= 55000:
        tax = wuxian * 0.30 - 2755
    elif wuxian <= 80000:
        tax = wuxian * 0.35 - 5505
    else:
        tax = wuxian * 0.45 - 13505
    wuxian_xin = 0.165 * num
    return format((num - wuxian_xin - tax), '.2f')
try:
    shuru = sys.argv[1:]
    for qie in shuru:
        print(qie.split(":")[0] + ':' + calculator(int(qie.split(":")[1])))
except IndexError:
    print("Parameter Error")
