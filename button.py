import pygame 

#classe do botao
class Button():
	def __init__(self, surface, x, y, image, size_x, size_y):
		self.image = pygame.transform.scale(image, (size_x, size_y))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
		self.surface = surface

	def draw(self):
		action = False

		#posicao do mouse
		pos = pygame.mouse.get_pos()

		#clicar
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#botao
		self.surface.blit(self.image, (self.rect.x, self.rect.y))

		return action