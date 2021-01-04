import pyxel

WINDOW_H = 120
WINDOW_W = 200
PLANT_H = 22
PLANT_W = 20

class App:
	def __init__(self):
		self.IMG_ID0_X = 40
		self.IMG_ID0_Y = 30

		pyxel.init(WINDOW_W, WINDOW_H, caption="BmGeek")
		pyxel.image(0).load(0, 0, "plant.png")
		pyxel.run(self.update, self.draw)

	def update(self):
		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()

	def draw(self):
		pyxel.cls(0)
		self.plant()

	def plant(self):
		
		if pyxel.btn(pyxel.KEY_W):
			self.IMG_ID0_Y -= 1
		if pyxel.btn(pyxel.KEY_A):
			self.IMG_ID0_X -= 1
		if pyxel.btn(pyxel.KEY_S):
			self.IMG_ID0_Y += 1
		if pyxel.btn(pyxel.KEY_D):
			self.IMG_ID0_X += 1

		pyxel.blt(self.IMG_ID0_X, self.IMG_ID0_Y, 0, 0, 0, PLANT_W, PLANT_H)

App()