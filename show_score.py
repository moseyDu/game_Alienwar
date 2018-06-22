# 在屏幕上显示得分：
import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard():
    """设置一个显示得分信息的类"""

    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分的字体设置：
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备初始化图像：
        self.prep_score()
        self.prep_top_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """显示当前得分，将文本转化为图像"""
        # 首先将数字转化成字符串：
        # 设置得分的格式，显示为10的整数倍：
        rounded_score = int(round(self.stats.score, -1))
        # round()函数通常让小数精确到小数点后几位，如果第二个实参为负数，则圆整到最近的10、100等整数倍

        # 使用字符串格式设置指令，加入千位分隔符：
        score_str = "{:,}".format(rounded_score)

        self.score_image = self.font.render("score: " + score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将得分放在右上角：
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_top_score(self):
        """显示最高得分"""
        rounded_top_score = int(round(self.stats.top_score, -1))
        top_score_str = "{:,}".format(rounded_top_score)

        self.top_score_image = self.font.render("top_score: " + top_score_str, True, self.text_color, self.ai_settings.bg_color)

        self.top_score_rect = self.top_score_image.get_rect()
        self.top_score_rect.centerx = self.screen_rect.centerx
        self.top_score_rect.top = 20

    def prep_level(self):
        """显示游戏等级"""
        self.level_image = self.font.render("level: " + str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.top_score_rect.right + 100
        self.level_rect.top = self.score_rect.top

    def prep_ships(self):
        """显示剩余飞船编组"""
        self.ships = Group()

        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """在屏幕上显示得分,等级,剩余飞船数"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.top_score_image, self.top_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        self.ships.draw(self.screen)









































