import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkFont
from periodic_table import PeriodicTable
from calculator import WeightCalculator


class WeightCalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('800x400')
        self.title('Weight Calculator')
        self.text_font= tkFont.Font(family="Helvetica",size=11)
        self.text_font1= tkFont.Font(family="Helvetica",size=10,weight="bold")
        tk.Label(self, text='No of element',font=self.text_font1).place(x=50, y=3)
        self.n1 = tk.StringVar()
        tk.Entry(self, textvariable=self.n1,font=self.text_font,width=10).place(x=150, y=5)
        tk.Button(self, text='Ok',font=self.text_font, command=self.add_element).place(x=300, y=0)

    def add_element(self):
        main_frame=tk.Frame(self,width=1000, height=290)
        main_frame.place(relx=0.1, rely=0.1)
        tk.Label(main_frame, text='Symbol',font=self.text_font1).place(x=0, y=70)
        tk.Label(main_frame, text='Atomic Mass',font=self.text_font1).place(x=0, y=100)
        tk.Label(main_frame, text='Ratio',font=self.text_font1).place(x=0, y=180)
        tk.Label(main_frame, text='Fix',font=self.text_font1).place(x=0, y=210)
        tk.Label(main_frame, text='Weight (gm)',font=self.text_font1).place(x=0, y=240)
        tk.Label(main_frame, text='Total (gm)',font=self.text_font1).place(x=0, y=270)
        self.n2=[]
        self.n3=[]
        self.n4=[]
        self.n5=[]
        options = ["Total"]
        for i in range(int(self.n1.get())):
            tk.Label(main_frame, text=f'Element{i+1}',font=self.text_font1).place(x=100 * i+155, y=0)
            label = tk.Button(main_frame, text='Select',font=self.text_font, command=lambda i=i: self.pt(i))
            label.place(x=100*i+160,y=25)
            options.append(f'Element{i+1}')
            self.n2.append(tk.StringVar())
            tk.Label(main_frame,textvariable=self.n2[i],font=self.text_font).place(x=100 * i+175, y=70)
            self.n3.append(tk.StringVar())
            tk.Label(main_frame, textvariable=self.n3[i],font=self.text_font).place(x=100 * i + 165, y=100)
            self.n4.append(tk.StringVar())
            tk.Entry(self,textvariable=self.n4[i], width=5,font=self.text_font).place(x=100 * i + 247, y=220)
            self.n5.append(tk.StringVar())
            tk.Entry(self,textvariable=self.n5[i], width=10,font=self.text_font).place(x=100 * i + 230, y=280)
        self.combo = ttk.Combobox(self, values=options)
        self.combo.place(x=230, y=250)
        self.combo.current(0)
        self.n6=tk.StringVar()
        tk.Entry(self, textvariable=self.n6, width=10,font=self.text_font).place(x=230, y=310)
        tk.Button(self, text='Calculate',font=self.text_font, command=self.calculate).place(x=400,y=310)

    def pt(self, index):
        PeriodicTable(self, index)

    def calculate(self):
        if any(entry.get() == '' for entry in self.n4):
            messagebox.showerror("Input Error", "Put some value in Ratio")
            return
        if self.combo.current() == 0 and self.n6.get() == '':
            messagebox.showerror("Input Error", "Put some value in Total")
            return
        if self.combo.current() != 0 and self.n5[self.combo.current() - 1].get() == '':
            messagebox.showerror("Input Error", "Put some value in Weight")
            return

        result = WeightCalculator.calculate(self.n1.get(), self.n3, self.n4, self.n5, self.n6.get(), self.combo.current())

        for i, value in enumerate(result['weights']):
            self.n5[i].set(round(value, 5))
        self.n6.set(round(result['total'], 5))


if __name__ == "__main__":
    app = WeightCalculatorApp()
    app.mainloop()
