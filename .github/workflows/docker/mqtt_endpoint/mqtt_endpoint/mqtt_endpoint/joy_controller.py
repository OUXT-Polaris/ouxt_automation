import pygame
import time

gap = 0.1

pygame.init()
j = pygame.joystick.Joystick(0)
j.init()
stick_lx = 0.0
stick_ly = 0.0
stick_rx = 0.0
stick_ry = 0.0
mode = 2


def update():
    try:
        events = pygame.event.get()
        for event in events:

            if event.type == pygame.JOYBUTTONDOWN:  # ボタンが押された場合
                if j.get_button(0):
                    mode = 0
                    # print("Xボタンが押されました(auto)")
                elif j.get_button(1):
                    mode = 2
                    # print("Aボタンが押されました(stop)")
                elif j.get_button(2):
                    mode = 1
                    # print("Bボタンが押されました(manual)")
                elif j.get_button(3):
                    # print("Yボタンが押されました")
                    pass
            elif event.type == pygame.JOYAXISMOTION:

                def zero(value, gap):
                    if abs(value) <= gap:
                        return 0.0
                    else:
                        return value

                stick_lx = zero(j.get_axis(0), gap)
                stick_ly = zero(j.get_axis(1), gap)
                stick_rx = zero(j.get_axis(2), gap)
                stick_ry = zero(j.get_axis(3), gap)
        # print(f"左スティック座標 ({stick_lx}, {stick_ly}),右スティック座標 ({stick_rx}, {stick_ry}),状態：{mode}")

    except KeyboardInterrupt:
        print("プログラムを終了します")
        j.quit()
