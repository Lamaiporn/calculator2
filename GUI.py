import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self):
        # สร้างหน้าต่างหลัก
        self.window = tk.Tk()
        self.window.title("เครื่องคิดเลข")
        self.window.geometry("320x400")
        self.window.resizable(0, 0)
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # ปรับแต่งสไตล์ของปุ่ม
        self.style.configure("TButton", font=("Arial", 15), padding=10)
        
        # หน้าจอแสดงผล
        self.display = tk.Entry(self.window, font=('Arial', 24), justify='right', bg="#E0E0E0", bd=8, relief="sunken")
        self.display.grid(row=0, column=0, columnspan=4, sticky="we", padx=5, pady=5)

        # ปุ่มตัวเลขและเครื่องหมาย
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            ttk.Button(self.window, text=button, command=cmd).grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        # ปุ่มล้างข้อมูล
        ttk.Button(self.window, text='C', command=self.clear).grid(row=5, column=0, columnspan=4, padx=2, pady=2, sticky="nsew")

        # ปรับแต่งขนาดแถวและคอลัมน์ให้ขยายตามขนาดหน้าต่าง
        for i in range(4):
            self.window.grid_columnconfigure(i, weight=1)
        for i in range(1, 6):
            self.window.grid_rowconfigure(i, weight=1)
    
    def click(self, key):
        if key == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, key)
            
    def clear(self):
        self.display.delete(0, tk.END)
        
    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    calc = Calculator()
    calc.run()
