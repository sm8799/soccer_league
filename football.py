import pygame
import sys
import time
import math
import random
from pygame.locals import *
pygame.init() # initialize pygame
pygame.font.init()
pygame.mixer.init()
clock = pygame.time.Clock()
bg = pygame.image.load('2.png')
back = pygame.image.load('fs.png')
p1 = pygame.image.load('7.jpeg')
gk1 = pygame.image.load('7.jpeg')
p2 = pygame.image.load('8.jpeg')
gk2 = pygame.image.load('8.jpeg')
b = pygame.image.load('9.gif')
bg_size = bg.get_size()
gk2_rect = gk2.get_rect()
gk1_rect = gk1.get_rect()
gk2_x = 949
gk2_y = 303
gk1_x = 43
gk1_y = 309
gk2_rect.center = gk2_x, gk2_y
gk1_rect.center = gk1_x, gk1_y
screen = pygame.display.set_mode([bg_size[0],bg_size[1] + 50])
pygame.display.set_caption('SoccerLeague')
back_rect = back.get_rect()
back_rect.center = 500,250
screen.blit(back, back_rect)
pygame.display.update()
g2_x = 988
g2_y = 300
you_g = cpu_g = 0
white = (255,255,255)
red = (0,0,128)
black =(0,0,0)
control = 2
arg = 0
g1_x = g1_y = 0
collected_gk1 = 0
collected_gk2 = 0
img_1 = 0
kick = 0
p1_x = 417
p1_y = 308
b_x = 498
b_y = 308
p2_x = 800
p2_y = 308
dim_x1 = 25
dim_y1 = 20
dim_x2 = 970
dim_y2 = 596
g2_x = 988
g2_y = 300
move_x = move_y = 0
b_rect = b.get_rect()
p1_rect = p1.get_rect()
p2_rect = p2.get_rect()
b_rect.center = b_x,b_y
p1_rect.center = p1_x,p1_y
p2_rect.center = p2_x,p2_y
connect = 0
prev = new = 0 
pk = 1
r = (200,0,0)
green = (0,200,0)
orange = (255,127,0)
grey = (50,50,50)
bright_r = (255,0,0)
bright_green = (0,255,0)
bright_orange = (255,215,0)

def move_p2(b_x, b_y, p2_x, p2_y, p1_x, p1_y):
	global control, arg, g1_x, g1_y, connect
	if arg == 0:
		g1_x = random.randint(0, 27)
		g1_y = random.randint(229, 392)
	d2 = math.hypot(p2_x - b_x, p2_y - b_y)
	d3 = math.hypot(b_x - g1_x, b_y - g1_y)
	d4 = math.hypot(p2_x - p1_x, p2_y - p1_y)
	d5 = math.hypot(p1_x - b_x, p1_y - b_y)
	p_x = b_x - p2_x
	p_y = b_y - p2_y
	if p_y > 0 :
		connect = 1
	elif p_y < 0 :
		connect = 2
	else:
		connect = 0
	if d2 > 26 and arg != 1 :
		p_x = p_x / d2
		p_y = p_y / d2
		p2_y = p2_y + p_y * 1.5
		p2_x = p2_x + p_x * 1.5
	elif control != 1:
		p_x = g1_x - b_x
		p_y = g1_y - b_y
		p_x = p_x / d3
		p_y = p_y / d3
		if d3 > 130 :
			b_y = (b_y + p_y*8)
			b_x = (b_x + p_x*8)
		else:
			b_x = b_x + p_x * 130
			b_y = b_y + p_y * 130
			p2_x = p2_x - 3
		return p2_x, p2_y,b_x,b_y
	return p2_x,p2_y,b_x,b_y

