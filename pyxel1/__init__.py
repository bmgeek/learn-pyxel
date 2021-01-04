import pyxel

WINDOW_H = 200
WINDOW_W = 250
PLANT_H = 22
# PLANT_W = 20

class App:
	def __init__(self):
		self.IMG_ID0_X = 40
		self.IMG_ID0_Y = 30

		self.PLANT_W = 20

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
			self.IMG_ID0_Y -= 5
		if pyxel.btn(pyxel.KEY_A):
			self.IMG_ID0_X -= 5
			self.PLANT_W = -20
		if pyxel.btn(pyxel.KEY_S):
			self.IMG_ID0_Y += 5
		if pyxel.btn(pyxel.KEY_D):
			self.IMG_ID0_X += 5
			self.PLANT_W = 20
		
		pyxel.blt(self.IMG_ID0_X, self.IMG_ID0_Y, 0, 0, 0, self.PLANT_W, PLANT_H)

App()