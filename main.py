from random import randint

global xlength
xlength = 20
global ylength
ylength = 20
global minecount
minecount = 10
global mines
mines = [[0 for i in range(xlength)] for j in range(ylength)]
global visible
visible = [[False for i in range(xlength)] for j in range(ylength)]

def show():
  string1 = ""
  string2 = ""
  for i in range(ylength):
    for j in range(xlength):
      if mines[i][j] < 0:
        string1 += "#"
      elif mines[i][j] == 0:
        string1 += "_"
      else:
        string1 += str(mines[i][j])
      if visible[i][j]:
        string2 += "_"
      else:
        string2 += "#"
    string1 += "\n"
    string2 += "\n"
  print(string1,"\n",string2,sep="")
  # print(mines)

def nearcell(list, val, x, y):
  exec(f"{list}[y][x] {val}")
  if y > 0 and x > 0:
    exec(f"{list}[y-1][x-1] {val}")
  if y > 0:
    exec(f"{list}[y-1][x] {val}")
  if y > 0 and x < xlength-1:
    exec(f"{list}[y-1][x+1] {val}")
  if x > 0:
    exec(f"{list}[y][x-1] {val}")
  if x < xlength-1:
    exec(f"{list}[y][x+1] {val}")
  if y < ylength-1 and x > 0:
    exec(f"{list}[y+1][x-1] {val}")
  if y < ylength-1:
    exec(f"{list}[y+1][x] {val}")
  if y < ylength-1 and x < xlength-1:
    exec(f"{list}[y+1][x+1] {val}")

i = minecount
while i > 0:
  x = randint(0,xlength-1)
  y = randint(0,ylength-1)
  if mines[y][x] < 0:
    continue
  mines[y][x] = -99
  nearcell("mines","+= 1", x, y)
  i -= 1

xcur = 1
ycur = 1
nearcell("visible","= True", xcur, ycur)
curs = "◫☐①⚙"
show()