# 本模块储存一些让游戏运行的函数

# 首先我们把管理事件的代码移到一个名为check_events()函数中：
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


# def check_events(ship):
#     """响应按键和鼠标事件"""
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#         # elif event.type == pygame.KEYDOWN:
#         #     if event.key == pygame.K_RIGHT:
#         #         ship.ship_rect.centerx += 1
#         #     if event.key == pygame.K_LEFT:
#         #         ship.ship_rect.centerx -= 1
#
#         # 优化：操控飞船可不断的移动：我们设置一个标志moving_right,玩家按下右键时,为true,飞船不停的向右移动,松开时，为False，停止移动(同理，向左移动)
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 ship.moving_right = True
#             elif event.key == pygame.K_LEFT:
#                 ship.moving_left = True
#
#         elif event.type == pygame.KEYUP:
#             if event.key == pygame.K_RIGHT:
#                 ship.moving_right = False
#             elif event.key == pygame.K_LEFT:
#                 ship.moving_left = False


# 重构check_events()，将其代码放到两个函数check_keydown_events和check_keyup_events中：

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按下键盘事件"""
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            # 按下空格键时，生成一颗子弹
            fire_bullet(ai_settings, screen, ship, bullets)
        elif event.key == pygame.K_q:
            # 按下q之后，自动关闭游戏：
            sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """把发射子弹的代码独立出来"""
    if len(bullets) < ai_settings.bullet_allowed:
        # 判断屏幕中的子弹数是否小于允许出现的子弹数：
        bullet = Bullet(ai_settings, screen, ship)
        bullets.add(bullet)


def check_keyup_events(event, ship):
    """响应松开键盘事件"""
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False


def check_events(ai_settings, screen, ship, play_button, stats, aliens, bullets, score):
    """处理总事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # mouse.get_pos()方法获取鼠标的x，y坐标：
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, ship, play_button, mouse_x, mouse_y, stats, aliens, bullets, score)


def check_play_button(ai_settings, screen, ship, play_button, mouse_x, mouse_y, stats, aliens, bullets, score):
    """在玩家单机play按钮时开始新游戏，并重置游戏"""
    # 为避免在游戏运行过程中，点击play区域也会重新开始游戏，设置成只有游戏为非活跃状态时才会重置游戏：
    # 函数collidepoint()检测鼠标单击位置是否在按钮rect内：
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:

        # 每当玩家开始新游戏时，都重置游戏设置(否则会是上一次游戏结束时的速度)：
        ai_settings.initialize_dynamic_settings()

        # 让游戏在活跃状态时隐藏光标：
        pygame.mouse.set_visible(False)

        # 重置游戏统计信息：
        stats.reset_stats()
        stats.game_active = True

        # 重置记分牌：
        score.prep_score()
        score.prep_top_score()
        score.prep_level()
        score.prep_ships()

        # 清空外星人和子弹列表：
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并让飞船居中：
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


# 下面将更新屏幕的代码放到函数update_screen()中：
def update_screen(ai_settings, screen, ship, aliens, bullets, play_button, stats, score):
    """更新屏幕，并切换到新屏幕"""

    # 每次循环时都重新绘制屏幕：
    screen.fill(ai_settings.bg_color)

    # 显示得分,等级,飞船数：
    score.show_score()

    # 绘制飞船：
    ship.draw_ship()

    # # 绘制单个外星人：
    # aliens.draw_alien()
    # 绘制外星人群:对编组调用draw()函数，会自动对编组的每个元素进行绘制，绘制位置由元素的属性rect决定：
    aliens.draw(screen)

    # 绘制子弹：
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 当游戏处于非活跃状态时，显示按钮：
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见：
    pygame.display.flip()


# def update_bullets(ai_settings, screen, ship, bullets, aliens):
#     """更新子弹的位置，并删除已消失的子弹"""
#     # 更新子弹的位置：
#     bullets.update()
#     # 删除已消失的子弹：
#     for bullet in bullets.copy():
#         if bullet.rect.bottom <= 0:
#             bullets.remove(bullet)
#
#     # 检查是否有子弹击中了外星人,如果是,就删除子弹和外星人：
#     # 这行代码遍历buttles中的每颗子弹和aliens中的每个外星人，每当有rect重叠的时候，就在它返回的字典中添加一个键值对：
#     collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
#     # 实参True告诉pygame删除发生碰撞的元素
#
#     # 检测是否消灭了所有外星人(即编组aliens是否为空),如果为空,则删除现有的子弹并新创建一群外星人:
#     if len(aliens) == 0:
#         bullets.empty()
#         create_fleet(ai_settings, screen, ship, aliens)