def goal(score,x,y,t):
	global arg
	global control, collected_gk1, collected_gk2, move_x, move_y, b_rect, p1_rect, p2_rect
	global img_1, kick, p1_x, p1_y, b_x, b_y, p2_x, p2_y, dim_x1, dim_x2, dim_y1, dim_y2, g2_x, g2_y
	arg = 0
	pygame.mixer.music.load('whistle.wav')
	pygame.mixer.music.play(1)
	score = 0
	x = str(x)
	y = str(y)
	scored = pygame.image.load('3.png')
	font = pygame.font.Font('freesansbold.ttf', 32)
	text = font.render('RED : BLUE', True, red)
	board = font.render(y+' : '+x, True, red)
	textRect = text.get_rect()
	board_rect = board.get_rect()
	textRect.center = 500, 437
	board_rect.center = 500, 500
	scored_rect = scored.get_rect()
	scored_x = 500
	scored_y = 167
	scored_rect.center = scored_x, scored_y
	screen.blit(scored,scored_rect)
	screen.blit(text,textRect)
	screen.blit(board, board_rect)
	pygame.display.update()
	time.sleep(3)
	img_1 = 0
	kick = 0
	p1_x = 417
	p1_y = 308
	b_x = 498
	b_y = 308
	p2_x = 800
	p2_y = 308
	dim_x1 = 25
	dim_y1 = 20
	dim_x2 = 970
	dim_y2 = 596
	g2_x = 988
	g2_y = 300
	move_x = move_y = 0
	b_rect = b.get_rect()
	p1_rect = p1.get_rect()
	p2_rect = p2.get_rect()
	b_rect.center = b_x,b_y
	p1_rect.center = p1_x,p1_y
	p2_rect.center = p2_x,p2_y
	football(score,t)

def move_p1(b_x, b_y, p1_x, p1_y, hit):
	global g1_x, g1_y
	g1_x = random.randint(0, 27)
	g1_y = random.randint(235, 392)
	d1 = math.hypot(p1_x - b_x, p1_y - b_y)
	d3 = math.hypot(b_x - g1_x, b_y - g1_y)
	p_x = b_x - p1_x
	p_y = b_y - p1_y
	p_x , p_y = p_x / d1, p_y / d1
	if d1 > 26:
		p1_x += p_x * 1.5
		p1_y += p_y * 1.5
	elif d1 <= 26 and hit == 1 :
		p_x = g1_x - b_x
		p_y = g1_y - b_y
		p_x = p_x / d3
		p_y = p_y / d3
		b_x = b_x + p_x * 130
		b_y = b_y + p_y * 130
		p1_x = p1_x - 3
	hit = 0
	return b_x, b_y, p1_x, p1_y, hit

def move_p2_penalty(b_x, b_y, p2_x, p2_y):
	global g1_x, g1_y
	g1_x = random.randint(0, 27)
	g1_y = random.randint(235, 392)
	d2 = math.hypot(p2_x - b_x, p2_y - b_y)
	d3 = math.hypot(b_x - g1_x, b_y - g1_y)
	p_x = b_x - p2_x
	p_y = b_y - p2_y
	if d2 > 26 :
		p_x = p_x / d2
		p_y = p_y / d2
		p2_y = p2_y + p_y * 2
		p2_x = p2_x + p_x * 2
		return b_x, b_y, p2_x, p2_y
	else :	
		p_x = g1_x - b_x
		p_y = g1_y - b_y
		p_x = p_x / d3
		p_y = p_y / d3
		b_x = b_x + p_x * 130
		b_y = b_y + p_y * 130
		p2_x = p2_x - 3
		return b_x, b_y, p2_x, p2_y

def penaltygoal(x, y) :
	k1 = str(x)
	k2 = str(y)
	scored = pygame.image.load('3.png')
	font = pygame.font.Font('freesansbold.ttf', 32)
	text = font.render('RED : BLUE', True, red)
	board = font.render(k1+' : '+k2, True, red)
	textRect = text.get_rect()
	board_rect = board.get_rect()
	textRect.center = 500, 437
	board_rect.center = 500, 500
	scored_rect = scored.get_rect()
	scored_x = 500
	scored_y = 167
	scored_rect.center = scored_x, scored_y
	screen.blit(scored,scored_rect)
	screen.blit(text,textRect)
	screen.blit(board, board_rect)
	pygame.display.update()
	time.sleep(3)

