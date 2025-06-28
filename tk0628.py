import tkinter as tk
import tkinter.messagebox

def clickMe():
  tkinter.messagebox.showinfo(title = "你變帥了", message = "成功變帥！")


window = tk.Tk()
window.title("my GUI program")
window.geometry('300x300')

label = tk.Label(window, text="帥哥的日記", bg="#05A", fg="#330")
label.pack()

entry = tk.Entry(window, width = 30)
entry.pack()

button = tk.Button(window, text = "按了會變帥哥", command= clickMe)
button.pack()

window.mainloop()

