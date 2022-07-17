


import pygame, sys, random

SCREEN_W, SCREEN_H = 1065, 588

class CLS_pic(object):
	def __init__(self, fileName):
		img = pygame.image.load(fileName)
		self.img = pygame.transform.scale(img, \
			(SCREEN_W, SCREEN_H))
		self.x, self.y = 0, 0
		self.w, self.h = self.img.get_size()
	def draw(self, scr, effNum = 0, spd = 5):
		if spd == 0:
			spd = SCREEN_W
		if effNum == 1:
			for x in range( -SCREEN_W, 0, spd ):
				scr.blit( self.img, ( x, 0) )
				pygame.display.update()
		elif effNum == 2:
			for x in range( 0 , SCREEN_W, spd ):
				scr.blit( self.img, ( x, 0 ), (x, 0, spd, self.h))
				pygame.display.update()
		elif effNum == 3:
			oldImg = scr.copy()
			for x in range( -SCREEN_W, 0, spd ):
				scr.blit( self.img, ( x, 0 ) )
				scr.blit( oldImg, (x + SCREEN_W, 0) )
				pygame.display.update()
		elif effNum == 4:
			oldImg = scr.copy()
			for x in range( SCREEN_W, 0, -spd ):
				scr.blit(self.img, (x, 0))
				scr.blit( oldImg, (x - SCREEN_W, 0) )
				pygame.display.update()
		elif effNum == 5:
			for w in range(1, SCREEN_W, spd ):
				h = int(w * SCREEN_H / SCREEN_W)
				img = pygame.transform.scale(self.img, (w, h))
				scr.blit( img, ((SCREEN_W - w)//2, (SCREEN_H - h)//2))
				pygame.display.update()
		elif effNum == 6:
			oldImg = scr.copy()
			for w in range(SCREEN_W, 0, -spd ):
				h = int(w * SCREEN_H / SCREEN_W)
				img = pygame.transform.scale( oldImg, (w, h))
				scr.blit( img, ((SCREEN_W - w)//2, (SCREEN_H - h)//2))
				pygame.display.update()

		scr.blit(self.img, (self.x, self.y), (0, 0, self.w, self.h))
		pygame.draw.rect(scr, (0,255,0), (0, 0, spd*8, 8), 0)
	def filter(self, scr, filterNum):
		if filterNum == 1:
			for y in range(self.h):
				for x in range(self.w):
					r0, g0, b0, alpha = self.img.get_at( (x, y) )
					gray = int(0.3*r0 + 0.59*g0 + 0.11*b0)
					c = (gray, gray, gray)
					scr.set_at( (x, y), c )
				pygame.display.update()
		elif filterNum == 2:
			img0 = pygame.transform.scale(self.img, (SCREEN_W, SCREEN_W))
			img1 = pygame.Surface( (SCREEN_W, SCREEN_W) )
			n = self.w
			a = int(self.w / 2)
			for y in range(a):
				for x in range(y, a):
					img1.set_at( (x,y), img0.get_at( (x, y) ) )
					img1.set_at( (y,x), img0.get_at( (x, y) ) )
					img1.set_at( (n-1-x,y), img0.get_at( (x, y) ) )
					img1.set_at( (n-1-y,x), img0.get_at( (x, y) ) )
			for y in range(a - 1):
				for x in range(n):
					img1.set_at( (x, n-1-y), img1.get_at( (x, y) ) )
			scr = pygame.transform.scale(img1, (SCREEN_W, SCREEN_H))
		elif filterNum == 3:
			for y in range(self.h):
				for x in range(self.w):
					r0, g0, b0, alpha = self.img.get_at( (x, y) )
					c = (255 - r0, 255 - g0, 255 - b0)
					scr.set_at( (x, y), c )
				pygame.display.update()
		elif filterNum == 4:
			for y in range(self.h):
				for x in range(self.w):
					r0, g0, b0, alpha = self.img.get_at( (x, y) )
					gray = int(0.3*r0 + 0.59*g0 + 0.11*b0)
					c = (gray//128*128,gray//128*128,gray//128*128)
					scr.set_at( (x, y), c )
				pygame.display.update()
		elif filterNum == 5:
			n = 5
			grid = [[0] * n] * n
			for y in range(n // 2, self.h - n // 2):
				for x in range(n // 2, self.w - n // 2):
					self.get_pixel_grid(x, y, n, grid)
					x1 = random.randint(0, n - 1)
					y1 = random.randint(0, n - 1)
					scr.set_at( (x, y), grid[y1][x1] )
				pygame.display.update()
		elif filterNum == 6:
			n = 5
			grid = [[0] * n] * n
			for y in range(n // 2, self.h - n // 2):
				for x in range(n // 2, self.w - n // 2):
					self.get_pixel_grid(x, y, n, grid)
					x1 = random.randint(0, n - 1)
					y1 = random.randint(0, n - 1)
					c1 = grid[y1][x1]
					gray = (c1[0] + c1[1] + c1[2])//3//32*32
					c = (gray, gray, gray)
					scr.set_at( (x, y), c )
				pygame.display.update()
		elif filterNum == 7:
			d = 128
			n = 5
			grid = [[0] * n] * n
			for y in range(n // 2, self.h - n // 2):
				for x in range(n // 2, self.w - n // 2):
					self.get_pixel_grid(x, y, n, grid)
					c0 = self.img.get_at( (x,y) )
					c1 = grid[0][0]
					r = (c1[0] - c0[0]) + d
					if r > 255:
						r = 255
					if r < 0:
						r = 0
					g = (c1[1] - c0[1]) + d
					if g > 255:
						g = 255
					if g < 0:
						g = 0
					b = (c1[2] - c0[2]) + d
					if b > 255:
						b = 255
					if b < 0:
						b = 0
					gray = max(r,g,b)
					c = (gray, gray, gray)
					scr.set_at( (x, y), c )
				pygame.display.update()
		self.img = scr.copy()
	def get_pixel_grid(self, x0, y0, sideLen, pixelGrid):
		n = sideLen // 2
		for y in range(-n, n + 1):
			for x in range(-n, n + 1):
				pixelGrid[y + n][x + n] = self.img.get_at((x + x0, y + y0))


class CLS_photoship(object):
	def __init__(self):
		pygame.init()
		self.scr = pygame.display.set_mode((SCREEN_W, SCREEN_H))
		self.clock = pygame.time.Clock()
		self.font = pygame.font.Font('clash.ttf', 32)
		self.picList = []
		self.load_pic()
		self.picCurNum = 0
		self.spd = 5
		self.effNum = 0
	def load_pic(self):
		fList = ['difficulty.png', 'pship1.png', 'pship2.png', 'pship3.png',
		'pship4.png', 'pship5.png', 'failure.png', 'neighborkid.png']
		for fileName in fList:
			self.picList.append( CLS_pic(fileName) )
	def play(self):
		self.picList[self.picCurNum].draw(self.scr, spd = self.spd)
		pygame.display.update()
		self.clock.tick(50)
	def key_up(self, key):
		return
	def key_down(self, key):
		if event.key in (32, pygame.K_RIGHT):
			self.picCurNum = (self.picCurNum + 1) % len(self.picList)
			self.picList[self.picCurNum].draw(self.scr, self.effNum, self.spd)
		elif event.key == pygame.K_LEFT:
			self.picCurNum = (self.picCurNum - 1) % len(self.picList)
			self.picList[self.picCurNum].draw(self.scr, self.effNum, self.spd)
		elif event.key == pygame.K_UP:
			self.spd = (self.spd - 1) % 10
		elif event.key == pygame.K_DOWN:
			self.spd = (self.spd + 1) % 10
		elif ord('a') <= event.key <= ord('z'):
			self.effNum = event.key - ord('a') + 1
			self.picCurNum = (self.picCurNum + 1) % len(self.picList)
			self.picList[self.picCurNum].draw(self.scr, self.effNum, self.spd)
		elif ord('1') <= event.key <= ord('9'):
			self.picList[self.picCurNum].filter(self.scr, event.key - ord('0'))
		elif ord('0') == event.key:
			self.picList = []
			self.load_pic()
# -------main-------
pship = CLS_photoship()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYUP:
			pship.key_up(event.key)
		if event.type == pygame.KEYDOWN:
			pship.key_down(event.key)
	pship.play()