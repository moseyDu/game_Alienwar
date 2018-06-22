# 一、首先创建一个空窗口：

# import sys
# import pygame
#
# def run_game():
#     """初始化游戏并开始主循环"""
#     pygame.init()
#     # 创建一个窗口：
#     screen = pygame.display.set_mode((1200, 800))
#     # 设置窗口的名字：
#     pygame.display.set_caption('Alien_war')
#
#     # 设置窗口背景色：
#     bg_color = (230, 230, 230)
#
#     # 进入游戏主循环：
#     while True:
#
#         # 监视键盘和鼠标事件：
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#
#         # 每次循环时都重绘屏幕(用背景色填充屏幕)：
#         screen.fill(bg_color)
#         # 让最近绘制的屏幕可见：
#         pygame.display.flip()
#
# run_game()


# # 创建了settings模块和类后，修改代码：
# import sys
# import pygame
# from settings import Settings
#
#
# def run_game():
#     """使用settings类进行代码修改"""
#     pygame.init()
#     # 创建一个实例：
#     ai_settings = Settings()
#     screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
#
#     # 背景色已设置，下面这句省略：
#     # bg_color = (ai_settings.bg_color)
#
#     pygame.display.set_caption("Alien_war")
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#
#         # 填充背景色：
#         screen.fill(ai_settings.bg_color)
#
#         pygame.display.flip()
#
#
# run_game()




# 二、添加飞船图像：
# # 选择表示飞船的图像之后，我们需要将其显示到屏幕上：
# import sys
# import pygame
# from settings import Settings
# from ship import Ship
#
# def run_game():
#     """添加飞船后，修改代码"""
#     pygame.init()
#     # 设置窗口大小和名称：
#     ai_settings = Settings()
#     screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
#     pygame.display.set_caption('Alien_war')
#
#     # 创建一艘飞船：
#     ship = Ship(screen)
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#
#         # 填充屏幕的颜色(每次循环都重新绘制屏幕)：
#         screen.fill(ai_settings.bg_color)
#         # 绘制飞船：
#         ship.draw_ship()
#
#         # 让最近绘制的屏幕可见：
#         pygame.display.flip()
#
# run_game()




# 三、进行重构，将函数放入game_functions中后简化run_game()函数：
import pygame
import game_functions as g_f
from ship import Ship
from settings import Settings
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from show_score import Scoreboard


def run_game():
    """简化函数"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien_war")

    # 创建一个play按钮：
    play_button = Button(ai_settings, screen, "Play")

    # 创建游戏统计信息的实例，并创建一个记分牌：
    stats = GameStats(ai_settings)
    score = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船：
    ship = Ship(ai_settings, screen)
    # 创建一个存储子弹编组 ：
    bullets = Group()

    # # 创建一个外星人实例：
    # alien = Alien(ai_settings, screen)
    # 为创建多个外星人，先创建一个外星人组：
    aliens = Group()

    # 创建外星人群：
    g_f.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        # 处理事件：
        g_f.check_events(ai_settings, screen, ship, play_button, stats, aliens, bullets, score)

        # 判断哪些代码在游戏活跃时运行：
        if stats.game_active:
            # 更新飞船的位置：
            ship.update()

            # # 更新子弹的位置：
            # bullets.update()
            # # 删除已消失的子弹：
            # for bullet in bullets.copy():
            #     if bullet.rect.bottom <= 0:
            #         bullets.remove(bullet)
            # 可将管理子弹的代码移到game_functions中，从而简化为：
            g_f.update_bullets(ai_settings, screen, ship, bullets, aliens, stats, score)

            # 更新外星人的位置(在有外星人撞到飞船时，我们将用这些实参来跟踪玩家还有多少艘飞船)：
            g_f.update_aliens(ai_settings, screen, stats, ship, aliens, bullets, score)

        # 更新屏幕：
        g_f.update_screen(ai_settings, screen, ship, aliens, bullets, play_button, stats, score)


run_game()





































