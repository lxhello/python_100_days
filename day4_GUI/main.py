import pygame


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

def main():
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((1200, 1000))
    # 设置当前窗口的标题
    pygame.display.set_caption("big ball eat small ball")
    # 设置窗口的背景色(颜色是由红绿蓝三原色构成的元组)
    screen.fill((242, 242, 242))
    # 绘制一个圆(参数分别是: 屏幕, 颜色, 圆心位置, 半径, 0表示填充圆)
    pygame.draw.circle(screen, (255, 0, 0), (100, 100), 30, 0)
    # 刷新当前窗口(渲染窗口将绘制的图像呈现出来)
    pygame.display.flip()
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