def gameover1(x,y):
	global pk
	pygame.mixer.music.load('whistle.wav')
	pygame.mixer.music.play(1)
	game = pygame.font.Font('freesansbold.ttf', 60)
	if y < x :
		go = game.render('TEAM RED HAS WON', True, white)
	elif y > x :
		go = game.render('TEAM BLUE HAS WON', True, white)
	elif y == x:
		go = game.render('Match Tied', True, white)
	k1 = str(x)
	k2 = str(y)
	font = pygame.font.Font('freesansbold.ttf', 32)
	text = font.render('RED : BLUE', True, white)
	board = font.render(k1+' : '+k2, True, white)
	textRect = text.get_rect()
	board_rect = board.get_rect()
	go_rect = go.get_rect()
	go_x = 500
	go_y = 267
	go_rect.center = go_x, go_y
	screen.blit(go,go_rect)
	textRect.center = 500, 359
	board_rect.center = 500, 413
	screen.blit(text,textRect)
	screen.blit(board, board_rect)
	pygame.display.update()
	time.sleep(3)
	pygame.quit()
	quit()
	
def gameover(x,y):
	global pk
	pygame.mixer.music.load('whistle.wav')
	pygame.mixer.music.play(1)
	game = pygame.font.Font('freesansbold.ttf', 60)
	if y < x :
		go = game.render('TEAM BLUE HAS WON', True, white)
	elif y > x :
		go = game.render('TEAM RED HAS WON', True, white)
	elif y == x:
		if pk == 1 :
			time.sleep(3)
			penaltyshoot()
		else :
			go = game.render('Match Tied', True, white)
	k1 = str(x)
	k2 = str(y)
	font = pygame.font.Font('freesansbold.ttf', 32)
	text = font.render('RED : BLUE', True, white)
	board = font.render(k2+' : '+k1, True, white)
	textRect = text.get_rect()
	board_rect = board.get_rect()
	go_rect = go.get_rect()
	go_x = 500
	go_y = 267
	go_rect.center = go_x, go_y
	screen.blit(go,go_rect)
	textRect.center = 500, 359
	board_rect.center = 500, 413
	screen.blit(text,textRect)
	screen.blit(board, board_rect)
	pygame.display.update()
	time.sleep(5)
	pygame.quit()
	quit()
	
	
def scoreboard(t, x, y, p1_rect, p2_rect, b_rect):
	global gk1, gk1_x, gk1_y, gk2, gk2_x, gk2_y, gk1_rect, gk2_rect
	x1 = x
	y1 = y
	x = str(x)
	y = str(y)
	w = int(t * 5 / 3)
	v = w % 60
	v = int(v)
	w = w // 60
	w = int(w)
	k3 = str(v)
	k4 = str(w)
	if v < 10:
		k3 = '0'+k3
	if w < 10:
		k4 = '0'+k4
	font = pygame.font.Font('freesansbold.ttf', 20)
	text = font.render('RED : BLUE', True, white, red)
	board = font.render(y+' : '+x, True, white, red)
	textRect = text.get_rect()
	board_rect = board.get_rect()
	font1 = pygame.font.Font('freesansbold.ttf', 30)
	timer = font1.render(k4+' : '+k3, True, white)
	timer_rect = timer.get_rect()
	timer_rect.center = 500, 655
	textRect.center = 102, 635
	board_rect.center = 102, 655
	screen.fill((0, 0, 0))
	screen.blit(bg, (0,0))
	screen.blit(b, b_rect)
	screen.blit(p1, p1_rect)
	screen.blit(p2, p2_rect)
	screen.blit(text,textRect)
	screen.blit(timer, timer_rect)
	screen.blit(board, board_rect)
	screen.blit(gk1, gk1_rect)
	screen.blit(gk2, gk2_rect)
	pygame.display.update()
	if w == 90 :
		gameover(x1, y1)

