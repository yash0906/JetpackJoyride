from colorama import init,Fore
END ='\033[0m'
from accessories import Magnet
class panda:
	def __init__(self,xpos,ypos):
		self._piece =[["_","_","_","_","_"],["|","0"," ","0","|"],["|"," ","^"," ","|"],["`","`","`","`","`"],["/","|"," ","|","\\"],[" ","/"," ","\\"," "],["/"," "," "," ","\\"]] 
		self._xpos = xpos
		self._ypos = ypos
		self._jump = False
		self._jumpcount = 0
		self._height = len(self._piece)
		self._width = len(self._piece[0])
		self._points = 0
		self._life = 3 
		self._shield = False 
		self._starttime = 0
		self._bxpos = 3
		self._bypos = 3
		self._minx = 5
		self._type1 = []
		self._type2 = []
		self._type3 = []
		self._type4 = []
		self._yl = 1
		self._yr = 4
		self.CreateSnake()
	def PrintPiece(self):
		for i in range(self._xpos,self._xpos+self._height):
			for j in range(self._ypos,self._ypos+self._width):
				try:
					print("\033["+str(i)+";"+str(j)+"H"+ Fore.WHITE + self._piece[i-self._xpos][j-self._ypos])
				except:
					pass
	def MoveLeft(self):
		if self._ypos>=4:
			self._ypos-=2

	def MoveRight(self):
		if self._ypos<=93:
			self._ypos+=2

	def MoveUp(self):
		self._jump = True
		self._jumpcount = 0
		if self._xpos-4>=self._minx:
			self._xpos-=4
		else:
			self._xpos=self._minx

	def MoveDown(self):
		if self._jump==False:
			self._jumpcount+=1
			if self._xpos+int(((self._jumpcount/3)**2)*0.5)<=36:#36
				self._xpos+=int(((self._jumpcount/3)**2)*0.5)
			else:
				self._xpos = 36#36
	def FalseJump(self):
		self._jump = False

	def PrintShield(self):
		if self._shield:
			for i in range(self._xpos-1,self._xpos+8):
				print("\033["+str(i)+";"+str(self._ypos-1)+"H"+ Fore.GREEN + '-')
				print("\033["+str(i)+";"+str(self._ypos+5)+"H"+ Fore.GREEN + '-')
			for i in range(self._ypos-1,self._ypos+6):
				print("\033["+str(self._xpos-1)+";"+str(i)+"H"+ Fore.GREEN + '-')
				print("\033["+str(self._xpos+7)+";"+str(i)+"H"+ Fore.GREEN + '-')

	def PrintLife(self,timeremaining):
		print('\033[1m' + 'COINS: ' + str(self._points) + "			" + 'LIFE: ' + str(self._life) + "		Time Remaining: " + str(100-timeremaining))

	def CheckShieldValidity(self,curr_time):
		if curr_time - self._starttime>=10:
			self._shield = False

	def CheckColision(self,grid,p,run,inc,booststart,curr_time):
		c = Fore.YELLOW + '$'
		e1 = Fore.RED + '_'
		e2 = Fore.RED + '|'
		e3 = Fore.RED + '\\'
		for i in range(self._xpos-4, self._xpos+3):
			for j in range(self._ypos-self._yl, self._ypos+self._yr):
				# grid[i][p+j] = '&'
				if grid[i][p+j]==c:
					grid[i][p+j] = ' '
					self._points+=1
				elif grid[i][p+j]==e1 or grid[i][p+j]==e2 or grid[i][p+j]==e3 :
					if self._shield:
						self._shield = False
					else:
						self._life-=1
					self._xpos = 37
					self._ypos = 35
					p+=50
					for q in range(p,p+100):
						for w in range(31,39):
							grid[w][q] = ' '
					if self._life<=0:
						run=False
				elif grid[i][p+j]=='B':
					inc = 2
					booststart = curr_time
		return p,run,inc,booststart
	
	def LegMove(self):
		if self._piece[6][0] == '/':
			self._piece[6][0] = '\\'
			self._piece[6][4] = '/'
		else:
			self._piece[6][0] = '/'
			self._piece[6][4] = '\\'
	def DecLife(self):
		self._life-=1
	def Life(self):
		return self._life
	def Xpos(self):
		return self._xpos
	def Ypos(self):
		return self._ypos
	def changecharacter(self):
		self._piece = []
		with open('commando.txt') as obj:
			for line in obj:
				self._piece.append(line)
		self._width = 10
		self._height = 6
		self._bxpos = 3
		self._bypos = 10
		self._minx = 6
		self._xpos = 34
		self._ypos = 15
	def BXpos(self):
		return self._bxpos
	def BYpos(self):
		return self._bypos
	def Shield(self):
		self._shield = True
	def StartShield(self,curr_time):
		self._starttime = curr_time
	def CreateSnake(self):
		with open('1.txt') as obj:
			for line in obj:
				self._type1.append(line)  
		with open('2.txt') as obj:
			for line in obj:
				self._type2.append(line)
		with open('3.txt') as obj:
			for line in obj:
				self._type3.append(line)
		with open('4.txt') as obj:
			for line in obj:
				self._type4.append(line)

	def ChangeSnake(self,k):
		self._piece = []
		self._height = 5
		self._width = 30
		self._yr = 14
		if k%4==0:
			for line in self._type1:
				self._piece.append(line)
		if k%4==1:
			for line in self._type2:
				self._piece.append(line)
		if k%4==2:
			for line in self._type3:
				self._piece.append(line)
		if k%4==3:
			for line in self._type4:
				self._piece.append(line)
	def ChangeToMondo(self):
		self._piece =[["_","_","_","_","_"],["|","0"," ","0","|"],["|"," ","^"," ","|"],["`","`","`","`","`"],["/","|"," ","|","\\"],[" ","/"," ","\\"," "],["/"," "," "," ","\\"]] 
		self._height = len(self._piece)
		self._width = len(self._piece[0])
		self._yr = 4




