import math
import tkinter as tk
from sympy import symbols, Eq, solve
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import *
from PIL import *
from matplotlib.figure import Figure
import tkinter.font as tkfont
import os


class math_project():
    global x_points_global
    x_points_global=[]
    global y_points_global
    y_points_global=[]
    def __init__(self):
        self.st=0
        self.sr=0
        self.r_square=0
        self.r=0
        self.x_fitted_weighted=[]
        self.y_fitted_weighted=[]


    def linear_regression(self):
        x_points=x_points_global.copy()
        y_points=y_points_global.copy()
        y_points_plot=y_points_global.copy()
        print(x_points,y_points)
        sum_of_x=sum(x_points)
        sum_of_y=sum(y_points)
        sum_of_x_square=0
        sum_of_x_y=0
        n=len(x_points)
        for i in range(len(x_points)):
            sum_of_x_square=sum_of_x_square+pow(x_points[i],2)
            sum_of_x_y=sum_of_x_y+x_points[i]*y_points[i]
        print(f"sum of x={sum_of_x}\nsum of y={sum_of_y}\nsum of x^2={sum_of_x_square}\nsum of xy={sum_of_x_y}")
        a0, a1 = symbols('a0 a1')
        eq1 = Eq(n * a0 + sum_of_x * a1 - sum_of_y,0)
        eq2 = Eq(sum_of_x * a0 + sum_of_x_square * a1 -sum_of_x_y,0)
        sol_dict = solve((eq1,eq2), (a0, a1))
        a0=sol_dict[a0]
        a1=sol_dict[a1]
        print(f'a0 = {a0}')
        print(f'a1 = {a1}')

        self.sr=0
        self.st=0
        mean_of_y=sum_of_y/len(y_points)
        self.x_fitted_weighted=[]
        self.y_fitted_weighted=[]
        for i in range(len(x_points)):
            self.x_fitted_weighted.append(x_points_global[i])
            self.y_fitted_weighted.append(a0+a1*x_points[i])
            self.sr=self.sr+pow((y_points[i]-a0-a1*x_points[i]),2)
            self.st=self.st+pow((y_points[i]-mean_of_y),2)
        self.r_square=(self.st-self.sr)/self.st
        self.r=math.sqrt(self.r_square)
        self.sr_var.set(f"sr={round(self.sr,5)}")
        self.st_var.set(f"st={round(self.st,5)}")
        self.r_square_var.set(f"r^2={round(self.r_square,5)}")
        self.r_var.set(f"r={round(self.r,5)}")
        print(f"sr={self.sr}\nstst={self.st}\nr^2={self.r_square}\nr={self.r}")


        

    def exponential_model(self):
        x_points=x_points_global.copy()
        y_points=y_points_global.copy()
        y_points_plot=y_points_global.copy()
        for i in range(len(y_points)):
            y_points[i]=math.log(y_points[i])
        sum_of_x=sum(x_points)
        sum_of_y=sum(y_points)
        sum_of_x_square=0
        sum_of_x_y=0
        n=len(x_points)
        for i in range(len(x_points)):
            sum_of_x_square=sum_of_x_square+pow(x_points[i],2)
            sum_of_x_y=sum_of_x_y+x_points[i]*y_points[i]
        print(f"sum of x={sum_of_x}\nsum of y={sum_of_y}\nsum of x^2={sum_of_x_square}\nsum of xy={sum_of_x_y}")
        a0, a1 = symbols('a0 a1')
        eq1 = Eq(n * a0 + sum_of_x * a1 - sum_of_y,0)
        eq2 = Eq(sum_of_x * a0 + sum_of_x_square * a1 -sum_of_x_y,0)
        sol_dict = solve((eq1,eq2), (a0, a1))
        a0=sol_dict[a0]
        a1=sol_dict[a1]
        print(f'a0 = {a0}')
        print(f'a1 = {a1}')

        self.sr=0
        self.st=0
        mean_of_y=sum_of_y/len(y_points)
        a=pow(math.e,a0)
        b=a1
        for i in range(len(x_points)):
            self.sr=self.sr+pow((y_points[i]-a0-a1*x_points[i]),2)
            self.st=self.st+pow((y_points[i]-mean_of_y),2)
        i=x_points_global[0]
        self.x_fitted_weighted=[]
        self.y_fitted_weighted=[]
        while i<x_points_global[len(x_points_global)-1]:
            self.x_fitted_weighted.append(i)
            self.y_fitted_weighted.append((a*pow(math.e,b*i)))
            i+=0.01
        self.r_square=(self.st-self.sr)/self.st
        self.r=math.sqrt(self.r_square)
        self.sr_var.set(f"sr={round(self.sr,5)}")
        self.st_var.set(f"st={round(self.st,5)}")
        self.r_square_var.set(f"r^2={round(self.r_square,5)}")
        self.r_var.set(f"r={round(self.r,5)}")
        print(f"sr={self.sr}\nst={self.st}\nr^2={self.r_square}\nr={self.r}")






    def power_model(self):
        x_points=x_points_global.copy()
        y_points=y_points_global.copy()
        y_points_plot=y_points_global.copy()
        for i in range(len(y_points)):
            y_points[i]=math.log10(y_points[i])
            x_points[i]=math.log10(x_points[i])

        sum_of_x=sum(x_points)
        sum_of_y=sum(y_points)
        sum_of_x_square=0
        sum_of_x_y=0
        n=len(x_points)
        for i in range(len(x_points)):
            sum_of_x_square=sum_of_x_square+pow(x_points[i],2)
            sum_of_x_y=sum_of_x_y+x_points[i]*y_points[i]
        print(f"sum of x={sum_of_x}\nsum of y={sum_of_y}\nsum of x^2={sum_of_x_square}\nsum of xy={sum_of_x_y}")
        a0, a1 = symbols('a0 a1')
        eq1 = Eq(n * a0 + sum_of_x * a1 - sum_of_y,0)
        eq2 = Eq(sum_of_x * a0 + sum_of_x_square * a1 -sum_of_x_y,0)
        sol_dict = solve((eq1,eq2), (a0, a1))
        a0=sol_dict[a0]
        a1=sol_dict[a1]
        print(f'a0 = {pow(10,a0)}')
        print(f'a1 = {a1}')
        self.sr=0
        self.st=0
        mean_of_y=sum_of_y/len(y_points)
        a=pow(10,a0)
        b=a1
        for i in range(len(x_points)):
            self.sr=self.sr+pow((y_points[i]-a0-a1*x_points[i]),2)
            self.st=self.st+pow((y_points[i]-mean_of_y),2)

        i=x_points_global[0]
        self.x_fitted_weighted=[]
        self.y_fitted_weighted=[]
        while i<x_points_global[len(x_points_global)-1]:
            self.x_fitted_weighted.append(i)
            self.y_fitted_weighted.append((a*pow(i,b)))
            i+=0.01
        self.r_square=(self.st-self.sr)/self.st
        self.r=math.sqrt(self.r_square)
        self.sr_var.set(f"sr={round(self.sr,5)}")
        self.st_var.set(f"st={round(self.st,5)}")
        self.r_square_var.set(f"r^2={round(self.r_square,5)}")
        self.r_var.set(f"r={round(self.r,5)}")
        print(f"sr={self.sr}\nst={self.st}\nr^2={self.r_square}\nr={self.r}")





    def growth_model(self):
        x_points=x_points_global.copy()
        y_points=y_points_global.copy()
        for i in range(len(y_points)):
            y_points[i]=1/(y_points[i])
            x_points[i]=1/(x_points[i])
        sum_of_x=sum(x_points)
        sum_of_y=sum(y_points)
        sum_of_x_square=0
        sum_of_x_y=0
        n=len(x_points)
        for i in range(len(x_points)):
            sum_of_x_square=sum_of_x_square+pow(x_points[i],2)
            sum_of_x_y=sum_of_x_y+x_points[i]*y_points[i]
        print(f"sum of x={sum_of_x}\nsum of y={sum_of_y}\nsum of x^2={sum_of_x_square}\nsum of xy={sum_of_x_y}")
        a0, a1 = symbols('a0 a1')
        eq1 = Eq(n * a0 + sum_of_x * a1 - sum_of_y,0)
        eq2 = Eq(sum_of_x * a0 + sum_of_x_square * a1 -sum_of_x_y,0)
        sol_dict = solve((eq1,eq2), (a0, a1))
        a0=sol_dict[a0]
        a1=sol_dict[a1]
        print(f'a0 = {a0}')
        print(f'a1 = {a1}')
        self.sr=0
        self.st=0
        mean_of_y=sum_of_y/len(y_points)
        a=1/a0
        b=a1*a
        self.x_fitted_weighted=[]
        self.y_fitted_weighted=[]
        i=x_points_global[0]
        while i<x_points_global[len(x_points_global)-1]:
            self.x_fitted_weighted.append(i)
            self.y_fitted_weighted.append((a*i)/(b+i))
            i+=0.01
        for i in range(len(x_points)):
            self.sr=self.sr+pow((y_points[i]-a0-a1*x_points[i]),2)
            self.st=self.st+pow((y_points[i]-mean_of_y),2)
        self.r_square=(self.st-self.sr)/self.st
        self.r=math.sqrt(self.r_square)
        self.sr_var.set(f"sr={round(self.sr,5)}")
        self.st_var.set(f"st={round(self.st,5)}")
        self.r_square_var.set(f"r^2={round(self.r_square,5)}")
        self.r_var.set(f"r={round(self.r,5)}")
        print(f"sr={self.sr}\nst={self.st}\nr^2={self.r_square}\nr={self.r}")


    def print_points_entry(self,reset=False):
        myfont=tkfont.Font(family="ubuntu",size=10,weight="normal",slant="italic")
        myfont_large=tkfont.Font(family="ubuntu",size=14,weight="normal",slant="italic")
        x_entry=[]
        y_entry=[]
        def clear_points():
            for i in range(len(x_entry)):
                x_entry[i].destroy()
                y_entry[i].destroy()
            points_submit.destroy()
            points_reset.destroy()
        def submit_points():
            x_points_global.clear()
            y_points_global.clear()
            for i in range(len(x_entry)):
                x_points_global.append(float(x_entry[i].get()))
                y_points_global.append(float(y_entry[i].get()))
        if reset:clear_points()
        number_of_points=int(how_many_entry.get())
        for i in range(number_of_points):
            x_point=tk.Entry(root,width=5,font=myfont,bg="#FAF9F6")
            x_point.insert(0,f"x{i+1}")
            x_point.place(x=320+50*i,y=120)
            y_point=tk.Entry(root,width=5,font=myfont,bg="#FAF9F6")
            y_point.insert(0,f"y{i+1}")
            y_point.place(x=320+50*i,y=150)
            x_entry.append(x_point)
            y_entry.append(y_point)
        points_submit=tk.Button(root,text="Submit Points",command=lambda: [submit_points()],padx=25,font=myfont_large,background="white",fg="#000000")
        points_submit.grid(row=1,column=5,padx=10,pady=10)
        points_reset=tk.Button(root,text="Reset Points",command=lambda: [clear_points(),points_submit.destroy(),points_reset.destroy()],padx=25,font=myfont_large,background="white",fg="#000000")
        points_reset.grid(row=2,column=5,padx=10,pady=10)





    def linear_window(self,exponential=False,power=False,growth=False):
            myfont=tkfont.Font(family="ubuntu",size=14,weight="normal",slant="italic")
            self.sr_var=tk.StringVar()
            self.sr_var.set(f"sr={round(self.sr,5)}")
            sr_label=tk.Label(root,textvariable=self.sr_var,padx=25,font=myfont,width=14,background="white",fg="#000000").place(x=300,y=230)
            self.st_var=tk.StringVar()
            self.st_var.set(f"st={round(self.st,5)}")
            st_label=tk.Label(root,textvariable=self.st_var,padx=25,font=myfont,width=14,background="white",fg="#000000").place(x=550,y=230)
            self.r_square_var=tk.StringVar()
            self.r_square_var.set(f"r^2={round(self.r_square,5)}")
            r_square_label=tk.Label(root,textvariable=self.r_square_var,padx=25,font=myfont,width=14,background="white",fg="#000000").place(x=800,y=230)
            self.r_var=tk.StringVar()
            self.r_var.set(f"r={round(self.r,5)}")
            r_label=tk.Label(root,textvariable=self.r_var,padx=25,font=myfont,width=14,background="white",fg="#000000").place(x=1050,y=230)
            global how_many_entry
            how_many_entry=tk.Entry(root,font=myfont,background="white",fg="#000000")
            how_many_entry.grid(row=1,column=2,padx=10,pady=10)
            how_many_entry.insert(0,"Enter Number of Points")
            how_many_button=tk.Button(root,text="Submit",command=lambda: [self.print_points_entry()],font=myfont,background="white",fg="#000000",height=1,width=20).grid(row=1,column=3,padx=10,pady=10)
            if exponential==True:
                exp_reg_button=tk.Button(root,text="View Exponential Graph",command=lambda: [self.exponential_model(),self.plot()],font=myfont,background="white",fg="#000000"
                ,height=1,width=20).grid(row=1,column=4,padx=10,pady=10)
            elif power==True:
                power_reg_button=tk.Button(root,text="View Power Graph",command=lambda: [self.power_model(),self.plot()],font=myfont,background="white",fg="#000000"
                ,height=1,width=20).grid(row=1,column=4,padx=10,pady=10)
            elif growth==True:
                growth_reg_button=tk.Button(root,text="View Growth Graph",command=lambda: [self.growth_model(),self.plot()],font=myfont,background="white",fg="#000000"
                ,height=1,width=20).grid(row=1,column=4,padx=10,pady=10)
            else:
                linear_reg_button=tk.Button(root,text="View Linear Graph",command=lambda: [self.linear_regression(),self.plot()],font=myfont,background="white",fg="#000000"
                ,height=1,width=20).grid(row=1,column=4,padx=10,pady=10)
        
    def plot (self,mode=""):
        myfont=tkfont.Font(family="ubuntu",size=14,weight="normal",slant="italic")
        frame=tk.Frame(root)
        frame.place(x=50,y=300)
        if mode=="black":
            plt.style.use('dark_background')
        elif mode=="light":
            plt.style.use('default')
        fig, ax1 = plt.subplots(1,figsize=(5,5))
        fig.suptitle('Least Square Vs Data Points')
        ax1.plot(self.x_fitted_weighted, self.y_fitted_weighted,"r")
        ax1.plot(x_points_global, y_points_global,"b",linestyle="",marker="o")
        canvas = FigureCanvasTkAgg(fig, master=frame)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack()

        toolbar = NavigationToolbar2Tk(canvas, frame)
        toolbar.update()
        canvas.get_tk_widget().pack()
        light=tk.Button(master=root,text="Light Graph",font=myfont,background="white",fg="#000000",height=1,width=20,command=lambda:[self.plot(mode="light")]).place(x=650,y=500)
        dark=tk.Button(master=root,text="Dark Graph",font=myfont,background="#000000",fg="white",height=1,width=20,command=lambda:[self.plot(mode="black")]).place(x=650,y=550)








