class GameStats():
	"""跟踪游戏的统计信息"""
	def __init__(self, ai_settings):
		"""初始化统计信息"""

		self.ai_settings = ai_settings
		#游戏刚启动时处于活动状态
		self.game_active = True 
		self.reset_stats()

	def reset_stats(self):
		"""初始化游戏在运行期间可能变化的统计信息"""

		#飞船剩余可用数量
		self.ships_left = self.ai_settings.ship_limit
		