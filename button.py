# 创建按钮：
import pygame.font

class Button():

    def __init__(self, ai_settings, screen, msg):
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的属性：
        self.width, self.height = 200, 50
        self.button_color = (255, 0, 255)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # None表示使用默认字体

        # 创建按钮的rect对象，并使其居中：
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮的标签只需创建一次：
        self.prep_msg(msg)
        # msg主要是在按钮上显示的文本



    # pygame通过将要显示的字符串渲染为图像来显示文本:
    def prep_msg(self, msg):
        """将msg渲染为图像，并使其在按钮上居中"""

        # font.render()方法将储存在msg中的文本转化为图像，接受参数为(要渲染的文本，布尔参数（指定是否开启反锯齿功能），文本颜色，背景色)
        # 如果没有背景色，将以透明背景的方式渲染文本
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)

        # 让图像在按钮居中：
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        """将按钮显示在屏幕上"""
        # 绘制一个用颜色显示的按钮：
        self.screen.fill(self.button_color, self.rect)
        # 绘制文本：
        self.screen.blit(self.msg_image, self.msg_image_rect)
















































