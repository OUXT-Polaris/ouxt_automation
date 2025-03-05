import pygame
import time


class JoyController:
    gap = 0.1
    stick_lx = 0.0
    stick_ly = 0.0
    stick_rx = 0.0
    stick_ry = 0.0
    mode = 1

    def __init__(self):
        pygame.init()
        self.j = pygame.joystick.Joystick(0)
        self.j.init()

    def update(self):
        try:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.JOYBUTTONDOWN:  # ボタンが押された場合
                    # print("Xボタンが押されました(auto)")
                    if self.j.get_button(0):
                        self.mode = 0
                    # print("Aボタンが押されました(stop)")
                    elif self.j.get_button(1):
                        self.mode = 1
                    # print("Bボタンが押されました(manual)")
                    elif self.j.get_button(2):
                        self.mode = 2
                    # print("Yボタンが押されました")
                    elif self.j.get_button(3):
                        pass
                elif event.type == pygame.JOYAXISMOTION:

                    def zero(value, gap):
                        if abs(value) <= self.gap:
                            return 0.0
                        else:
                            return value

                    self.stick_lx = zero(self.j.get_axis(0), self.gap)
                    self.stick_ly = zero(self.j.get_axis(1), self.gap)
                    self.stick_rx = zero(self.j.get_axis(2), self.gap)
                    self.stick_ry = zero(self.j.get_axis(3), self.gap)
            # print(f"左スティック座標 ({stick_lx}, {stick_ly}),右スティック座標 ({stick_rx}, {stick_ry}),状態：{mode}")

        except KeyboardInterrupt:
            print("プログラムを終了します")
            j.quit()