def move_gk1(gk1_x, gk1_y, p2_x, p2_y, b_x, b_y):
	global collected_gk1, connect, prev, new, arg, control
	d1 = math.hypot(gk1_x - b_x, gk1_y - b_y)
	p_y = (b_y - gk1_y) / d1
	if (abs(b_y - gk1_y) < 45 and d1 < 70) or d1 < 45:
		b_x = gk1_x + 26
		gk1_y = b_y
		collected_gk1 = 1
		arg = 0
	elif d1 < 80 :
		if b_y < gk1_y :
			gk1_y -= 30
		if b_y > gk1_y :
			gk1_y += 30
	'''elif control == 2:
		gk1_x = 42
		gk1_y += p_y * 2.5
		if gk1_y >= 395:
			gk1_y -= 5
		elif gk1_y <= 229:
			gk1_y += 5
		connect = 0
		collected_gk1 = 0'''
	return gk1_x, gk1_y, b_x, b_y

def move_gk2_pen(gk2_x, gk2_y, p1_x, p1_y, b_x, b_y):
	global collected_gk2, move_y, arg, control
	d1 = math.hypot(gk2_x - b_x, gk2_y - b_y)
	p_y = (b_y - gk2_y) / d1
	if (abs(b_y - gk2_y) < 40 and d1 < 65) or d1 < 45:
		b_x = gk2_x + 26
		gk2_y = b_y
		collected_gk2 = 1
		arg = 0
	elif d1 < 80 :
		if b_y < gk2_y :
			gk2_y -= 30
		if b_y > gk2_y :
			gk2_y += 30
		
	'''elif control == 1:
		gk2_x = 949
		gk2_y += p_y * 1.5
		if gk2_y >= 395:
			gk2_y -= 5
		elif gk2_y <= 229:
			gk2_y += 5
		connect = 0
		collected_gk2 = 0'''
	return gk2_x, gk2_y, b_x, b_y
	
def move_gk2(gk2_x, gk2_y, p1_x, p1_y, b_x, b_y):
	global collected_gk2, move_y, arg, control
	d1 = math.hypot(gk2_x - b_x, gk2_y - b_y)
	p_y = (b_y - gk2_y) / d1
	if (abs(b_y - gk2_y) < 40 and d1 < 65) or d1 < 45:
		b_x = gk2_x - 26
		gk2_y = b_y
		collected_gk2 = 1
		arg = 0
	elif control == 1:
		gk2_x = 949
		gk2_y += p_y * 1.5
		if gk2_y >= 395:
			gk2_y -= 5
		elif gk2_y <= 229:
			gk2_y += 5
		connect = 0
		collected_gk2 = 0
	return gk2_x, gk2_y, b_x, b_y
	
def gamereload1(b_x, b_y, p1_x, p1_y, p2_x, p2_y, p1_rect, p2_rect, b_rect):
	time.sleep(0.5)
	global gk1_y, gk2_y
	d1 = math.hypot(b_x - p1_x, b_y - p1_y)
	p_x = p1_x - b_x
	p_y = p1_y - b_y
	p_x, p_y = p_x / d1, p_y/ d1
	b_x =  b_x + p_x * 120
	b_y =  b_y + p_y * 120
	return b_x, b_y, p1_x, p1_y, p2_x, p2_y

def gamereload2(b_x, b_y, p1_x, p1_y, p2_x, p2_y):
	time.sleep(0.5)
	global gk2_x, gk2_y
	d1 = math.hypot(b_x - p2_x, b_y - p2_y)
	p_x = p2_x - b_x
	p_y =p2_y - b_y
	p_x, p_y = p_x / d1, p_y / d1
	b_x = b_x + p_x * 120
	b_y = b_y + p_y * 120
	return b_x, b_y, p1_x, p1_y, p2_x, p2_y
	
