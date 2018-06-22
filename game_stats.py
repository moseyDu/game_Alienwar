# 跟踪游戏统计信息


class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # # 游戏刚启动时处于活跃状态：
        # self.game_active = True

        # 添加play按钮，点击开始游戏，所以让游戏一开始处于非活跃状态：
        self.game_active = False

        # 记录玩家的最高得分（任何情况都不应该重置最高得分）：
        self.top_score = 0

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0

        # 设置游戏等级：
        self.level = 1





































