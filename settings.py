
# 为了避免在代码中到处添加不同的设置，我们把这些设置储存在一个地方：

# 我们编写一个settings类：
# class Settings():
#     """储存外星人游戏的所有设置的类"""
#
#     def __init__(self):
#         """总设置的初始化"""
#         self.screen_width = 1200
#         self.screen_height = 800
#         self.bg_color = (230, 230, 230)
#
#
#         # 调整飞船的速度(目前飞船默认一次移动一像素,我们可把默认值设为1.5)：
#         self.ship_speed = 3
#         # 因为rect的centerx属性只能储存整数值，所以我们需要对Ship类做些修改
#         # 限定的飞船的数量：
#         self.ship_limit = 3
#
#         # 子弹属性设置：
#         self.bullet_speed = 3
#         self.bullet_width = 3
#         self.bullet_height = 15
#         self.bullet_color = (60, 60, 60)
#         # 设置在屏幕上允许的最大子弹数(限制子弹的数量)：
#         self.bullet_allowed = 50
#
#
#         # 外星人属性设置：
#         self.alien_speed = 1
#         # 外星人撞到右边缘后向下移动的速度：
#         self.down_speed = 10
#         # 设置方向系数，1表示向右移，-1表示向左移(便于后面加减坐标)：
#         self.fleet_direction = 1


# 为提高游戏难度等级，加快游戏节奏，需要修改settings，将游戏设置划分为静态和动态的两组

class Settings():
    """储存外星人游戏所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置："""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 设置飞船的数量：
        self.ship_limit = 3

        # 子弹属性设置：
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 50

        # 外星人属性设置：
        self.down_speed = 10

        # 设置速度变化系数（以什么样的速度加快节奏）：
        self.speedup_scale = 1.2

        # 设置外星人分数提高速度：
        self.score_scale = 1.5

        # 随着游戏进行而变化的值，在游戏开始时也要被重置：
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而改变的设置"""

        # 飞船的速度：
        self.ship_speed = 3

        # 子弹的速度：
        self.bullet_speed = 3

        # 外星人的速度：
        self.alien_speed = 1

        # 方向系数：
        self.fleet_direction = 1

        # 消灭每个外星人得分(随着游戏进行，每个外星人得分会增高)：
        self.alien_point = 50

    def increase_speed(self):
        """随着游戏进行，速度提高，外星人分数提高"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_point = int(self.alien_point * self.score_scale)





























