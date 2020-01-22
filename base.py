from accessories import *
from random import randint,choice
from colorama import init,Fore

def CreateBase(grid):
	for i in range(45):
		new = []
		for j in range(5000):
			new.append(" ")
		grid.append(new)

	for i in range(5000):
		grid[0][i] = '+'
		grid[39][i] = '+'
	k=0
	for i in range(0,5000,10):
		if k%2==0:
			for j in range(i,i+10):
				grid[10][j]='-'
				grid[30][j]='-'
			for j in range(11,30):
				grid[j][i]='.'
				grid[j][i+9]='.'
			k=1
		else:
			k=0
	points = coins()
	boost = Boost()
	points.PrintCoins(grid)

#creating type2
	obstacle = Obstacle()
	qwe  = [1,2,3,4,5,1]
	# 1 for coin type 2
	# 2 for coin type 4
	# 3 for obstacle type 1
	# 4 for obstacle type 2
	# 5 for obstacle type slant
	for i in range(200,4000,50):
		a=1
		done = []
		for q in range(3):
			r = choice(qwe)
			while r in done:
				r = choice(qwe)
			done.append(r)
			if q==2 and 3 in done and 4 in done and 5 in done:
				continue
			if r==1:
				xpos = randint(a,a+8)
				ypos = randint(10,40)+i
				Coin1(xpos,ypos).PrintCoin(grid)  
			elif r==2:
				xpos = randint(a,a+8)
				ypos = randint(10,40)+i
				Coin2(xpos,ypos).PrintCoin(grid)  
			elif r==3:
				xpos = randint(a,a+9)
				ypos = randint(5,35)+i
				obstacle.PrintType1(grid,xpos,ypos)
			elif r==4:
				xpos = randint(a,a+3)
				ypos = randint(5,45)+i
				obstacle.PrintType2(grid,xpos,ypos)
			elif r==5:
				xpos = randint(a,a+3)
				ypos = randint(5,35)+i
				for j in range(10):
					grid[int(xpos+j)][int(ypos+j)] = Fore.RED + '\\'
					grid[int(xpos+j)][int(ypos+j+1)] = Fore.RED + '\\'
			a+=12
				

	boost.PrintBoost(grid)
	
def CreateBase2(finalgrid):
	for i in range(42):
		new = []
		for j in range(102):
			new.append(' ')
		finalgrid.append(new)
	for i in range(102):
		finalgrid[0][i] = '='
		finalgrid[39][i] = '='
		if i%2==0:
			finalgrid[1][i] = '\\'
			finalgrid[38][i] = '\\'
		else:
			finalgrid[1][i] = '/'
			finalgrid[38][i] = '/'
	for i in range(42):
		finalgrid[i][0] = '>'
		finalgrid[i][100] = '<'



