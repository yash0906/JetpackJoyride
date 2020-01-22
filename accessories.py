from colorama import init,Fore
from random import randint
class Bullet:
	def __init__(self,x,y):
		self.__xpos = x
		self.__ypos = y
		self.__piece = 'O)'
	def move(self):
		self.__ypos+=6
		# self._xpos+=1
	def Xpos(self):
		return self.__xpos
	def Ypos(self):
		return self.__ypos
	def CheckColition(self,grid,p):
		zxc=0
		e1 = Fore.RED + '_'
		e2 = Fore.RED + '|'
		e3 = Fore.RED + '\\'
		for i in range(self.__ypos,self.__ypos+6):
			if grid[self.__xpos-4][i+p]==e1 or grid[self.__xpos-4][i+p]==e2 or grid[self.__xpos-4][i+p]==e3 :
				xx = self.__xpos-4
				yy = i+p
				if grid[xx][yy]==e1:
					yyy = yy+1
					while grid[xx][yy]==e1 or grid[xx+1][yy]==e1 or grid[xx-1][yy]==e1:
						grid[xx][yy]=' '
						grid[xx-1][yy]=' '
						grid[xx+1][yy]=' '
						yy-=1
					while grid[xx][yyy]==e1 or grid[xx+1][yyy]==e1 or grid[xx-1][yyy]==e1:
						grid[xx][yyy]=' '
						grid[xx-1][yyy]=' '
						grid[xx+1][yyy]=' '
						yyy+=1
				elif grid[xx][yy]==e2:
					xxx = xx+1
					while grid[xx][yy]==e2 or grid[xx][yy+1]==e2 or grid[xx][yy-1]==e2:
						grid[xx][yy+1]=' '
						grid[xx][yy]=' '
						grid[xx][yy-1]=' '
						xx-=1
					while grid[xxx][yy]==e2 or grid[xxx][yy+1]==e2 or grid[xxx][yy-1]==e2:
						grid[xxx][yy+1]=' '
						grid[xxx][yy]=' '
						grid[xxx][yy-1]=' '
						xxx+=1
				else:
					xxx=xx+1
					yyy=yy+1
					while grid[xx][yy]==e3 or grid[xx][yy+1]==e3 or grid[xx][yy-1]==e3:
						grid[xx][yy+1]=' '
						grid[xx][yy]=' '
						grid[xx][yy-1]=' '
						xx-=1
						yy-=1
					while grid[xxx][yyy]==e3 or grid[xxx][yyy+1]==e3 or grid[xxx][yyy-1]==e3:
						grid[xxx][yyy+1]=' '
						grid[xxx][yyy]=' '
						grid[xxx][yyy-1]=' '
						xxx+=1
						yyy+=1
				zxc=1
				break
		return zxc
class Coin1:
	def __init__(self,x,y):
		self._type = [['$','$','$'],['$','$','$'],['$','$','$']]
		self._xpos = x
		self._ypos = y
		self._h = 3
		self._w = 3
	def PrintCoin(self,grid):
		for j in range(self._xpos,self._xpos+self._h):
			for k in range(self._ypos,self._ypos+self._w):
				grid[j][k] = Fore.YELLOW + self._type[j-self._xpos][k-self._ypos]

class Coin2(Coin1):
	def __init__(self,x,y):
		super().__init__(x,y)
		self._type = [[' ','$',' '],['$','$','$'],[' ','$',' ']]
class coins:
	def __init__(self):
		self.__type1 = []
		self.__type2 = []
		self.Create()

	def Create(self):
		with open('jetpack.txt') as obj:
			for line in obj:
				self.__type1.append(line)

		with open('joyride.txt') as obj:
			for line in obj:
				self.__type2.append(line)

	def PrintCoins(self,grid):
		for i in range(0,5):
			for j in range(100,143):
				grid[i+20][j] = Fore.YELLOW + self.__type1[i][j-100]
		for i in range(0,5):
			for j in range(160,200):
				grid[i+20][j] = Fore.YELLOW + self.__type2[i][j-160]

	
class Obstacle:
	def __init__(self):
		self.__type1 = [['_']*10]*2
		self.__h1=2
		self.__w1=10
		self.__type2 = [['|']*2]*10
		self.__h2=10
		self.__w2=2
	def PrintType1(self,grid,xpos,ypos):
		for j in range(xpos,xpos+self.__h1):
			for k in range(ypos,ypos+self.__w1):
				grid[j][k] = Fore.RED + self.__type1[j-xpos][k-ypos]

	def PrintType2(self,grid,xpos,ypos):
		for j in range(xpos,xpos+self.__h2):
			for k in range(ypos,ypos+self.__w2):
				grid[j][k] = Fore.RED + self.__type2[j-xpos][k-ypos]

class Enemy:
	def __init__(self,x,y):
		self.__Type1 = [['(','_',')','_','_','_',' '],[' ',' ',' ','|',' ','|','\\'],[' ',' ',' ','~',' ','~',' ']]
		self.__xpos = x
		self.__ypos = y
class Boost:
	def __init__(self):
		self.__Type = [['B','B','B'],['B','B','B'],['B','B','B']]

	def PrintBoost(self,grid):
		for i in range(0,4900,500):
			x = randint(0,50) + i
			y = randint(3,35)
			for j in range(3):
				for k in range(3):
					grid[int(y+j)][int(x+k)] = self.__Type[j][k]


class Magnet:
	def __init__(self):
		self._mType = [' ',' ',' ','~',' ',' ',' '],['(','(','(','O',')',')',')'],[' ',' ',' ','~',' ',' ',' ']
		self._mxpos = randint(5,35)
		self._mypos = 92
		self._existance = True
		self._parity =1 
	def PrintMagnet(self):
		for i in range(self._mxpos,self._mxpos+3):
			for j in range(self._mypos,self._mypos+7):
				print("\033["+str(i)+";"+str(j)+"H"+ Fore.BLUE + self._mType[i-self._mxpos][j-self._mypos])

	def Enable(self):
		self._existance = True
		self._mypos = 92
		self._mxpos = randint(5,38)
	def Disable(self):
		if self._mypos<=1:
			self._existance = False
	def MagnetAttraction(self,inc,x,y):
		if self._existance:
			self.PrintMagnet()
			self._mypos-=inc
			if self._mypos<=-2:
				self._mypos=-1
			if abs(x-self._mxpos)<=20 and abs(y-self._mypos)<=20:
				if x<self._mxpos and x<34:
					x+=1
				elif x>self._mxpos and x>3:
					x-=1
				if y<self._mypos and y<95:
					y+=1
				elif y>self._mypos and y>1:
					y-=1
		return x,y



