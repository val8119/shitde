import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk
import os, sys

# variables
file_types = [("All types (*.*)", "*.*"), ("Text file (*.txt)", "*.txt"), ("Python (*.py)", "*.py")]
text_size = 10

root = tk.Tk()


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def do_nothing():
    pass


def about():
    tk.messagebox.showinfo("About ShitDE v0.1", "What is ShitDE:\nShitDE is something I made because I was bored. I was supposed to play Among Us! with friends but only like 5 people showed up so we got bored and I ended up doing this.\n\nWhat does ShitDE mean:\nShitDE means Shit Development Environment, because I can't be asked to come up with a name for something as shitty as this.\n\nMade by val8119 on GitHub")


def ctrl_s(event):
    file_save()


def file_save():
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


def ask_save():
    ask_dialog = tk.messagebox.askquestion("New File", "Save current file?",icon="warning")

    if ask_dialog == "yes":
        file_save()
        text_area.delete(1.0, "end")
    else:
        text_area.delete(1.0, "end")


# menu bar
menu = tk.Menu(root)
filemenu = tk.Menu(menu, tearoff=0)
filemenu.add_command(label="New File", command=ask_save)
filemenu.add_command(label="Open File...", command=file_open)
filemenu.add_command(label="Save As...", command=file_save)
menu.add_cascade(label="File", menu=filemenu)

helpmenu = tk.Menu(menu, tearoff=0)
helpmenu.add_command(label="About...", command=about)
menu.add_cascade(label="Help", menu=helpmenu)

# text area
text_container = tk.Frame(root, borderwidth=0)

text_area = tk.Text(fg="#ededed", font=("Courier New", 10, "bold"), borderwidth=0, wrap="no")
text_area.pack(expand="yes", fill="both")



root.geometry("600x400")
root.config(menu=menu)
root.bind("<Control-s>", ctrl_s)
root.iconphoto(False, tk.PhotoImage(file=resource_path("icon.png")))
root.title("ShitDE v0.1")
root.mainloop()