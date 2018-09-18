class Cat:
	def __init__(life, hp, x, y, h):
		self.coin = 0;
		self.life = life;
		self.hp = hp;
		self.x = x;
		self.y = y;
		self.h = h;

	def getPos():
		return self.x, self.y;

	def setPos(x, y):
		self.x = x;
		self.y = y;

	def forward():
		self.x++;

	def backward():
		#cat move backward
		if self.x > 0:
			self.x--;

	def jump(t, y):
		#jump
		self.y += 20 * t - 200;
		if self.y >= y:
			return True
		else return False;

	def hurt():
		#hurt
		self.hp--;

	def die():
		#die
		return --self.life;

	def gainCoin(coin):
		#coin
		self.coin += coin;