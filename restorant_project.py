from tkinter import *
from turtle import bgcolor, title

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074478"
        title=Label(self.root,text="Billing Software",font=("times new roman",30,"bold"),bd=12,relief=GROOVE,pady=2,bg=bg_color,fg="white")
        title.pack(fill=X)
        

        #========================================customer detail frame======================================================================
        F1=LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_labl=Label(F1,text="Custumer Name",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        cname_labl.grid(row=0,column=0,padx=15,pady=5)
        cname_text=Entry(F1,width=20,font="arial 15 bold",relief=SUNKEN)
        cname_text.grid(row=0,column=1,padx=5,pady=10)

        cname_labl=Label(F1,text="Phone NO",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        cname_labl.grid(row=0,column=2,padx=15,pady=5)
        cname_text=Entry(F1,width=20,font="arial 15 bold",relief=SUNKEN)
        cname_text.grid(row=0,column=3,padx=5,pady=10)

        cname_labl=Label(F1,text="Bill NO",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        cname_labl.grid(row=0,column=4,padx=15,pady=5)
        cname_text=Entry(F1,width=20,font="arial 15 bold",relief=SUNKEN)
        cname_text.grid(row=0,column=5,padx=5,pady=10)

        bill_btn=Button(F1,text="Search",width=10,bd=7,font="arial 12 bold")
        bill_btn.grid(row=0,column=6,padx=60,pady=10)

        #======================================================food list======================================================

        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="FOOD LIST",font="times new roman,15,bold",bg=bg_color,fg="gold")
        F2.place(x=5,y=180,width=900,height=328)











root=Tk()
obj=Bill_App(root)
root.mainloop()
