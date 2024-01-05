from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task:
        lb.insert(END, task)
        my_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter some task.")

def deleteTask():
    selected_task = lb.curselection()
    if selected_task:
        lb.delete(selected_task[0])

ws = Tk()
ws.geometry('500x450+500+200')
ws.title('PythonGuides')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)

frame = Frame(ws, bg='#223441')
frame.grid(row=0, column=0, pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
)
lb.grid(row=0, column=0, padx=10, pady=10, sticky='ns')

task_list = [
    'Walk the dog',
    'Read a book',
    'Call a friend',
    'Buy groceries',
    'Watch a movie',
    'Cook dinner',
    'Exercise',
    'Listen to music'
]

for idx, item in enumerate(task_list):
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.grid(row=0, column=1, sticky='ns')

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
)
my_entry.grid(row=1, column=0, pady=20)

button_frame = Frame(ws, bg='#223441')
button_frame.grid(row=2, column=0, pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.grid(row=0, column=0, padx=5)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.grid(row=0, column=1, padx=5)

ws.mainloop()
