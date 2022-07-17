


from pic import *
time_start = time.time() 
pygame.init()

none = 'none'
class CLS_photoship(object):
	def __init__(self):
		pygame.init()
		self.scr = pygame.display.set_mode((SCREEN_W, SCREEN_H))
		pygame.display.set_caption('RT Photoship')
		self.clock = pygame.time.Clock()
		self.font = pygame.font.Font('clash.ttf', 32)
		self.spd = 5
		self.mousePos = (0,0)
		self.guideList = []
		self.guideId = 0
	def play(self):
		for guide in self.guideList:
			guide.draw(self.scr)
		pygame.display.update()
		self.clock.tick(50)
		return
	def add_guide(self,guide):
		guide.id = len(self.guideList)
		self.guideList.append(guide)
		return
	def key_up(self, key):
		return
	def key_down(self, key):
		return
	def mouse_down(self, pos, btn):
		self.guideList[self.guideId].mouse_down(pos, btn)
		return
	def mouse_up(self, pos, btn):
		self.guideList[self.guideId].mouse_up(pos, btn)
		return
	def mouse_motion(self, pos):
		self.mousePos = pos
		self.guideList[self.guideId].mouse_motion(pos)
		return
class CLS_guide(object):
	def __init__(self,picName):
		self.pic = CLS_pic(picName)
		self.id = 0
		self.btnList = []
		self.txtList = []
		self.secretList = []
	def draw(self, scr):
		if pship.guideId != self.id:
			return
		scr.blit(self.pic.img, (0, 0))
		for btn in self.btnList:
			btn.draw(scr)
		for txt in self.txtList:
			txt.draw(scr)
		return
	def add_button(self, name, picFile, x, y, guideId, music):
		b = CLS_button( name, picFile, x, y, guideId, music)
		self.btnList.append( b )
		return
	def add_txt(self, txt, font, x, y, c, rect):
		t = CLS_txt( txt, font, x, y, c, rect )
		self.txtList.append( t )
	def add_secret(self, rect, guideId, music):
		secret = CLS_secret(rect, guideId, music)
		self.secretList.append(secret)
	def mouse_down(self, pos, button):
		for btn in self.btnList:
			btn.mouse_down( pos, button )
		for secret in self.secretList:
			secret.mouse_down( pos, button )
		return
	def mouse_up( self, pos, button ):
		for btn in self.btnList:
			btn.mouse_up( pos, button )
		return
	def mouse_motion( self, pos ):
		return
class CLS_button(object):
	def __init__(self, name, picFile, x, y, guideId, music):
		self.name = name
		self.img = pygame.image.load(picFile)
		self.img.set_colorkey( (38,38,38) )
		self.w, self.h = self.img.get_width()//2, self.img.get_height()
		self.x, self.y = x, y
		self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
		self.status = 0
		self.guideId = guideId
		if music == 'none':
			pass
		else:
			self.music = pygame.mixer.Sound(music)
	def draw(self,scr):
		scr.blit(self.img, (self.x, self.y),
			(self.status * self.rect.w, 0, self.rect.w, self.rect.h))
		return
	def mouse_down(self,pos,button):
		if self.rect.collidepoint(pos):
			self.status = 1
		return
	def mouse_up(self,pos,button):
		self.status = 0
		if not self.rect.collidepoint(pos):
			return
		if self.name == 'U':
			pship.guideList[self.guideId].pic.draw(pship.scr, 5, pship.spd)
		elif self.name == 'D':
			pship.guideList[self.guideId].pic.draw(pship.scr, 6, pship.spd)
			sound = pygame.mixer.Sound('die.mp3')
			sound.play()
		elif self.name == 'L':
			pship.guideList[self.guideId].pic.draw(pship.scr, 3, pship.spd)
		elif self.name == 'R':
			pship.guideList[self.guideId].pic.draw(pship.scr, 4, pship.spd)
		elif self.name == 'Return1':
			pship.guideList[self.guideId].pic.draw(pship.scr, 6, pship.spd)
			self.music.play()
		elif self.name == 'Return2':
			pship.guideList[self.guideId].pic.draw(pship.scr, 6, pship.spd)
			self.music.play()
		elif self.name == 'Return3':
			pship.guideList[self.guideId].pic.draw(pship.scr, 6, pship.spd)
			self.music.play()
		elif self.name == 'Return4':
			pship.guideList[self.guideId].pic.draw(pship.scr, 6, pship.spd)
			self.music.play()
		elif self.name == 'R1':
			pship.guideList[self.guideId].pic.draw(pship.scr, 4, pship.spd)
			self.music.play()
		elif self.name == 'Return5':
			pship.guideList[self.guideId].pic.draw(pship.scr, 6, pship.spd)
			self.music.play()
		pship.guideId = self.guideId
		return
class CLS_txt(object):
	def __init__(self, txt, font, x, y, c, rect):
		self.txt = txt
		self.img = font.render(txt, True, c)
		self.x, self.y = x, y
		self.c = c
		self.rect = pygame.Rect(rect)
	def draw(self, scr):
		if self.rect.collidepoint(pship.mousePos):
			scr.blit(self.img, (self.x, self.y))
		return
class CLS_secret(object):
	def __init__(self, rect, guideId, music):
		self.rect = pygame.Rect(rect)
		self.guideId = guideId
		self.music = pygame.mixer.Sound(music)
	def mouse_down(self,pos,secret):
		if self.rect.collidepoint(pos):
			pship.guideList[self.guideId].pic.draw(pship.scr, 5, pship.spd)
			pship.guideId = self.guideId
			self.music.play()
		return
#--main

