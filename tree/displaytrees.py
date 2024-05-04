def display(root, **kwargs):
    def draw(node, canvas, x, y, x_offset, y_offset, avl):
        if node == None:
            return
        
        canvas.create_oval(x-15, y-15, x+15, y+15, fill="white")
        canvas.create_text(x, y, text=str(node.v))
        canvas.create_text(x+25, y, text=str(node.i))
        if avl:
            #canvas.create_text(x-25, y, text=str(node.lvl))
            canvas.create_text(x, y+25, text=str(node.b))
        if node.l:
            canvas.create_line(x, y, x-x_offset, y+y_offset, arrow=tk.LAST)
            draw(node.l, canvas, x-x_offset, y+y_offset, x_offset//2, y_offset, avl)
        if node.r:
            canvas.create_line(x, y, x+x_offset, y+y_offset, arrow=tk.LAST)
            draw(node.r, canvas, x+x_offset, y+y_offset, x_offset//2, y_offset, avl)

    import tkinter as tk

    win = tk.Tk()
    win.title('Visualizador de árboles')

    canvas = tk.Canvas(win, width=800, height=600)
    canvas.pack()

    if len(kwargs) > 0:
        if kwargs['avl']:
            draw(root, canvas, 400, 50, 200, 100, True)
    else:
        draw(root, canvas, 400, 50, 200, 100, False)
    win.mainloop()