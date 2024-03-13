import math

import pandas as pd


def count_n(tbl):
    n = 0
    for k in tbl.keys():
        n += tbl[k]
    return n

def count_Xv(tbl, n):
    sum = 0
    for k in tbl.keys():
        sum += tbl[k] * k

    return sum/n

def count_por(tbl, n, Xv, p):
    sum = 0
    for k in tbl.keys():
        sum += tbl[k] * (math.pow((k - Xv), p))

    return sum/n



df = pd.read_csv("gr-1.csv")

table = {2:0, 3:0, 4:0, 5:0}

for i, r in df.iterrows():
    table[int(r['mark'])] += 1


n = count_n(table)


Xv = count_Xv(table, n)
Dv = count_por(table, n, Xv, 2)
Sv = math.sqrt(Dv)

A = count_por(table, n, Xv, 3) / math.pow(Sv, 3)
E = count_por(table, n, Xv, 4) / math.pow(Sv, 4) - 3


