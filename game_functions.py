import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, settings, screen, ship, bullets):
	"""as name indicated"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		# when space hit, create a new bullet and add it to the group
		fire_bullet(settings, screen, ship, bullets)

def check_keyup_events(event, ship):
	"""as name indicated"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(settings, screen, ship, bullets):
	# keeps monitoring keyboard and mouse input
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

def update_screen(settings, screen, ship, bullets):
	# it's always set to be filled with our background color and our ship
	screen.fill(settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	# display the latest screen
	pygame.display.flip()

def update_bullets(bullets):
	bullets.update() # update bullets group position

	# delete bullets out of bounds to save resources
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def fire_bullet(settings, screen, ship, bullets):
	if len(bullets) < settings.bullets_allowed:
		new_bullet = Bullet(settings, screen, ship)
		bullets.add(new_bullet)
