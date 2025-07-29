from tkinter import *
from tkinter import ttk, messagebox
from db_handler import add_employee, update_employee, delete_employee, fetch_employees
from validation import is_valid_age, is_valid_salary

class EmployeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("1200x600")
        self.root.resizable(False, False)

        # Title
        title = Label(self.root, text="Employee Management System", font=("arial", 20, "bold"), bg="skyblue", pady=10)
        title.pack(fill=X)

        # Left Frame (Form)
        left = Frame(self.root, bg="lightyellow", bd=2, relief=GROOVE)
        left.place(x=10, y=70, width=400, height=520)

        Label(left, text="Employee Details", font=("arial", 14, "bold"), bg="lightyellow").place(x=90, y=10)

        Label(left, text="ID", bg="lightyellow").place(x=20, y=60)
        self.id_entry = Entry(left, width=30)
        self.id_entry.place(x=150, y=60)

        Label(left, text="Name", bg="lightyellow").place(x=20, y=100)
        self.name_entry = Entry(left, width=30)
        self.name_entry.place(x=150, y=100)

        Label(left, text="Age", bg="lightyellow").place(x=20, y=140)
        self.age_entry = Entry(left, width=30)
        self.age_entry.place(x=150, y=140)

        Label(left, text="Salary", bg="lightyellow").place(x=20, y=180)
        self.salary_entry = Entry(left, width=30)
        self.salary_entry.place(x=150, y=180)

        Label(left, text="Department", bg="lightyellow").place(x=20, y=220)
        self.dept_entry = Entry(left, width=30)
        self.dept_entry.place(x=150, y=220)

        Button(left, text="Add", width=20, command=self.add).place(x=100, y=270)
        Button(left, text="Update", width=20, command=self.update).place(x=100, y=310)
        Button(left, text="Delete", width=20, command=self.delete).place(x=100, y=350)
        Button(left, text="Clear", width=20, command=self.clear).place(x=100, y=390)

        # Right Frame (Treeview)
        right = Frame(self.root, bd=2, relief=GROOVE)
        right.place(x=420, y=70, width=760, height=520)

        self.tree = ttk.Treeview(right, columns=("ID", "Name", "Age", "Salary", "Department"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=CENTER, width=140)
        self.tree.pack(fill=BOTH, expand=True)
        self.tree.bind("<ButtonRelease-1>", self.load_selected_row)

        self.refresh_tree()

    def get_inputs(self):
        return (
            self.id_entry.get().strip(),
            self.name_entry.get().strip(),
            self.age_entry.get().strip(),
            self.salary_entry.get().strip(),
            self.dept_entry.get().strip()
        )

    def add(self):
        id, name, age, salary, dept = self.get_inputs()
        if not all([id, name, age, salary, dept]):
            messagebox.showerror("Error", "All fields are required.")
            return
        if not is_valid_age(age):
            messagebox.showerror("Error", "Invalid Age. Must be between 18 and 65.")
            return
        if not is_valid_salary(salary):
            messagebox.showerror("Error", "Invalid Salary. Must be a number >= 0.")
            return
        msg = add_employee(id, name, int(age), float(salary), dept)
        self.refresh_tree()
        self.clear()
        messagebox.showinfo("Info", msg)

    def update(self):
        id, name, age, salary, dept = self.get_inputs()
        if not id:
            messagebox.showerror("Error", "ID required for update.")
            return
        msg = update_employee(id, name, age, salary, dept)
        self.refresh_tree()
        self.clear()
        messagebox.showinfo("Info", msg)

    def delete(self):
        id = self.id_entry.get().strip()
        if not id:
            messagebox.showerror("Error", "ID required for delete.")
            return
        msg = delete_employee(id)
        self.refresh_tree()
        self.clear()
        messagebox.showinfo("Info", msg)

    def clear(self):
        for widget in [self.id_entry, self.name_entry, self.age_entry, self.salary_entry, self.dept_entry]:
            widget.delete(0, END)

    def refresh_tree(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in fetch_employees():
            self.tree.insert("", END, values=row)

    def load_selected_row(self, event):
        selected = self.tree.focus()
        values = self.tree.item(selected, 'values')
        if values:
            self.clear()
            self.id_entry.insert(0, values[0])
            self.name_entry.insert(0, values[1])
            self.age_entry.insert(0, values[2])
            self.salary_entry.insert(0, values[3])
            self.dept_entry.insert(0, values[4])


if __name__ == "__main__":
    root = Tk()
    app = EmployeeApp(root)
    root.mainloop()