pship = CLS_photoship()
G01 = CLS_guide('difficulty.png')
pship.guideId = G01.id
pship.add_guide(G01)
G02 = CLS_guide('pship1.png')
pship.guideId = G02.id
pship.add_guide(G02)
G03 = CLS_guide('pship2.png')
pship.guideId = G03.id
pship.add_guide(G03)
G04 = CLS_guide('failure.png')
pship.guideId = G04.id
pship.add_guide(G04)
G05 = CLS_guide('pship3.png')
pship.guideId = G05.id
pship.add_guide(G05)
G06 = CLS_guide('pship4.png')
pship.guideId = G06.id
pship.add_guide(G06)
G07 = CLS_guide('pshipsotheymadethis.png')
pship.guideId = G07.id 
pship.add_guide(G07)
G08 = CLS_guide('pship5.png')
pship.guideId = G08.id
pship.add_guide(G08)
G09 = CLS_guide('pship6.png')
pship.guideId = G09.id
pship.add_guide(G09)
G010 = CLS_guide('poison.png')
pship.guideId = G010.id
pship.add_guide(G010)
G011 = CLS_guide('l2.png')
pship.guideId = G011.id
pship.add_guide(G011)
G012 = CLS_guide('block.png')
pship.guideId = G012.id
pship.add_guide(G012)
G013 = CLS_guide('pship7.png')
pship.guideId = G013.id
pship.add_guide(G013)
G014 = CLS_guide('blockthesun.png')
pship.guideId = G014.id
pship.add_guide(G014)
G015 = CLS_guide('boss.png')
pship.guideId = G015.id
pship.add_guide(G015)
G016 = CLS_guide('action.png')
pship.guideId = G016.id
pship.add_guide(G016)
G017 = CLS_guide('fat.png')
pship.guideId = G017.id
pship.add_guide(G017)
G018 = CLS_guide('emdmg.png')
pship.guideId = G018.id
pship.add_guide(G018)
G019 = CLS_guide('dmg.png')
pship.guideId = G019.id
pship.add_guide(G019)

G02.add_button('U', 'bUp.bmp', 117, 550, G03.id, none)
G02.add_button('D', 'bDown.bmp', 117, 550 + 100, G04.id, none)
G02.add_button('L', 'bLeft.bmp', 70, 550 + 50, G03.id, none)
G02.add_button('R', 'bRight.bmp', 164, 550 + 50, G03.id, none)
G03.add_button('D','bDown.bmp', SCREEN_W//2 - 35, SCREEN_H - 100, G04.id, none)
G04.add_button('L','bReturn.bmp', SCREEN_W//2 - 35, SCREEN_H - 100, G01.id, none)
G05.add_button('Return1', 'bReturn.bmp', SCREEN_W//2 - 35, SCREEN_H - 100, G06.id, 'branch.mp3')
G06.add_button('Return2', 'bReturn.bmp', SCREEN_W//2 - 35, SCREEN_H - 100, G07.id, 'sotheymadethis.mp3')
G07.add_button('R1', 'bRight.bmp', SCREEN_W//2 - 35, SCREEN_H - 100, G08.id, 'emo.mp3')
G08.add_button('D', 'bDown.bmp', SCREEN_W//2 - 35, SCREEN_H - 100, G04.id, none)
G09.add_button('Return3', 'bReturn.bmp', SCREEN_W//2 - 35, SCREEN_H - 100, G010.id, 'leaf.mp3')
G010.add_button('Return4', 'bReturn.bmp', SCREEN_W//2 - 35, SCREEN_H - 100, G011.id, 'l2.mp3')
G011.add_button('Return4', 'bReturn.bmp', SCREEN_W//2 - 35, SCREEN_H - 100, G012.id, 'emo.mp3')
G012.add_button('R1', 'bRight.bmp', SCREEN_W//2 - 35, SCREEN_H - 100, G013.id, 'die.mp3')
G013.add_button('R1', 'bRight.bmp', SCREEN_W//2 - 35, SCREEN_H - 100, G014.id, 'blockthesun.mp3')
G014.add_button('R1', 'bRight.bmp', SCREEN_W//2 - 35, SCREEN_H - 100, G015.id, 'emo.mp3')
G015.add_button('R1', 'bRight.bmp', SCREEN_W//2 - 35, SCREEN_H - 100, G016.id, 'action.mp3')
G016.add_button('R1', 'bRight.bmp', SCREEN_W//2 - 35, SCREEN_H - 100, G017.id, 'fat.mp3')
G017.add_button('R1', 'bRight.bmp', SCREEN_W//2 - 35, SCREEN_H - 100, G018.id, 'die.mp3')
G018.add_button('Return5', 'bReturn.bmp', SCREEN_W//2 - 35, SCREEN_H - 100, G019.id, 'dmg.mp3')
# G01.add_txt('我帅吗？', pship.font, 371, 384,(0, 255, 0), (429,451,23,16))
G01.add_secret((145,590,759,84), G02.id, 'emo.mp3')
G01.add_secret((145,249,759,322), G04.id, 'die.mp3')
G03.add_secret((373,240,151,178), G05.id, 'die.mp3')
G08.add_secret((552,0,70,64), G09.id, 'die.mp3')

while True: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			time_end = time.time() 
			time_c= time_end - time_start 
			f = open('score.myshellyyds', 'w')
			f.write(str(time_c))
			f.close
			print('time cost', time_c, 's')
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYUP:
			pship.key_up(event.key)
		if event.type == pygame.KEYDOWN:
			pship.key_down(event.key)
		if event.type == pygame.MOUSEBUTTONDOWN:
			pship.mouse_down(event.pos, event.button)
			print(pship.mousePos)
		if event.type == pygame.MOUSEBUTTONUP:
			pship.mouse_up(event.pos, event.button)
		if event.type == pygame.MOUSEMOTION:
			pship.mouse_motion(event.pos)
	pship.play()