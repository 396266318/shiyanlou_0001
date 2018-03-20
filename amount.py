#!/usr/bin/env python3
#coding=utf-8
threshold = 3500
def amount_number(new_amount):
    try:
        if new_amount is int:
            print("输入的是数字")
        if new_amount >= 80000:
            tax = (new_amount - threshold) * 0.45 - 13505
            print('%.2f' % tax)
        elif new_amount >= 55000 or new_amount >= 80000:
            tax = (new_amount - threshold) * 0.35 - 5505
            print('%.2f' % tax)
        elif new_amount >= 35000 or new_amount >= 55000:
            tax = (new_amount - threshold) * 0.30 - 2755
            print('%.2f' % tax)
        elif new_amount >= 9000 or new_amount >= 35000:
            tax = (new_amount - threshold) * 0.25 - 1005
            print('%.2f' % tax)
        elif new_amount >= 4500 or new_amount >= 9000:
            tax = (new_amount - threshold) * 0.20 - 555
            print('%.2f' % tax)
        elif new_amount >= 1500 or new_amount >= 4500:
            tax = (new_amount - threshold) * 0.10 - 105
            print('%.2f' % tax)
        elif new_amount < 1500:
            tax = (new_amount - threshold) * 0.03
            print('%.2f' % tax)
    except:
        print("请输入整数")

# def change():
#     global a
#     a = 90


if __name__ == "__main__":
    amount = int(input("Please input:"))
    amount_number(int(amount))