# 重构update_bullets()函数，将处理碰撞的代码移到另一个函数中：
def update_bullets(ai_settings, screen, ship, bullets, aliens, stats, score):
    """更新子弹的位置，并删除消失子弹"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(ai_settings, screen, ship, bullets, aliens, stats, score)


def check_bullet_alien_collision(ai_settings, screen, ship, bullets, aliens, stats, score):
    """检测外星人和子弹是否发生碰撞"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        # 每当击落一个外星人，就更新一下得分
        # (此方法碰撞一下增加一个外星人的分数，如果一次碰撞消灭了两个外星人，则只增加一个外星人的分数，因此需要修改碰撞方式)：
        for aliens in collisions.values():
            # collisions.values()值表示一个列表，包含被同一个子弹击中的所有外星人
            stats.score += ai_settings.alien_point * len(aliens)
            score.prep_score()
        check_top_score(stats, score)

    if len(aliens) == 0:
        # 消灭所有的外星人后：
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        # 加快游戏节奏：
        ai_settings.increase_speed()
        # 等级提高：
        stats.level += 1
        score.prep_level()


# def create_fleet(ai_settings, screen, aliens):
#     """创建外星人群"""
#     # 创建一个外星人，并计算一行可以放多少外星人
#     # 外星人间距为外星人宽度：
#     alien = Alien(ai_settings, screen)
#     alien_width = alien.rect.width
#
#     # 放置外星人的水平空间为(屏幕宽度-外星人宽度的两倍)：
#     put_alien_x = ai_settings.screen_width - alien_width * 2
#     # 一行可放置外星人数(可放置区域/一个外星人所需区域)：
#     aliens_number_x = int(put_alien_x / (alien_width * 2))
#
#     # 创建第一行外星人：
#     for alien_number in range(aliens_number_x):
#         # 创建一个外星人：
#         alien = Alien(ai_settings, screen)
#         # 加入到当前行（外星人的位置）：
#         alien.x = alien_width + alien_width * 2 * alien_number
#         alien.rect.x = alien.x
#         aliens.add(alien)


# 重构create_fleet()函数，增加两个函数：
def get_aliens_number_x(ai_settings, alien_width):
    """计算一行可放置多少外星人"""
    put_alien_x = ai_settings.screen_width - alien_width * 2
    aliens_number_x = int(put_alien_x / (alien_width * 2))
    return aliens_number_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算可放置多少行外星人"""
    # 首先计算可放置垂直区域：
    put_alien_y = ai_settings.screen_height - ship_height - 3 * alien_height
    # 计算可放置的行数：
    put_rows = int(put_alien_y / (2 * alien_height))
    return put_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并放置在当前行"""
    alien = Alien(ai_settings, screen)
    # 使用新创建的外星人来获取外星人宽度：
    alien_width = alien.rect.width
    alien.x = alien_width + alien_width * 2 * alien_number
    alien.rect.x = alien.x
    # 第一行的行号为0：
    alien.rect.y = alien.rect.height + alien.rect.height * 2 * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人：
    alien = Alien(ai_settings, screen)
    # 计算一行可放置多少外星人：
    aliens_number_x = get_aliens_number_x(ai_settings, alien.rect.width)
    # 计算可放置多少行：
    put_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # 创建外星人群：
    for row_number in range(put_rows):
        for alien_number in range(aliens_number_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """将外星人下移，并改变外星人的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.down_speed
    # 反向移动：
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, screen, stats, ship, aliens, bullets, score):
    """响应外星人撞到飞船"""
    if stats.ships_left > 0:
        # 外星人撞到飞船后，飞船数量减一：
        stats.ships_left -= 1
        score.prep_ships()

        # 清空子弹和外星人：
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船居中(调用方法center_ship())：
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停：
        sleep(0.5)

    else:
        # 飞船用完后游戏将停止：
        stats.game_active = False

        # 游戏结束时让光标可见：
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, screen, stats, ship, aliens, bullets, score):
    """检测是否有外星人到达了底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, ship, aliens, bullets, score)
            break


def update_aliens(ai_settings, screen, stats, ship, aliens, bullets, score):
    """更新外星人中所有外星人的位置，检查是否有外星人位于边缘"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测是否有外星人和飞船发生碰撞：
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, ship, aliens, bullets, score)

    # 检测是否有外星人到达底端：
    check_aliens_bottom(ai_settings, screen, stats, ship, aliens, bullets, score)


def check_top_score(stats, score):
    """检查是否产生了新的最高分数"""
    if stats.score > stats.top_score:
        stats.top_score = stats.score
        score.prep_top_score()























