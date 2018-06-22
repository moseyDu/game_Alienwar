
# 创建ship模块，负责管理飞船的大部分行为：
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """处理飞船的类"""
    # 初始化飞船并设置其初始位置：
    def __init__(self, ai_settings, screen):
        # 为了显示剩余飞船数，需要创建一个飞船编组：
        super(Ship, self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像：
        self.image = pygame.image.load('images/ship.bmp')
        # 获取飞船和屏幕的外接矩形：
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将飞船放到屏幕底部正中央：
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中储存小数值：
        self.center = float(self.rect.centerx)

        # 设置一个移动标志(默认为False)：
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值而不是rect值：
        # 限制飞船的移动范围(飞船将在到达屏幕边缘时停止移动)：
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed
        # 此处应使用if，如果使用elif的话，同时按下左右箭头，飞船将一直向右移动，使用if，同时按下左右箭头时，飞船将停止不动：
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed

        # 根据self.center更新rect对象(self.ship_rect.centerx将只存储self.center的整数部分)：
        self.rect.centerx = self.center

    def draw_ship(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """将飞船居中"""
        self.center = self.screen_rect.centerx
























