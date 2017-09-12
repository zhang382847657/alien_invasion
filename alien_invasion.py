import pygame
import game_functions as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button

def run_game():

	#初始化pygame、设置和屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("外星人入侵")

	#创建一艘飞创
	ship = Ship(ai_settings, screen)
	#创建一个用于存储子弹的编组
	bullets = Group()
	#创建一个用于存储外星人的编组
	aliens = Group()
	#创建外星人群
	gf.create_fleet(ai_settings, screen, ship, aliens)
	#创建一个用于存储游戏统计信息的实例
	stats = GameStats(ai_settings)
	#创建Play按钮
	play_button = Button(ai_settings, screen, "Play")


	#开始游戏的主循环
	while True:
		
		#监视键盘和鼠标事件
		gf.check_events(ai_settings, screen, ship, bullets)

		#如果游戏处于活动状态
		if stats.game_active:
			#更新飞船的位置
			ship.update()
			#更新子弹的位置
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			#更新外星人群中所有外星人的位置
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

		
		#重绘屏幕
		gf.update_screen(ai_settings, screen, stats ,ship, aliens, bullets, play_button)

run_game()