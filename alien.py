# 创建外星人：
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_settings, screen):
        """初始化外星人并设置其他起始设置"""
        super(Alien, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        # 加载外星人图像，并设置其rect属性：
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 放置外星人位置（位于屏幕左上角附近）：
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 储存每个外星人的准确位置：
        self.x = float(self.rect.x)

    def check_edges(self):
        """判断外星人是否到达了屏幕边缘，如果是，返回True"""
        # 获取屏幕rect值：
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """更新外星人的位置(向左/右移动)"""
        # 我们用self.x来表示外星人的准确位置，再用它的值来更新外星人rect的位置(如果fleet_direction=1,则向右移动，如果为-1，则向左移动)
        self.x += self.ai_settings.alien_speed * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def draw_alien(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)






















































