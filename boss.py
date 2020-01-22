from colorama import init,Fore
from warrior import panda
class Dragon(panda):
	def __init__(self,xpos,ypos):
		super().__init__(xpos,ypos)
		self.__maxlife = 25
		self.SetDefault(xpos,ypos)

	def SetDefault(self,xpos,ypos):
		self._piece = []
		self._xpos = xpos
		self._ypos = ypos
		self._xshot = self._xpos+9
		self._yshot = self._ypos+10
		self._height = 15
		self._width = 40
		self._life = 25

	def ShotPos(self):
		return self._xshot, self._yshot

	def CreateDragon(self):
		with open('dragon.txt') as obj:
			for line in obj:
				self._piece.append(line)
	def PrintDragon(self,finalgrid):
		for i in range(self._xpos,self._xpos+self._height):
			for j in range(self._ypos,self._ypos+self._width-1):
				finalgrid[i][j] = Fore.BLUE + self._piece[i-self._xpos][j-self._ypos]
	def move(self,x):
		if self._xshot > x+2:
			if self._xpos-2>=3:
				self._xpos-=2
				self._xshot-=2
		elif self._xshot < x+2:
			if self._xpos+2<=23:
				self._xpos+=2
				self._xshot+=2
	def PrintLife(self):
		for i in range(self._life):
				print('|',end='')
		for i in range(self.__maxlife-self._life):
			print(' ',end='')


class DragonFire:
	def __init__(self,x,y):
		self.__fire = [[' ',Fore.RED + '~','~'],[Fore.RED+'~', ' ', Fore.RED+'O'],[' ',Fore.RED+'~','~']]  
		self.__xpos = x
		self.__ypos = y
	def PrintFire(self,finalgrid):
		for i in range(self.__xpos,self.__xpos+3):
			for j in range(self.__ypos,self.__ypos+3):
				finalgrid[i][j] = self.__fire[i-self.__xpos][j-self.__ypos]
				# print("\033["+str(int(i+self.__xpos))+";"+str(int(j+self.__ypos))+"H" + self.__fire[i][j],end='')

	def Move(self):
		self.__ypos-=3
	def Check(self):
		return self.__ypos
	def Xpos(self):
		return self.__xpos
	def Ypos(self):
		return self.__ypos
