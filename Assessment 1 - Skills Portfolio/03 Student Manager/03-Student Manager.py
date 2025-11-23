import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import os

class StudentManager:
    def __init__(self, window):
        self.window = window
        self.window.title("Student Manager Dashboard")
        self.window.geometry("1100x650")
        
        # this path points to your specific text file
        self.file_path = "Assessment 1 - Skills Portfolio/03 Student Manager/studentMarks.txt"
        self.students = []

        # use the clam theme to make the table look nicer
        style = ttk.Style()
        style.theme_use("clam")
        
        # configure the table colors and font size
        style.configure("Treeview", rowheight=30, font=("Arial", 11))
        style.configure("Treeview.Heading", font=("Arial", 11, "bold"), background="#ecf0f1")

        # create the left side menu frame with dark blue color
        self.menu_frame = tk.Frame(window, bg="#2c3e50", width=260)
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        # create the right side content frame with white color
        self.content_frame = tk.Frame(window, bg="white")
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # add a big title label inside the menu
        tk.Label(self.menu_frame, text="STUDENT\nMANAGER", bg="#2c3e50", fg="white", font=("Arial", 22, "bold")).pack(pady=40)

        # 1. view all button in light blue
        tk.Button(self.menu_frame, text="1. View All Students", command=self.view_all, bg="#3498db", fg="white", font=("Arial", 10, "bold"), width=22).pack(pady=5)
        
        # 2. view individual button in light blue
        tk.Button(self.menu_frame, text="2. Find Student", command=self.view_individual, bg="#3498db", fg="white", font=("Arial", 10, "bold"), width=22).pack(pady=5)

        # 3. highest score button in green
        tk.Button(self.menu_frame, text="3. Highest Score", command=self.show_highest, bg="#2ecc71", fg="white", font=("Arial", 10, "bold"), width=22).pack(pady=5)

        # 4. lowest score button in orange
        tk.Button(self.menu_frame, text="4. Lowest Score", command=self.show_lowest, bg="#e67e22", fg="white", font=("Arial", 10, "bold"), width=22).pack(pady=5)

        # 5. sort button in purple
        tk.Button(self.menu_frame, text="5. Sort List", command=self.sort_students, bg="#9b59b6", fg="white", font=("Arial", 10, "bold"), width=22).pack(pady=5)

        # 6. add button in teal
        tk.Button(self.menu_frame, text="6. Add Student", command=self.add_student, bg="#1abc9c", fg="white", font=("Arial", 10, "bold"), width=22).pack(pady=5)

        # 7. delete button in dark red
        tk.Button(self.menu_frame, text="7. Delete Student", command=self.delete_student, bg="#c0392b", fg="white", font=("Arial", 10, "bold"), width=22).pack(pady=5)

        # 8. update button in yellow
        tk.Button(self.menu_frame, text="8. Update Student", command=self.update_student, bg="#f1c40f", fg="black", font=("Arial", 10, "bold"), width=22).pack(pady=5)

        # exit button at the bottom
        tk.Button(self.menu_frame, text="EXIT APP", command=window.destroy, bg="red", fg="white", font=("Arial", 11, "bold"), width=22).pack(side=tk.BOTTOM, pady=20)

        # setup the columns for the table
        columns = ("code", "name", "cw", "exam", "overall", "grade")
        self.tree = ttk.Treeview(self.content_frame, columns=columns, show="headings")

        # set the heading text for each column
        self.tree.heading("code", text="Code")
        self.tree.heading("name", text="Name")
        self.tree.heading("cw", text="Total CW")
        self.tree.heading("exam", text="Exam")
        self.tree.heading("overall", text="Overall %")
        self.tree.heading("grade", text="Grade")

        # set the width and alignment for each column
        self.tree.column("code", width=80, anchor="center")
        self.tree.column("name", width=200)
        self.tree.column("cw", width=80, anchor="center")
        self.tree.column("exam", width=80, anchor="center")
        self.tree.column("overall", width=100, anchor="center")
        self.tree.column("grade", width=80, anchor="center")

        # add a scrollbar to the right side
        scrollbar = ttk.Scrollbar(self.content_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # load the data when we start
        self.load_students()
        self.refresh_table()

    # helper function to calculate the grade
    def calculate(self, marks, exam):
        total_cw = sum(marks)
        total_score = total_cw + exam
        # calculate percentage out of one hundred and sixty
        overall = (total_score / 160) * 100
        
        grade = "F"
        if overall >= 70: grade = "A"
        elif overall >= 60: grade = "B"
        elif overall >= 50: grade = "C"
        elif overall >= 40: grade = "D"
            
        return total_cw, overall, grade

    # helper function to create popup text
    def get_info_text(self, s):
        msg = "Name: " + s['name'] + "\n"
        msg = msg + "Code: " + s['code'] + "\n"
        msg = msg + "Coursework: " + str(s['cw']) + "/60\n"
        msg = msg + "Exam: " + str(s['exam']) + "/100\n"
        msg = msg + "Overall: {:.2f}%\n".format(s['overall'])
        msg = msg + "Grade: " + s['grade']
        return msg

    def load_students(self):
        self.students = []
        # check if file exists
        if not os.path.exists(self.file_path):
            return

        try:
            f = open(self.file_path, "r")
            lines = f.readlines()
            f.close()
            
            # skip the first line with the number count
            for line in lines[1:]:
                parts = line.strip().split(",")
                if len(parts) >= 6:
                    marks = [int(parts[2]), int(parts[3]), int(parts[4])]
                    exam = int(parts[5])
                    cw, overall, grade = self.calculate(marks, exam)
                    
                    self.students.append({
                        "code": parts[0], "name": parts[1], 
                        "marks": marks, "cw": cw, "exam": exam, 
                        "overall": overall, "grade": grade
                    })
        except:
            messagebox.showerror("Error", "Could not read file")

    def save_students(self):
        try:
            f = open(self.file_path, "w")
            f.write(str(len(self.students)) + "\n")
            for s in self.students:
                # format the string for the text file
                line = f"{s['code']},{s['name']},{s['marks'][0]},{s['marks'][1]},{s['marks'][2]},{s['exam']}\n"
                f.write(line)
            f.close()
        except:
            messagebox.showerror("Error", "Could not save file")

    def refresh_table(self):
        # delete old rows
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # put new rows in
        for s in self.students:
            self.tree.insert("", "end", values=(
                s['code'], s['name'], s['cw'], s['exam'], 
                "{:.2f}%".format(s['overall']), s['grade']
            ))

    def view_all(self):
        self.refresh_table()
        # calculate the class average
        total = 0
        for s in self.students:
            total = total + s['overall']
            
        avg = 0
        if len(self.students) > 0:
            avg = total / len(self.students)
            
        msg = "Total Students: " + str(len(self.students)) + "\n"
        msg = msg + "Class Average: {:.2f}%".format(avg)
        messagebox.showinfo("Class Summary", msg)

    def view_individual(self):
        code = simpledialog.askstring("Search", "Enter Student Code")
        for s in self.students:
            if s['code'] == code:
                messagebox.showinfo("Student Details", self.get_info_text(s))
                return
        messagebox.showerror("Error", "Student not found")

    def show_highest(self):
        if not self.students: return
        # find best student by percentage
        best = max(self.students, key=lambda x: x['overall'])
        messagebox.showinfo("Highest Score", self.get_info_text(best))

    def show_lowest(self):
        if not self.students: return
        # find worst student by percentage
        worst = min(self.students, key=lambda x: x['overall'])
        messagebox.showinfo("Lowest Score", self.get_info_text(worst))

    def sort_students(self):
        ask = messagebox.askyesno("Sort", "Yes = Low to High\nNo = High to Low")
        # sort the list based on overall score
        self.students.sort(key=lambda x: x['overall'], reverse=not ask)
        self.save_students()
        self.refresh_table()

    def add_student(self):
        code = simpledialog.askstring("Add", "Enter Code")
        # loop to check if code exists
        for s in self.students:
            if s['code'] == code:
                messagebox.showerror("Error", "Code exists")
                return
                
        name = simpledialog.askstring("Add", "Enter Name")
        try:
            m1 = simpledialog.askinteger("Add", "Mark 1 (0-20)", minvalue=0, maxvalue=20)
            m2 = simpledialog.askinteger("Add", "Mark 2 (0-20)", minvalue=0, maxvalue=20)
            m3 = simpledialog.askinteger("Add", "Mark 3 (0-20)", minvalue=0, maxvalue=20)
            ex = simpledialog.askinteger("Add", "Exam (0-100)", minvalue=0, maxvalue=100)
            
            marks = [m1, m2, m3]
            cw, overall, grade = self.calculate(marks, ex)
            
            self.students.append({
                "code": code, "name": name, "marks": marks, 
                "cw": cw, "exam": ex, "overall": overall, "grade": grade
            })
            self.save_students()
            self.refresh_table()
            messagebox.showinfo("Success", "Student Added")
        except:
            pass 

    def delete_student(self):
        # check if a row is clicked
        sel = self.tree.selection()
        if sel:
            code = self.tree.item(sel)['values'][0]
        else:
            code = simpledialog.askstring("Delete", "Enter Code")
            
        if not code: return
        
        if messagebox.askyesno("Confirm", "Delete this student"):
            # make a new list without that student code
            new_list = []
            for s in self.students:
                if str(s['code']) != str(code):
                    new_list.append(s)
            self.students = new_list
            
            self.save_students()
            self.refresh_table()

    def update_student(self):
        sel = self.tree.selection()
        if sel:
            code = self.tree.item(sel)['values'][0]
        else:
            code = simpledialog.askstring("Update", "Enter Code")
            
        # find the student object
        target = None
        for s in self.students:
            if str(s['code']) == str(code):
                target = s
                break
        
        if target:
            new_name = simpledialog.askstring("Update", "New Name", initialvalue=target['name'])
            if new_name:
                target['name'] = new_name
                if messagebox.askyesno("Update", "Update marks too"):
                    m1 = simpledialog.askinteger("Update", "Mark 1", minvalue=0, maxvalue=20)
                    m2 = simpledialog.askinteger("Update", "Mark 2", minvalue=0, maxvalue=20)
                    m3 = simpledialog.askinteger("Update", "Mark 3", minvalue=0, maxvalue=20)
                    ex = simpledialog.askinteger("Update", "Exam", minvalue=0, maxvalue=100)
                    
                    target['marks'] = [m1, m2, m3]
                    target['exam'] = ex
                    cw, ov, gr = self.calculate(target['marks'], ex)
                    target['cw'] = cw
                    target['overall'] = ov
                    target['grade'] = gr
                
                self.save_students()
                self.refresh_table()
        else:
            messagebox.showerror("Error", "Not found")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManager(root)
    root.mainloop()