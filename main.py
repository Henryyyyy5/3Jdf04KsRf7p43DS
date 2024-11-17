from random import randint

global xlength
xlength = 6
global ylength
ylength = 6
global minecount
minecount = 6
global mines
mines = [[0 for i in range(xlength)] for j in range(ylength)]
global visible
visible = [[False for i in range(xlength)] for j in range(ylength)]

def show():
  string1 = ""
  string2 = ""
  for i in range(y):
    for j in range(x):
      if mines[i][j] < 0:
        string1 += "#"
      elif mines[i][j] == 0:
        string1 += "_"
      else:
        string1 += str(mines[i][j])
      if visible[i][j]:
        string2 += "#"
      else:
        string2 += "_"
    string1 += "\n"
    string2 += "\n"
  print(string1,"\n",string2)
  # print(mines)

def nearcell(list, val):
  if y > 0 and x > 0:
    exec(f"{list}d[y-1][x-1] += val
  if y > 0:
    mines[y-1][x] += val
  if y > 0 and x < xlength-1:
    mines[y-1][x+1] += val
  if x > 0:
    mines[y][x-1] += val
  if x < xlength-1:
    mines[y][x+1] += val
  if y < ylength-1 and x > 0:
    mines[y+1][x-1] += val
  if y < ylength-1:
    mines[y+1][x] += val
  if y < ylength-1 and x < xlength-1:
    mines[y+1][x+1] += val

i = minecount
while i > 0:
  x = randint(0,xlength-1)
  y = randint(0,ylength-1)
  if mines[y][x] < 0:
    continue
  mines[y][x] = -99
  nearcell("mines","+= 1")
  i -= 1

show()

xcur = 1
ycur = 1