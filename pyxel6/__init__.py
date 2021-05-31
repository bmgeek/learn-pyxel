import pyxel
import random
import time

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

class Cat:
	def __init__(self, img_id):
		self.pos = Position(0, 0)
		self.img_plant = img_id
		self.size_x = 8
		self.size_y = 6
		self.speed_x = 1
		self.speed_y = 1
		self.get_image_left = Imageposition(0, 10)
		self.get_image_right = Imageposition(8, 10)
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

		### main character
		self.plant = Plant(self.IMG_ID0)
		self.plant.pos.x = 0
		self.plant.pos.y = 0

		self.Cats = []
		self.Balls = []

		pyxel.run(self.update, self.draw)

	def update(self):
		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()

		if self.plant.pos.y > 0 and pyxel.btn(pyxel.KEY_W):
			self.plant.update(self.plant.pos.x, self.plant.pos.y-2)
		if self.plant.pos.x > 0 and pyxel.btn(pyxel.KEY_A):
			self.plant.update(self.plant.pos.x-2, self.plant.pos.y)
			self.plant.get_image = self.plant.get_image_left
		if self.plant.pos.y+self.plant.size_y < self.WINDOW_H and pyxel.btn(pyxel.KEY_S):
			self.plant.update(self.plant.pos.x, self.plant.pos.y+2)
		if self.plant.pos.x+1+self.plant.size_x < self.WINDOW_W and pyxel.btn(pyxel.KEY_D):
			self.plant.update(self.plant.pos.x+2, self.plant.pos.y)
			self.plant.get_image = self.plant.get_image_right

		ball_count = len(self.Balls)
		cats_count = len(self.Cats)

		### SHOOT
		if pyxel.btnp(pyxel.KEY_SPACE) and ball_count < 5:
			new_ball = Ball()
			start_pos_x = round(self.plant.size_x/2) + 6
			if self.plant.get_image == self.plant.get_image_left:
				new_ball.speed = -new_ball.speed
				start_pos_x = round(self.plant.size_x/2) - 6
			new_ball.update(
				self.plant.pos.x + start_pos_x,
				self.plant.pos.y + self.plant.size_y/2
			)
			self.Balls.append(new_ball)

		for i in range(ball_count):
			if self.Balls[i].pos.x > 0 and self.Balls[i].pos.x < self.WINDOW_W:
				self.Balls[i].update(
					self.Balls[i].pos.x + self.Balls[i].speed,
					self.Balls[i].pos.y
				)
				try:
					if self.kill_cat(i):
						break
				except:
					pass
			else:
				del self.Balls[i]
				break
		### END SHOOT

		### CATS
		if cats_count < 5:
			new_cat = Cat(self.IMG_ID0)
			pos_x = random.choice(range(0, self.WINDOW_W - new_cat.size_x))
			pos_y = random.choice(range(0, self.WINDOW_H - new_cat.size_y))
			if pos_x > self.WINDOW_W / 2:
				new_cat.get_image = new_cat.get_image_left
			new_cat.pos.x = pos_x
			new_cat.pos.y = pos_y
			self.Cats.append(new_cat)

	def kill_cat(self, ball_index):
		for cat in range(len(self.Cats)):
			if (self.Balls[ball_index].pos.x in range(int(self.Cats[cat].pos.x), int(self.Cats[cat].pos.x) + self.Cats[cat].size_x)
			and self.Balls[ball_index].pos.y in range(int(self.Cats[cat].pos.y), int(self.Cats[cat].pos.y) + self.Cats[cat].size_y+1)):
				del self.Balls[ball_index]
				del self.Cats[cat]
				return True
		return False

	def draw(self):
		pyxel.cls(0)
		pyxel.blt(
			self.plant.pos.x,
			self.plant.pos.y,
			self.plant.img_plant,
			self.plant.get_image.pos.x,
			self.plant.get_image.pos.y,
			self.plant.size_x,
			self.plant.size_y,
			self.plant.color_tr
		)

		for cat in self.Cats:
			pyxel.blt(
				cat.pos.x,
				cat.pos.y,
				cat.img_plant,
				cat.get_image.pos.x,
				cat.get_image.pos.y,
				cat.size_x,
				cat.size_y,
				cat.color_tr
			)
		for ball in self.Balls:
			pyxel.circ(
				ball.pos.x,
				ball.pos.y,
				ball.size,
				ball.color
			)

App()