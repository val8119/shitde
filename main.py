import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox

# variables
file_types = [("All types (*.*)", "*.*"), ("Text file (*.txt)", "*.txt"), ("Python (*.py)", "*.py")]
text_size = 10

root = tk.Tk()


def do_nothing():
    pass


def about():
    tk.messagebox.showinfo("About ShitDE v0.1", "What is ShitDE:\nShitDE is something I made because I was bored. I was supposed to play Among Us! with friends but only like 5 people showed up so we got bored and I ended up doing this.\n\nWhat does ShitDE mean:\nShitDE means Shit Development Environment, because I can't be asked to come up with a name for something as shitty as this.\n\nMade by val8119 on GitHub")


def file_save(event):
    f = tk.filedialog.asksaveasfile(mode='w', defaultextension="*.txt", filetypes=file_types)
    if f is None:
        return
    text = str(text_area.get("1.0", "end"))
    f.write(text)
    f.close()


def file_open():
    f = tk.filedialog.askopenfilename(defaultextension="*.txt", filetypes=file_types)
    if f is None:
        return
    text_area.delete(1.0, "end")
    text_area.insert(1.0, open(f, 'r').read())


# menu bar
menu = tk.Menu(root)
filemenu = tk.Menu(menu, tearoff=0)
filemenu.add_command(label="New file", command=do_nothing)
filemenu.add_command(label="Open file...", command=file_open)
filemenu.add_command(label="Save as...", command=file_save)
menu.add_cascade(label="File", menu=filemenu)

helpmenu = tk.Menu(menu, tearoff=0)
helpmenu.add_command(label="About...", command=about)
menu.add_cascade(label="Help", menu=helpmenu)

text_area = tk.Text(fg="#ededed", font=("Courier New", 10, "bold"))
text_area.pack(expand="yes", fill="both")

root.geometry("600x400")
root.config(menu=menu)
root.bind("<Control-s>", file_save)
root.iconphoto(False, tk.PhotoImage(file="icon.png"))
root.title("ShitDE v0.1")
root.mainloop()