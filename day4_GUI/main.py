import pygame
from enum import Enum, unique
from math import sqrt
from random import randint


# import tkinter
# import tkinter.messagebox
#
#
# def main():
#     flag = True
#
#     def change_label_text():
#         nonlocal flag
#         flag = not flag
#         color, msg = ("red", "Hello world!") \
#             if flag else ("blue", "good bye,world!")
#         label.config(text=msg, fg=color)
#
#     def confirm_to_quit():
#         if tkinter.messagebox.askokcancel("warmly remind", "confirm to quit?"):
#             top.quit()
#
#     top = tkinter.Tk()
#     top.geometry("240X160")
#     top.title("game")
#     label = tkinter.Label(top, text="hello world!",
#                           font="Arial -32", fg="red")
#     label.pack(expand=1)
#     panel = tkinter.Frame(top)
#     button1 = tkinter.Button(panel, text="modify", command=change_label_text)
#     button1.pack(side="left")
#     button2 = tkinter.Button(panel, text="quit", command=confirm_to_quit)
#     button2.pack(side="bottom")
#     tkinter.mainloop()
#
#
#     if __name__ == "__main__":
#         main()

# @unique装饰器可以帮助我们检查保证没有重复值
@unique
class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    GRAY = (242, 242, 242)
    WHITE = (255, 255, 255)

    @staticmethod
    def random_color():
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)


class Ball(object):

    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def fight(self, other):
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color,(self.x, self.y), self.radius, 0)


'''
display a ball
def main():
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((1200, 1000))
    # 设置当前窗口的标题
    pygame.display.set_caption("big ball eat small ball")
    # 设置窗口的背景色(颜色是由红绿蓝三原色构成的元组)
    # screen.fill((255, 255, 255))
    # ball_image = pygame.image.load("/home/lx/pythonProject/python_100_days/day4_GUI/ball.jpg")
    # screen.blit(ball_image,(100,100))
    # 绘制一个圆(参数分别是: 屏幕, 颜色, 圆心位置, 半径, 0表示填充圆)
    # pygame.draw.circle(screen, (255, 0, 0), (100, 100), 30, 0)
    # 刷新当前窗口(渲染窗口将绘制的图像呈现出来)
    # pygame.display.flip()
    x, y = 50, 50
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 30, 0)
        pygame.display.flip()
        # 每隔50毫秒就改变小球的位置再刷新窗口
        pygame.time.delay(50)
        x, y = x + 3, y + 3
'''


# display a lot ball
def main():
    balls = []
    pygame.init()
    screen = pygame.display.set_mode((1200, 1000))
    pygame.display.set_caption("big balls eat small balls")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # 处理鼠标事件的代码
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                # 在点击鼠标的位置创建一个球(大小、速度和颜色随机)
                ball = Ball(x, y, radius, sx, sy, color)
                balls.append(ball)
        screen.fill((255, 255, 255))
        # 取出容器中的球 如果没被吃掉就绘制 被吃掉了就移除
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)

        pygame.display.flip()
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            # 检查球有没有吃到其他的球
            for other in balls:
                ball.fight(other)


if __name__ == "__main__":
    main()
