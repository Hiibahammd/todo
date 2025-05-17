import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb

# add task
#delte task
#complete task

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")


        self.frame1 = tk.Frame(self.root, bd=2, relief=tk.FLAT)
        self.frame1.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.frame1,height=1,width=30,bd=0 ,font=("Century Gothic", 15))
        self.textbox.pack(side= tk.LEFT,padx=10, pady=10,fill=tk.BOTH, expand=True) 

        self.button = tk.Button(
            self.frame1, 
            text="ADD TASK", 
            font=("Century Gothic", 15),
            relief="groove", 
            command=self.add_task)
        self.button.pack(side=tk.RIGHT)

        self.tasks_frame = tk.Frame(self.root,bd=2, relief=tk.FLAT)
        self.tasks_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(self.tasks_frame,font=("Century Gothic", 12))
        self.listbox.pack(side="left",padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.task_count = 0

        self.frame_btn = tk.Frame(self.root,bd=2, relief=tk.FLAT)
        self.frame_btn.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.button1 = tk.Button(
            self.frame_btn, 
            text="Delete Task", 
            font=("Century Gothic", 15),
            relief="groove", 
            command= self.del_task
        )
        self.button1.pack(side=tk.RIGHT)

        self.button2 = tk.Button(
            self.frame_btn, 
            text="Complete Task", 
            font=("Century Gothic", 15),
            relief="groove", 
            command= self.cmp_task
        )
        self.button2.pack(side=tk.LEFT)

        self.listbox_cmp = tk.Listbox(self.tasks_frame,font=("Century Gothic", 12))
        self.listbox_cmp.pack(side="right",padx=10, pady=10, fill=tk.BOTH, expand=True)

    def strike(self, text):
        return ''.join(char + '\u0336' for char in text)
    
    def add_task(self):
        task = self.textbox.get("1.0",tk.END).strip()
        if task:
            self.task_count += 1
            num_task = f"{self.task_count}. {task}"
            self.listbox.insert(tk.END, num_task)
            self.textbox.delete("1.0",tk.END)
        else:
            messagebox.showwarning("Warning","Please enter a task")

    def del_task(self):
        sel_index = self.listbox.curselection()
        sel2_index = self.listbox_cmp.curselection()
        if sel_index:
            self.listbox.delete(sel_index)
        elif sel2_index:
            self.listbox_cmp.delete(sel2_index)
            
        else:
            messagebox.showwarning("Warning","Please select a task to delete")
    
    def cmp_task(self):
        sel_index = self.listbox.curselection()
        if sel_index:
            task_text = self.listbox.get(sel_index)
            task_text = self.strike(task_text)
            self.listbox_cmp.insert(tk.END,f"✔️ {task_text}")
            self.listbox.delete(sel_index)
        else:
            messagebox.showwarning("Warning","Please select a task to complete")


if __name__ == "__main__":
    root = tb.Window(themename="minty")
    app = Todo(root)
    root.mainloop()