import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, settings, screen, ship, bullets):
	"""as name indicated"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		# when space hit, create a new bullet and add it to the group
		fire_bullet(settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()

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

def update_screen(settings, screen, ship, aliens, bullets):
	# it's always set to be filled with our background color and our ship
	screen.fill(settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen) # draw every single alien in aliens group
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

def get_number_aliens_x(settings, alien_width):
	"""calculate how many aliens are in one row"""
	avail_space_x = settings.screen_width - 2 * alien_width # leave both sides some space
	num_aliens_x = avail_space_x / (2 * alien_width)
	return int(num_aliens_x)

def get_number_rows(settings, ship_height, alien_height):
	avail_space_y = settings.screen_height - 3 * alien_height - ship_height
	number_rows = int (avail_space_y / (2 * alien_height))
	return number_rows

def create_alien(settings, screen, aliens, alien_num, row_number):
	"""create one alien and put it in the current row"""
	new_alien = Alien(settings, screen)
	alien_width = new_alien.rect.width
	new_alien.x = alien_width + 2 * alien_width * alien_num # starting from the very first one
	new_alien.rect.x = new_alien.x
	new_alien.rect.y = new_alien.rect.height + 2 * new_alien.rect.height * row_number
	aliens.add(new_alien)
	

def create_fleet(settings, screen, ship, aliens):
	"""creates a group of aliens"""
	# one alien first so we know how many we can have in one row
	alien = Alien(settings, screen)
	alien_width = alien.rect.width # the width of one alien, we want this to be space between them
	alien_height = alien.rect.height
	ship_height = ship.rect.height
	alien_number = get_number_aliens_x(settings, alien_width)
	number_rows = get_number_rows(settings, ship_height, alien_height)
	
	# now we can have a group of aliens
	for row_number in range(number_rows):
		for alien_num in range(alien_number):
			create_alien(settings, screen, aliens, alien_num, row_number)
		
		
		

	
