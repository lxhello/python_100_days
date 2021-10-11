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
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("big ball eat small ball")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()
