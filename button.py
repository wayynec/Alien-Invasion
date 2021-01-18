import pygame.font

class Button():
	"""this is a class for button"""
	def __init__(self, settings, screen, msg):
		"""initialize all button settings"""
		self.screen = screen
		self.screen_rect = self.screen.get_rect()

		# size and color of this button
		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		# create the rect for thsi button, and centralize it
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		# prepare the message
		self.prep_msg(msg)

	def prep_msg(self, msg):
		"""render text to image and place it at the center of the button"""
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)