def penaltyshoot() :
	pygame.mixer.music.load('crowd.wav')
	pygame.mixer.music.play(-1)
	global you_g, cpu_g, gk1, gk1_x, gk1_y, gk2, gk2_x, gk2_y, gk1_rect, gk2_rect, pk
	global control, collected_gk1, collected_gk2, move_x, move_y, b_rect, p1_rect, p2_rect
	global img_1, kick, p1_x, p1_y, b_x, b_y, p2_x, p2_y, dim_x1, dim_x2, dim_y1, dim_y2, g2_x, g2_y
	score = 0
	x = y = 0
	count = 3
	hit = 0
	collected_gk1 = 0 
	collected_gk2 = 0
	pk = 0
	disp = pygame.image.load('11.jpg')
	disp_rect = disp.get_rect()
	disp_rect.center = 498, 307
	b_rect.center = b_x,b_y
	p2_rect.center = p2_x,p2_y
	p1_rect.center = p1_x,p1_y
	gk2_rect.center = gk2_x, gk2_y
	gk1_rect.center = gk1_x, gk1_y
	screen.blit(bg, (0,0))
	screen.blit(p1, p1_rect)
	screen.blit(b, b_rect)
	screen.blit(p2, p2_rect)
	screen.blit(disp, disp_rect)
	screen.blit(gk1, gk1_rect)
	screen.blit(gk2, gk2_rect)
	pygame.display.update()
	time.sleep(2)
	while count != 0 :
		running = True
		gk1_x, gk1_y = 46, 454
		gk2_x, gk2_y = 42, 307
		p1_x, p1_y = 181, 344
		p2_x, p2_y = 495, 304
		b_x, b_y = 125, 304
		b_rect.center = b_x,b_y
		p2_rect.center = p2_x,p2_y
		p1_rect.center = p1_x,p1_y
		gk2_rect.center = gk2_x, gk2_y
		gk1_rect.center = gk1_x, gk1_y
		screen.blit(bg, (0,0))
		screen.blit(p1, p1_rect)
		screen.blit(b, b_rect)
		screen.blit(p2, p2_rect)
		screen.blit(gk1, gk1_rect)
		screen.blit(gk2, gk2_rect)
		pygame.display.update()
		time.sleep(2)
		while running :
			clock.tick(30)
			b_rect.center = b_x,b_y
			p2_rect.center = p2_x,p2_y
			p1_rect.center = p1_x,p1_y
			gk2_rect.center = gk2_x, gk2_y
			gk1_rect.center = gk1_x, gk1_y
			screen.blit(bg, (0,0))
			screen.blit(p1, p1_rect)
			screen.blit(b, b_rect)
			screen.blit(p2, p2_rect)
			screen.blit(gk1, gk1_rect)
			screen.blit(gk2, gk2_rect)
			pygame.display.update()
			if collected_gk2 == 1:
				collected_gk2 = 0
				time.sleep(1)
				running = False
			else :
				b_x, b_y, p1_x, p1_y, hit = move_p1(b_x, b_y, p1_x, p1_y, hit)
				gk2_x, gk2_y, b_x, b_y = move_gk2_pen(gk2_x, gk2_y, p2_x, p2_y, b_x, b_y)
				for event in pygame.event.get() :
					if event.type == pygame.KEYDOWN :
						if event.key == pygame.K_q :
							hit = 1
					if event.type == pygame.KEYUP :
						if event.key == pygame.K_q :
							hit = 0
				b_rect.center = b_x,b_y
				p2_rect.center = p2_x,p2_y
				p1_rect.center = p1_x,p1_y
				gk2_rect.center = gk2_x, gk2_y
				gk1_rect.center = gk1_x, gk1_y
				screen.blit(bg, (0,0))
				screen.blit(p1, p1_rect)
				screen.blit(b, b_rect)
				screen.blit(p2, p2_rect)
				screen.blit(gk1, gk1_rect)
				screen.blit(gk2, gk2_rect)
				pygame.display.update()
			if (b_x < 27) and  (b_y < 395 and b_y > 229):
				score = 1
				x = x + 1
				penaltygoal(x, y)
				running = False
				b_rect.center = b_x,b_y
				p2_rect.center = p2_x,p2_y
				p1_rect.center = p1_x,p1_y
				gk2_rect.center = gk2_x, gk2_y
				gk1_rect.center = gk1_x, gk1_y
				screen.blit(bg, (0,0))
				screen.blit(p1, p1_rect)
				screen.blit(b, b_rect)
				screen.blit(p2, p2_rect)
				screen.blit(gk1, gk1_rect)
				screen.blit(gk2, gk2_rect)
				pygame.display.update()
				time.sleep(1)
		gk1_x, gk1_y = 42, 307
		gk2_x, gk2_y = 46, 454
		p1_x, p1_y = 495, 304
		p2_x, p2_y = 181, 344
		b_x, b_y = 125, 304
		b_rect.center = b_x,b_y
		p2_rect.center = p2_x,p2_y
		p1_rect.center = p1_x,p1_y
		gk2_rect.center = gk2_x, gk2_y
		gk1_rect.center = gk1_x, gk1_y
		screen.blit(bg, (0,0))
		screen.blit(p1, p1_rect)
		screen.blit(b, b_rect)
		screen.blit(p2, p2_rect)
		screen.blit(gk1, gk1_rect)
		screen.blit(gk2, gk2_rect)
		pygame.display.update()
		time.sleep(2)
		running = True
		while running :
			clock.tick(30)
			b_rect.center = b_x,b_y
			p2_rect.center = p2_x,p2_y
			p1_rect.center = p1_x,p1_y
			gk2_rect.center = gk2_x, gk2_y
			gk1_rect.center = gk1_x, gk1_y
			screen.blit(bg, (0,0))
			screen.blit(p1, p1_rect)
			screen.blit(b, b_rect)
			screen.blit(p2, p2_rect)
			screen.blit(gk1, gk1_rect)
			screen.blit(gk2, gk2_rect)
			pygame.display.update()
			if collected_gk1 == 1:
				collected_gk1 = 0
				time.sleep(1)
				running = False
			else :
				b_x, b_y, p2_x, p2_y = move_p2_penalty(b_x, b_y, p2_x, p2_y)
				gk1_x, gk1_y, b_x, b_y = move_gk1(gk1_x, gk1_y, p2_x, p2_y, b_x, b_y)
				b_rect.center = b_x,b_y
				p2_rect.center = p2_x,p2_y
				p1_rect.center = p1_x,p1_y
				gk2_rect.center = gk2_x, gk2_y
				gk1_rect.center = gk1_x, gk1_y
				screen.blit(bg, (0,0))
				screen.blit(p1, p1_rect)
				screen.blit(b, b_rect)
				screen.blit(p2, p2_rect)
				screen.blit(gk1, gk1_rect)
				screen.blit(gk2, gk2_rect)
				pygame.display.update()
			if (b_x < 27) and  (b_y < 395 and b_y > 229):
				score = 1
				y = y + 1
				penaltygoal(x, y)
				running = False
				b_rect.center = b_x,b_y
				p2_rect.center = p2_x,p2_y
				p1_rect.center = p1_x,p1_y
				gk2_rect.center = gk2_x, gk2_y
				gk1_rect.center = gk1_x, gk1_y
				screen.blit(bg, (0,0))
				screen.blit(p1, p1_rect)
				screen.blit(b, b_rect)
				screen.blit(p2, p2_rect)
				screen.blit(gk1, gk1_rect)
				screen.blit(gk2, gk2_rect)
				pygame.display.update()
				time.sleep(1)
		count -= 1
	time.sleep(3)
	gameover1(x,y)

