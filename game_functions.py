import sys
from time import sleep
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

def update_bullets(settings, screen, ship, aliens, bullets):
	bullets.update() # update bullets group position

	# delete bullets out of bounds to save resources
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	check_bullet_alien_collisions(settings, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(settings, screen, ship, aliens, bullets):
	# check if bullets hit aliens, if so delete both bullet and alien
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True) # first True=deleted collided bullet
	# second True = delete collided alien

	if len(aliens) == 0: # if all aliens are eliminated
		bullets.empty() # get rid of bullets and create a new fleet
		create_fleet(settings, screen, ship, aliens)

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

def check_fleet_edges(settings, aliens):
	"""check for the whole fleet to see if there is any alien out of edge"""
	for alien in aliens.sprites(): # makes it a list so that we can go through each element
		if alien.check_edges():
			change_fleet_direction(settings, aliens)
			break

def change_fleet_direction(settings, aliens):
	"""if we are here, it means the fleet need to go down and change horizontal direction"""
	for alien in aliens.sprites():
		alien.rect.y += settings.fleet_drop_speed
	settings.fleet_direction *= -1

def ship_hit(settings, stats, screen, ship, aliens, bullets):
	"""what will this game do when alien hits ship"""
	if stats.ships_left > 0:
		stats.ships_left -= 1
		aliens.empty()
		bullets.empty()
		# create a new fleet of aliens
		create_fleet(settings, screen, ship, aliens)
		ship.center_ship()

		sleep(0.5)
	else:
		stats.game_active = False # game over here

def check_aliens_bottom(settings, stats, screen, ship, aliens, bullets):
	"""check if any alien reach the bottom"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(settings, stats, screen, ship, aliens, bullets)
			break

def update_aliens(settings, stats, screen, ship, aliens, bullets):
	"""update this group of aliens"""
	check_fleet_edges(settings, aliens)
	aliens.update()

	# check if alien hit ship
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(settings, stats, screen, ship, aliens, bullets)

	check_aliens_bottom(settings, stats, screen, ship, aliens, bullets)
		


	
