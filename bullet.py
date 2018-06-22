# 添加射击功能（添加子弹设置）：

# 首先要创建bullet类，且在settings中设置其属性：
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """对飞船发出的子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船所在的位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在（0,0）处绘制一个子弹对象:
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        # 放置子弹位置：
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 储存用小数表示子弹的位置(以便能够微调子弹的速度)：
        self.y = float(self.rect.y)

        # 设置别的属性：
        self.bullet_color = ai_settings.bullet_color
        self.bullet_speed = ai_settings.bullet_speed

    def update(self):
        """向上移动子弹，更新子弹的位置"""
        # 更新表示子弹位置的小数值：
        self.y -= self.bullet_speed
        # 更新表示子弹的rect的位置：
        self.rect.y = self.y

    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)












































