from random import randint
from keyboard import add_hotkey

global xlength, ylength, minecount, mines, visible, xcur, ycur
xlength = 20
ylength = 20
minecount = 20
mines = [[0 for i in range(xlength)] for j in range(ylength)]
visible = [[False for i in range(xlength)] for j in range(ylength)]
xcur = 1
ycur = 1

def show():
	string = ""
	for y in range(ylength):
		for x in range(xlength):
			if visible[y][x]:
				if mines[y][x] < 0:
					string += "M" #⚙
				elif mines[y][x] == 0:
					if x == xcur and y == ycur:
						string += "|"
					else:
						string += "_"
				else:
					if x == xcur and y == ycur:
						string += eval(rf"'\u246{mines[y][x]-1}'")
					else:
						string += str(mines[y][x])
			else:
					if x == xcur and y == ycur:
						string += "◫"
					else:
						string += "☐"
		string += "\n"
	print(string)
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

def move_cursor(x, y):
    xcur += x
    if xcur < 0:
        xcur = 0
    elif xcur > xlength:
        xcur = xlength
    ycur += y
    if ycur < 0:
        ycur = 0
    elif ycur > ylength:
        ycur = ylength
    show()

add_hotkey("right_arrow",move_cursor,args=[1,0])

i = minecount
while i > 0:
	x = randint(0,xlength-1)
	y = randint(0,ylength-1)
	if mines[y][x] < 0:
		continue
	mines[y][x] = -99
	nearcell("mines","+= 1", x, y)
	i -= 1

nearcell("visible","= True", xcur, ycur)
curs = "◫☐①⚙"

show()