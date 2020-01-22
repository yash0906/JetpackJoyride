import os
from random import randint
import signal
from colorama import init,Fore
import time
from getch import _getChUnix as getChar
from alarmexception import AlarmException
from boss import *
from warrior import *
from accessories import *
from base import *
init()
grid = []
snake=0
snakestart = time.time()
CreateBase(grid)
def TakeInput():
	
	def alarmhandler(signum, frame):
		raise AlarmException
	def user_input(timeout=0.06):
		signal.signal(signal.SIGALRM, alarmhandler)
		signal.setitimer(signal.ITIMER_REAL, timeout)

		try:
			val = getChar()()
			signal.alarm(0)
			return val
		except AlarmException:
			pass
		signal.signal(signal.SIGALRM, signal.SIG_IGN)
		return ''
	val = user_input()
	mondo.FalseJump()
	# bonus.FalseJump()
	global lasttime
	global snake
	global snakestart
	if val == 'w':
			mondo.MoveUp()
	elif val == 'd':
			mondo.MoveRight()
	elif val == 'a':
			mondo.MoveLeft()
	elif val == 's':
			mondo.MoveDown()
	elif val == 'b':
			shoot()
	elif val == ' ':
			if curr_time-lasttime>=60 and snake!=1:
				lasttime = curr_time
				mondo.Shield()
				mondo.StartShield(curr_time)
	elif val == 'q':
		quit()
	elif val=='x':
		snake=1
		snakestart = time.time()


os.system("clear")
k=0
p=0
mondo = panda(38,35)


bullets = []
def shoot():
	if len(bullets)<=8:
		bul = Bullet(mondo.Xpos()+mondo.BXpos(),mondo.Ypos()+mondo.BYpos())
		bullets.append(bul)


run=True
curr_time = 0
lasttime=0
magnettime = time.time()
magnet = Magnet()
inc = 1
booststart = 0
dragon = Dragon(5,55)
dragon.CreateDragon()
gamestart = time.time()
finalgrid = []
CreateBase2(finalgrid)
pp=0
f=0
points = [Fore.BLUE + '(' , Fore.BLUE + '\\' , Fore.BLUE + '@' , Fore.BLUE + "'" , Fore.BLUE + '-' , Fore.BLUE + '/', Fore.BLUE + ')', Fore.BLUE + '=', Fore.BLUE + '|', Fore.BLUE + '_', Fore.BLUE + 'o']
firetime = time.time()
dragonfire = []
game=0