def football(score = 0,t = 0):
    screen.fill((0, 0, 0))
    pygame.mixer.music.load('crowd.wav')
    pygame.mixer.music.play(-1)
    global you_g, cpu_g, gk1, gk1_x, gk1_y, gk2, gk2_x, gk2_y, gk1_rect, gk2_rect
    global control, collected_gk1, collected_gk2, move_x, move_y, b_rect, p1_rect, p2_rect
    global img_1, kick, p1_x, p1_y, b_x, b_y, p2_x, p2_y, dim_x1, dim_x2, dim_y1, dim_y2, g2_x, g2_y
    running = True
    
    
    while running:
        clock.tick(30)
        screen.blit(bg, (0,0))
        screen.blit(p1, p1_rect)
        screen.blit(b, b_rect)
        screen.blit(p2, p2_rect)
        screen.blit(gk1, gk1_rect)
        screen.blit(gk2, gk2_rect)
        t = t + 1
        if score == 1:
        	time.sleep(1)
        	goal(score,you_g,cpu_g,t)
        scoreboard(t, you_g, cpu_g, p1_rect, p2_rect, b_rect)
        pygame.display.update()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_i :
                    move_y = -3
            if event.type == pygame.KEYUP :
                if event.key == pygame.K_i :
                    move_y = 0
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_k :	
                    move_y = 3
            if event.type == pygame.KEYUP :
                if event.key == pygame.K_k :	
                    move_y = 0
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_j :
                    move_x = -3
            if event.type == pygame.KEYUP :
                if event.key == pygame.K_j :
                    move_x = 0
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_l :	
                    move_x = 3
            if event.type == pygame.KEYUP :
                if event.key == pygame.K_l :	
                    move_x = 0
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_q :	
                    kick = 1
            if event.type == pygame.KEYUP :
                if event.key == pygame.K_q :	
                    kick = 0
                            
        if (p1_y <= dim_y1) and move_y == -3:
        	move_y = 0
        if (p1_x <= dim_x1) and move_x == -3:
        	move_x = 0
        if (p1_y >= dim_y2) and move_y == 3:
        	move_y = 0
        if (p1_x >= dim_x2) and move_x == 3:
        	move_x = 0
        	        	
        p1_x,p1_y = p1_x + move_x, p1_y + move_y
        d1 = math.hypot(p1_x - b_x, p1_y - b_y)
        d4 = math.hypot(p2_x - p1_x, p2_y - p1_y)

        if d1 < 26 and kick != 1 :
        	if move_x == -3:
        		b_x,b_y = b_x - 5, b_y
        		control = 1
        	if move_y == -3:
        		b_x,b_y = b_x + 10, b_y - 20
        		control = 1
        	if move_x == 3 and b_y < 310 and d4 <= 30:
        		b_x,b_y = b_x + 20, b_y + 10
        		control = 1
        	elif move_x == 3 and b_y > 310 and d4 <= 30:
        		b_x,b_y = b_x + 20, b_y - 10
        		control = 1
        	elif move_x == 3:
        		b_x, b_y = b_x + 20, b_y
        		control = 1
        	if move_y == 3:
        		b_x,b_y = b_x + 10, b_y + 20
        		control = 1
        if 	d1 < 45 :	
        	if kick == 1 and b_y <= 310:
        		b_x, b_y = b_x + 130, b_y + 100
        		control = 1
        	elif kick == 1 and b_y > 310 :
        		b_x, b_y = b_x + 130, b_y - 100
        		control = 1
        		
        d1 = math.hypot(p1_x - b_x, p1_y - b_y)
        d2 = math.hypot(p2_x - b_x, p2_y - b_y)
        if d1 < 26:
        	control = 1
        if d2 < 26:
        	control = 2
        if p2_x - p1_x < 100 and (p1_y - p2_y) < 20 and control == 1 and d1 < 40 and d2 < 40 and b_y < 310:
        	b_x, b_y = b_x + 40, b_y + 70
        elif p2_x - p1_x < 100 and (p1_y - p2_y) < 20 and control == 2 and d1 < 30 and d2 < 30 and b_y < 310:
        	b_x, b_y = b_x - 40, b_y + 70
        elif p2_x - p1_x < 100 and (p1_y - p2_y) < 20 and control == 1 and d1 < 40 and d2 < 40 and b_y >= 310:
        	b_x, b_y = b_x + 40, b_y - 70
        elif p2_x - p1_x < 100 and (p1_y - p2_y) < 20 and control == 2 and d1 < 30 and d2 < 30 and b_y >= 310:
        	b_x, b_y = b_x - 40, b_y - 70
        	
        p2_x, p2_y,b_x,b_y = move_p2(b_x, b_y, p2_x, p2_y, p1_x, p1_y)
        gk1_x, gk1_y, b_x, b_y = move_gk1(gk1_x, gk1_y, p2_x, p2_y, b_x, b_y)
        gk2_x, gk2_y, b_x, b_y= move_gk2(gk2_x, gk2_y, p1_x, p1_y, b_x, b_y)
        
        if collected_gk1 == 1 :
        	b_rect.center = b_x,b_y
        	p2_rect.center = p2_x,p2_y
        	p1_rect.center = p1_x,p1_y
        	gk2_rect.center = gk2_x, gk2_y
        	gk1_rect.center = gk1_x, gk1_y
        	screen.blit(bg, (0,0))
        	screen.blit(p1, p1_rect)
        	screen.blit(b, b_rect)
        	screen.blit(p2, p2_rect)
        	screen.blit(gk1, gk1_rect)
        	screen.blit(gk2, gk2_rect)
        	if t >= 2700:
        		gameover(you_g, cpu_g)
        	if score == 1:
        		time.sleep(1)
        		goal(score,you_g,cpu_g,t)
        	scoreboard(t, you_g, cpu_g, p1_rect, p2_rect, b_rect)
        	pygame.display.update()
        	b_x, b_y, p1_x, p1_y, p2_x, p2_y = gamereload1(b_x, b_y, p1_x, p1_y, p2_x, p2_y, p1_rect, p2_rect, b_rect)
        	collected_gk1 = 0
        	pygame.mixer.music.load('crowd.wav')
        	pygame.mixer.music.play(-1)
        	
        elif collected_gk2 == 1 :
        	b_rect.center = b_x,b_y
        	p2_rect.center = p2_x,p2_y
        	p1_rect.center = p1_x,p1_y
        	gk2_rect.center = gk2_x, gk2_y
        	gk1_rect.center = gk1_x, gk1_y
        	screen.blit(bg, (0,0))
        	screen.blit(p1, p1_rect)
        	screen.blit(b, b_rect)
        	screen.blit(p2, p2_rect)
        	screen.blit(gk1, gk1_rect)
        	screen.blit(gk2, gk2_rect)
        	if t >= 2700:
        		gameover(you_g, cpu_g)
        	if score == 1:
        		time.sleep(5)
        		goal(score,you_g,cpu_g,t)
        	scoreboard(t, you_g, cpu_g, p1_rect, p2_rect, b_rect)
        	pygame.display.update()
        	b_x, b_y, p1_x, p1_y, p2_x, p2_y = gamereload2(b_x, b_y, p1_x, p1_y, p2_x, p2_y)
        	collected_gk2 = 0
        	pygame.mixer.music.load('crowd.wav')
        	pygame.mixer.music.play(-1)
        	
        if(((b_x < 27 ) or (b_x > 975)) and  b_y < 395 and b_y > 229):
        	score = 1
        	if b_x < 27:
        		you_g += 1
        	if b_x > 975:
        		cpu_g += 1
        if (b_y <= dim_y1):
        	b_y = 12
        	flag_t = 1
        if (b_x <= dim_x1):
        	b_x = 27
        	flag_t = 1
        if (b_y >= dim_y2):
        	b_y = 595
        	flag_t = 1
        if (b_x >= dim_x2):
        	b_x = 966
        	flag_t = 1
        	
        b_rect.center = b_x,b_y
        p2_rect.center = p2_x,p2_y
        p1_rect.center = p1_x,p1_y
        gk2_rect.center = gk2_x, gk2_y
        gk1_rect.center = gk1_x, gk1_y


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] == 1 and action != None:
            if action == penaltyshoot:
            	screen.fill((0, 0, 0))
            action()
    smallText = pygame.font.Font("freesansbold.ttf",25)
    text = smallText.render(msg, True,(255,255,255))
    textRect = text.get_rect()
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(text, textRect)
    
    
def how_to_play():
	control = pygame.image.load('controls.jpeg')
	control_rect = control.get_rect()
	control_rect.center = 500, 250
	screen.blit(control, control_rect)
	pygame.display.update()
	time.sleep(5)
	screen.fill((0, 0, 0))
	screen.blit(back, back_rect)
	pygame.display.update()


def end():
     pygame.quit()
     sys.exit()


def start(play):
	t = 0
	pygame.mixer.music.load('ipl.wav')
	pygame.mixer.music.play(1)
	while play :
		clock.tick(15)
		for event in pygame.event.get():
			if event.type == pygame.QUIT :
				pygame.quit()
				quit()
		button("Play",460,480,100,40,white,white,football)
		button("Controls",460,520,100,40,white,white, how_to_play)
		button("Penalty Shoot",460,560,100,40,white, white, penaltyshoot)
		button("Quit",460,600,100,40,white,white, end)
		pygame.display.update()


start(True)
pygame.quit()
quit()
