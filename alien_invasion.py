import pygame
import game_functions as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group

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


	#开始游戏的主循环
	while True:
		
		#监视键盘和鼠标事件
		gf.check_events(ai_settings, screen, ship, bullets)
		#更新飞船的位置
		ship.update()
		#更新子弹的位置
		gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
		#更新外星人群中所有外星人的位置
		gf.update_aliens(ai_settings ,aliens)
		#重绘屏幕
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()