print("\033[2;0H")
timeremaining = 0
v=0
dragtime = time.time()
while run:
	curr_time = time.time()
	timeremaining = curr_time-gamestart
	if 100-timeremaining<=0:
		run = False
	if curr_time-gamestart>=70:
		if pp<=100:
				if f==0:
					mondo.changecharacter()
					f=1 
				for j in range(40):
					print("\033["+str(j+4)+";"+str(101-pp)+"H"+ finalgrid[j][pp])
					print("\033["+str(j+4)+";"+str(100-pp)+"H"+ finalgrid[j][pp+1])
				pp+=2
		else:
			print("\033[0;0H")
			mondo.PrintLife(timeremaining)
			print('BOSS LIFE: ',end='')
			dragon.PrintLife()

			dragon.move(mondo.Xpos())
			dragon.PrintDragon(finalgrid)
			
			print("\033[3;0H")
			if curr_time-firetime>=0.7:
				x,y = dragon.ShotPos()
				dragonfire.append(DragonFire(x,y))
				firetime = curr_time
			for i in dragonfire:
				i.PrintFire(finalgrid)
				i.Move()
				if i.Check()<=2:
					dragonfire.remove(i)
			for i in range(40):
				for j in range(102):	
					if i>=38:
						print(Fore.WHITE + str(finalgrid[i][j]),end="")
					else:
						print(str(finalgrid[i][j]),end="")
				print()
				
			mondo.PrintPiece()
			for bullet in bullets:
				bullet.move()
				if bullet.Ypos() <=100:
					c = finalgrid[bullet.Xpos()-4][bullet.Ypos()]
					if c==' ':
						c = finalgrid[bullet.Xpos()-4][bullet.Ypos()+1]
					if c==' ':
						c = finalgrid[bullet.Xpos()-4][bullet.Ypos()+2]


				if bullet.Ypos() > 99 :
					bullets.remove(bullet)
				elif c==points[0] or c==points[1] or c==points[2] or c==points[3] or c==points[4] or c==points[5] or c==points[6] or c==points[7] or c==points[8] or c==points[9] or c==points[10] :
					bullets.remove(bullet)
					dragon.DecLife()
					if dragon.Life()==0:
						run = False
						game=1
				else:
					print("\033["+str(bullet.Xpos())+";"+str(bullet.Ypos())+"H"+ Fore.WHITE + '(O)')
			mondo.MoveDown()
			c = Fore.RED + '~'
			d = Fore.RED + 'O'

			for fire in dragonfire:
				wer=0
				for i in range(fire.Xpos(),fire.Xpos()+3):
					for j in range(fire.Ypos(),fire.Ypos()+3):
						if i<=mondo.Xpos()+2 and i>=mondo.Xpos()-4 and j<=mondo.Ypos()+8 and j>=mondo.Ypos()-1:
							dragonfire.remove(fire)
							mondo.DecLife()
							if mondo.Life()==0:
								run  = False
							wer=1
							break
					if wer==1:
						break

			for i in range(3,38):
				for j in range(1,100):	
					finalgrid[i][j]=' '
			for i in range(3,38):
				finalgrid[i][101] = ' '
			

	else:
		if snake==1:
			mondo.ChangeSnake(v)
			v+=1
		if curr_time-snakestart>30 and snake==1:
			snake=2
			mondo.ChangeToMondo()
		print("\033[0;0H")
		mondo.PrintLife(timeremaining)
		
		mondo.CheckShieldValidity(curr_time)
		
		if inc == 2:
			if curr_time-booststart >= 15:
				inc=1
		
		print("\033[3;0H")
		for i in range(40):
			for j in range(p,p+100):	
					print(Fore.CYAN + str(grid[i][j]),end="")
			print()
		p+=inc
		# magnet._existance = True
		if curr_time-magnettime>=15:
			magnet.Enable()
			magnettime = curr_time  
		magnet.Disable()
		mondo.MoveDown()
		# bonus.MoveDown()
		p,run,inc,booststart = mondo.CheckColision(grid,p,run,inc,booststart,curr_time)
		
		for bullet in bullets:
			bullet.move()
			if bullet.Ypos() > 99 or bullet.Xpos()>=42:
				bullets.remove(bullet) 
			else:
				if bullet.CheckColition(grid,p)==0:
					print("\033["+str(bullet.Xpos())+";"+str(bullet.Ypos())+"H"+ Fore.WHITE + '(O)')
				else:
					bullets.remove(bullet)

		
		mondo._xpos,mondo._ypos = magnet.MagnetAttraction(inc,mondo.Xpos(),mondo.Ypos())
		mondo.PrintShield()
		mondo.PrintPiece()
		if curr_time - dragtime >= 0.12 and snake==1:
			mondo.ChangeSnake(v)
			dragtime = curr_time
			v+=1
		if snake==0:
			mondo.LegMove()
			
	begin = time.time()
	Fore.BLACK
	TakeInput()
	Fore.RESET
	end = time.time()
	if end-begin<0.06:
		time.sleep(0.06-(end-begin))
# time.sleep(10)
os.system("clear")
	# time.sleep(.5)
gameover = []
if game==0:
	with open('gameover.txt') as obj:
		for line in obj:
			gameover.append(line)
else:
	with open('youwon.txt') as obj:
		for line in obj:
			gameover.append(line)
print("\033["+str(15)+";"+str(15)+"H")
for i in gameover:
	for j in i:
		print(j,end='')