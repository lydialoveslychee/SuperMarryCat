import pygame
from pygame.locals import *
class Cat:
	def __init__(self, life, hp, path, screenWidth, screenHeight, screen, h):
		self.coin = 0
		self.life = life
		self.hp = hp
		self.h = h
		self.img = pygame.image.load(path).convert()
		self.imgX, self.imgY = self.img.get_size()
		self.screenWidth = screenWidth
		self.screenHeight = screenHeight
		self.x = 0
		self.y = screenHeight - self.imgY
		self.screen = screen;
		self.isJumping = False
		self.jumpingTime = 0
		print(self.imgX, self.imgY)


	def forward(self):
		if self.x < self.screenWidth - self.imgX:
			self.x += 1

	def backward(self):
		#cat move backward
		if self.x > 0:
			self.x -= 1

	def jump(self):
		#jump
		if self.isJumping:
			self.y -= -((self.h + self.screenHeight - self.imgY) / 50000) * self.jumpingTime + self.h / 50
			self.jumpingTime += 1
			if self.y >= self.screenHeight - self.imgY:
				self.y = self.screenHeight - self.imgY
				self.isJumping = False
				self.jumpingTime = 0
				return False #jumping stopped
			else:
				return True #still jumping
		else:
			self.isJumping = True
			self.jumpingTime += 1
			return self.jump()


	def hurt(self):
		#hurt
		self.hp -= 1

	def die(self):
		#die
		return --self.life

	def gainCoin(self, coin):
		#coin
		self.coin += coin
		
	def getPos(self):
		return self.x, self.y

	def setPos(self, x, y):
		self.x = x
		self.y = y

	def getHP(self):
		return self.hp

	def isAlive(self):
		return self.life > 0

	def getCoin(self):
		return self.coin

	def setJumpHeight(self, h):
		self.h = h

	def showCat(self):
		self.screen.blit(self.img, (self.x,self.y))