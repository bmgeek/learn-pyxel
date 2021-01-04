import pyxel


# https://github.com/kitao/pyxel/blob/master/pyxel/__init__.py

class Position:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Imageposition:
    def __init__(self, x, y):
        self.pos = Position(x, y)

class Ball:
	def __init__(self):
		self.pos = Position(0, 0)
		self.size = 2
		self.speed = 3
		self.color = 11

	def update(self, x, y):
		self.pos.x = x
		self.pos.y = y

class Plant:
	def __init__(self, img_id):
		self.pos = Position(0, 0)
		self.img_plant = img_id
		self.size_x = 5
		self.size_y = 8
		self.get_image_left = Imageposition(9, 0)
		self.get_image_right = Imageposition(2, 0)
		self.get_image = self.get_image_right
		self.color_tr = 0

	def update(self, x, y):
		self.pos.x = x
		self.pos.y = y

class App:
	def __init__(self):
		self.IMG_ID0 = 0
		self.WINDOW_H = 120
		self.WINDOW_W = 200

		pyxel.init(self.WINDOW_W, self.WINDOW_H, caption="BmGeek")
		pyxel.load("my_resource.pyxres")		

		self.plant = Plant(self.IMG_ID0)
		self.plant.pos.x = 0
		self.plant.pos.y = 0

		self.Balls = []

		pyxel.run(self.update, self.draw)

	def update(self):
		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()

		if self.plant.pos.y-10 > 0 and pyxel.btn(pyxel.KEY_W):
			self.plant.update(self.plant.pos.x, self.plant.pos.y-2)
		if self.plant.pos.x-10 > 0 and pyxel.btn(pyxel.KEY_A):
			self.plant.update(self.plant.pos.x-2, self.plant.pos.y)
			self.plant.get_image = self.plant.get_image_left
		if self.plant.pos.y+24 < self.WINDOW_H and pyxel.btn(pyxel.KEY_S):
			self.plant.update(self.plant.pos.x, self.plant.pos.y+2)
		if self.plant.pos.x+22 < self.WINDOW_W and pyxel.btn(pyxel.KEY_D):
			self.plant.update(self.plant.pos.x+2, self.plant.pos.y)
			self.plant.get_image = self.plant.get_image_right

		ball_count = len(self.Balls)

		if pyxel.btnp(pyxel.KEY_SPACE) and ball_count < 5:
			new_ball = Ball()
			new_ball.update(
				self.plant.pos.x + round(self.plant.size_x/2) + 6,
				self.plant.pos.y + self.plant.size_y/2
			)
			self.Balls.append(new_ball)

		for i in range(ball_count):
			if self.Balls[i].pos.x > 0 and self.Balls[i].pos.x < self.WINDOW_W:
				self.Balls[i].update(
					self.Balls[i].pos.x + self.Balls[i].speed,
					self.Balls[i].pos.y
				)
			else:
				del self.Balls[i]
				break

	def draw(self):
		pyxel.cls(0)
		pyxel.blt(self.plant.pos.x, self.plant.pos.y, self.plant.img_plant, self.plant.get_image.pos.x, self.plant.get_image.pos.y, self.plant.size_x, self.plant.size_y, self.plant.color_tr)

		for ball in self.Balls:
			pyxel.circ(ball.pos.x, ball.pos.y, ball.size, ball.color)
App()