project=math_project()
root = tk.Tk()
def main_window():
    root.attributes('-fullscreen', True)
    myfont=tkfont.Font(family="ubuntu",size=14,weight="normal",slant="italic")
    myfont_xlarge=tkfont.Font(family="koulen",size=18,weight="normal",slant="italic")
    margin = tk.Label( root, text ="Computational Mathematics",background="white",fg="#000000",font=myfont_xlarge)
    margin.grid(row=0,column=0)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    bg = Image.open(os.path.join(script_dir, 'flower.jpg'))
    bg=bg.resize((root.winfo_screenwidth(),root.winfo_screenheight()), Image.ANTIALIAS)
    bg= ImageTk.PhotoImage(bg)
    # Show image using label
    label1 = tk.Label( root, image = bg)
    label1.place(x = -1,y = -1)


    regression_mode=tk.Button(text="Linear Regression Mode",font=myfont,command=lambda:[project.linear_window(),project.plot()],background="white",fg="#000000",height=1,width=20)
    regression_mode.grid(row=1,column=0,padx=10,pady=10)
    exponential_mode=tk.Button(text="Exponential Mode",font=myfont,command=lambda:[project.linear_window(exponential=True),project.plot()],background="white",fg="#000000",height=1,width=20)
    exponential_mode.grid(row=2,column=0,padx=10,pady=10)
    power_mode=tk.Button(text="Power Mode",font=myfont,command=lambda:[project.linear_window(power=True),project.plot()],background="white",fg="#000000",height=1,width=20)
    power_mode.grid(row=3,column=0,padx=10,pady=10)
    growth_mode=tk.Button(text="Growth Rate Mode",font=myfont,command=lambda:[project.linear_window(growth=True),project.plot()],background="white",fg="#000000",height=1,width=20)
    growth_mode.grid(row=4,column=0,padx=10,pady=10)
    
    exit_button=tk.Button(root,text="Exit",font=myfont,command=root.destroy,padx=20,pady=10,background="white",fg="#000000",height=1,width=20)
    exit_button.place(x=1250,y=800)
    


    root.mainloop()
main_window()



















