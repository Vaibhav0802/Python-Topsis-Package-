import sys
import pandas as pd
import math
import os
import numpy as np
# total arguments
def Topsis_dataset(file,Impacts,Weights):
  # df11=pd.read_csv(file)
  # print("You input file name is")
  # print(file)
  # print(impacts)
  # print(weights)
  # print(result)
  # print(df11)
  # n = len(sys.argv)
  # if n != 5:
  #   raise Exception("Wrong number of args.")  # No. of arguments
  try:
    f = open(file, 'r')
  except FileNotFoundError:
    raise Exception("Input File not found")  # file not found
  name, extension = os.path.splitext(file)
  if extension != '.csv':
    raise Exception("Input file is not a csv file")  # not a csv file
  # name2, extension2 = os.path.splitext(sys.argv[4])
  # if extension2 != '.csv':
  #   raise Exception("Output file is not a csv file")
  #
  # out=sys.argv[4]
  # yo=out[-4:]
  # if yo!='.csv':
  #   raise Exception("Output file must be .csv file")
  # li=[]
  # for i in range(len(weights)):
  #     if(i%2==0):
  #         li.append(float(weights[i]))
  weights = str(Weights)
  li = weights.split(",")
  flag = 0
  for i in range(len(li)):
    if li[i].isdigit():
      li[i] = int(li[i])
    elif li[i].replace('.', '', 1).isdigit() and li[i].count('.') < 2:
      li[i] = float(li[i])
    else:
      flag = 1
  if flag == 1:
    raise Exception("Weights must be ',' separated")
  impacts = str(Impacts)
  imp = []
  f = 0
  for i in range(len(impacts)):
    if (i % 2 == 0):
      if (impacts[i] == '+' or impacts[i] == '-'):
        imp.append(impacts[i])
      else:
        f = 1
  if f == 1:
    raise Exception("Impacts should either be '+' or '-'")  # + or - weights

  fl = 0
  for i in range(len(impacts)):
    if (i % 2 != 0):
      if impacts[i] != ',':
        fl = 1
  if fl == 1:
    raise Exception("Impacts must be ',' separated")  # impacts ',' separated
  # r_name = str(sys.argv[4])
  df = pd.read_csv(file)
  data = df.copy(deep=True)
  # print(df)

  df1 = df.applymap(np.isreal)
  ro = df1.shape[0]
  co = df1.shape[1]
  fla = 0
  for i in range(1, co):
    if df1.iloc[0, i] == False:
      fla = 1
  if fla == 1:
    raise Exception("Second to last column must be numeric")  # second to last column numeric
  c = df.shape[1]
  if c < 3:
    raise Exception("Number of Columns in the input file are less than 3.")  # no. of input files
  if len(imp) == len(li) and len(li) == c - 1:
    pass
  else:
    raise Exception(
      "No. of weights, impacts and No. of numerical rows must be equal")  # no. of weights, impacts and columns
  for j in range(1, c):
    sum = 0
    for i in df.iloc[:, j]:
      sum = sum + (i * i)
    n = math.sqrt(sum)
    r = df.shape[0]
    for i in range(r):
      df.iloc[i, j] = df.iloc[i, j] / n
  # print(df)
  # li=[1,1,1,2,1]
  r = df.shape[0]
  for i in range(0, r):
    c = df.shape[1]
    for j in range(1, c):
      df.iloc[i, j] = df.iloc[i, j] * li[j - 1]
  # print(df)

  # imp=['+','+','-','+','-']
  df.iloc[:, 1].max()
  c = df.shape[1]
  b = ['best']
  w = ['Worst']
  for i in range(1, c):
    if imp[i - 1] == '+':
      b.append(df.iloc[:, i].max())
      w.append(df.iloc[:, i].min())
    else:
      b.append(df.iloc[:, i].min())
      w.append(df.iloc[:, i].max())
  # print(df)

  sb = []
  sw = []
  r = df.shape[0]
  c = df.shape[1]
  for i in range(0, r):
    sum1 = 0
    sum2 = 0
    for j in range(1, c):
      a = df.iloc[i, j] - b[j]
      sum1 = sum1 + a * a
      d = df.iloc[i, j] - w[j]
      sum2 = sum2 + d * d
    sb.append(math.sqrt(sum1))
    sw.append(math.sqrt(sum2))
  # print(sb)
  # print(sw)

  p = []
  du = []
  for i in range(len(sb)):
    app = sw[i] / (sw[i] + sb[i])
    p.append(app)
    du.append(app)
  # print(p)

  du.sort(reverse=True)

  rank = []
  for i in range(len(p)):
    for j in range(len(du)):
      if p[i] == du[j]:
        rank.append(j + 1)

  data['Topsis Score'] = p
  data['Rank'] = rank

  data.to_csv('Toposis-102083059-result.csv', index=False)

#Toposis_dataset(file='102083059-data.csv',Weights="0.25,0.25,0.25,0.25",Impacts="-,+,+,+")







