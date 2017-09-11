class Settings():
	""" 存储《外星人入侵》的所有设置类 """

	def __init__(self):
		""" 初始化游戏的设置 """
		#屏幕设置
		self.screen_width = 1200  #屏幕宽度
		self.screen_height = 800  #屏幕高度
		self.bg_color = (230, 230, 230)  #屏幕背景色

		#飞船的设置
		self.ship_speed_factor = 10  #飞船的速度
		self.ship_limit = 3  #飞船可用的数量

		#子弹设置
		self.bullet_speed_factor = 20  #子弹的速度
		self.bullet_width = 30  #子弹的宽度
		self.bullet_height = 15  #子弹的高度
		self.bullet_color = (60, 60, 60)  #子弹的颜色
		self.bullets_allowed = 30  #允许发射的子弹数量

		#外星人设置
		self.alien_speed_factor = 5  #外星人移动速度
		self.fleet_drop_speed = 15 #外星人向下移动的速度
		self.fleet_direction = 1 #外星人移动的方向 1代表向右  -1代表向左

