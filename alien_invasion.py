import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
	# initialize the game and create a screen object
	pygame.init()
	game_settings = Settings()
	screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
	pygame.display.set_caption("Alien Invasion Game")

	# create a start button
	button = Button(game_settings, screen, "Play")
	# create game stats 
	stats = GameStats(game_settings)
	sb = Scoreboard(game_settings, screen, stats)
	# create our ship on background
	ship = Ship(game_settings, screen)
	# create a group for all bullets (inherited form Sprite superclass)
	bullets = Group()
	# create a group for aliens
	aliens = Group()

	# create a group of aliens before game starts
	gf.create_fleet(game_settings, screen, ship, aliens)

	# main loop for the game
	while True:
		gf.check_events(game_settings, screen, stats, sb, button, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(game_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(game_settings, stats, screen, sb, ship, aliens, bullets)
		gf.update_screen(game_settings, screen, stats, sb, ship, aliens, bullets, button)
		

run_game()