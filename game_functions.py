import sys
import pygame

def check_events(ship):
	#监视键盘和鼠标事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN: #监听键盘按下
				if event.key == pygame.K_RIGHT: 
					#允许飞船向右移动
					ship.moving_right = True
				elif event.key == pygame.K_LEFT: 
					#允许飞船向左移动
					ship.moving_left = True
			elif event.type == pygame.KEYUP:  #监听键盘松开
				if event.key == pygame.K_RIGHT: 
					#禁止飞船向右移动
					ship.moving_right = False
				elif event.key == pygame.K_LEFT: 
					#禁止飞船向左移动
					ship.moving_left = False





def update_screen(ai_settings, screen, ship):
	"""更新屏幕上的图像，并切换到新屏幕"""

	#每次循环的时候都重汇屏幕
	screen.fill(ai_settings.bg_color)
	ship.blitme()

	#让最近绘制的屏幕可见
	pygame.display.flip()