from cgitb import text
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

        F2=LabelFrame(self.root,text="FAST FOOD LIST",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=0,y=180,width=325,height=328)

        item1=Label(F2,text="Burger",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item1.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        int1=Entry(F2,width=15,font="arial 11 bold",relief=SUNKEN,bd=3)
        int1.grid(row=0,column=1,padx=10,pady=10)

        item2=Label(F2,text="Pizza",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item2.grid(row=1,column=0,padx=10,pady=10,sticky="w")
        int1=Entry(F2,width=15,font="arial 11 bold",relief=SUNKEN,bd=3)
        int1.grid(row=1,column=1,padx=10,pady=10)

        item3=Label(F2,text="Pasta",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item3.grid(row=2,column=0,padx=10,pady=10,sticky="w")
        int1=Entry(F2,width=15,font="arial 11 bold",relief=SUNKEN,bd=3)
        int1.grid(row=2,column=1,padx=10,pady=10)

        item4=Label(F2,text="Pati",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item4.grid(row=3,column=0,padx=10,pady=10,sticky="w")
        int4=Entry(F2,width=15,font="arial 11 bold",relief=SUNKEN,bd=3)
        int4.grid(row=3,column=1,padx=10,pady=10)

        item5=Label(F2,text="Fries",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item5.grid(row=4,column=0,padx=10,pady=10,sticky="w")
        int5=Entry(F2,width=15,font="arial 11 bold",relief=SUNKEN,bd=3)
        int5.grid(row=4,column=1,padx=10,pady=10)

        item6=Label(F2,text="Sandwich",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item6.grid(row=5,column=0,padx=10,pady=10,sticky="w")
        int6=Entry(F2,width=15,font="arial 11 bold",relief=SUNKEN,bd=3)
        int6.grid(row=5,column=1,padx=10,pady=10)
        #======================================================food list======================================================
        F3=LabelFrame(self.root,text="INDIAN FOOD LIST",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=326,y=180,width=325,height=328)

        item7=Label(F3,text="Chhole bhatture",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item7.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        int7=Entry(F3,width=15,font="arial 11 bold",relief=SUNKEN,bd=3)
        int7.grid(row=0,column=1,padx=10,pady=10)

        item8=Label(F3,text="Nan",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item8.grid(row=1,column=0,padx=10,pady=10,sticky="w")
        int8=Entry(F3,width=15,font="arial 11 bold",relief=SUNKEN,bd=3)
        int8.grid(row=1,column=1,padx=10,pady=10)

        item9=Label(F3,text="Biryani",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item9.grid(row=2,column=0,padx=10,pady=10,sticky="w")
        int9=Entry(F3,width=15,font="arial 11 bold",relief=SUNKEN,bd=3)
        int9.grid(row=2,column=1,padx=10,pady=10)

        item10=Label(F3,text="Dosa",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item10.grid(row=3,column=0,padx=10,pady=10,sticky="w")
        int10=Entry(F3,width=15,font="arial 11 bold",relief=SUNKEN,bd=3)
        int10.grid(row=3,column=1,padx=10,pady=10)

        item11=Label(F3,text="Idli sabhar",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item11.grid(row=4,column=0,padx=10,pady=10,sticky="w")
        int11=Entry(F3,width=15,font="arial 11 bold",relief=SUNKEN,bd=3)
        int11.grid(row=4,column=1,padx=10,pady=10)

        item12=Label(F3,text="sahi paneer",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item12.grid(row=5,column=0,padx=10,pady=10,sticky="w")
        int12=Entry(F3,width=15,font="arial 11 bold",relief=SUNKEN,bd=3)
        int12.grid(row=5,column=1,padx=10,pady=10)


        #======================================================food list======================================================
        F4=LabelFrame(self.root,text="ICECREAM/COLD DRINKS LIST",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=650,y=180,width=325,height=328)

        item13=Label(F4,text="Due",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item13.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        int13=Entry(F4,width=15,font="arial 11 bold",relief=SUNKEN,bd=3)
        int13.grid(row=0,column=1,padx=10,pady=10)

        item14=Label(F4,text="Mazza",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item14.grid(row=1,column=0,padx=10,pady=10,sticky="w")
        int14=Entry(F4,width=15,font="arial 11 bold",relief=SUNKEN,bd=3)
        int14.grid(row=1,column=1,padx=10,pady=10)

        item15=Label(F4,text="Mrinda",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item15.grid(row=2,column=0,padx=10,pady=10,sticky="w")
        int15=Entry(F4,width=15,font="arial 11 bold",relief=SUNKEN,bd=3)
        int15.grid(row=2,column=1,padx=10,pady=10)

        item16=Label(F4,text="Butterscoth",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item16.grid(row=3,column=0,padx=10,pady=10,sticky="w")
        int16=Entry(F4,width=15,font="arial 11 bold",relief=SUNKEN,bd=3)
        int16.grid(row=3,column=1,padx=10,pady=10)

        item17=Label(F4,text="Choclate",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item17.grid(row=4,column=0,padx=10,pady=10,sticky="w")
        int17=Entry(F4,width=15,font="arial 11 bold",relief=SUNKEN,bd=3)
        int17.grid(row=4,column=1,padx=10,pady=10)

        item18=Label(F4,text="Vanila",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item18.grid(row=5,column=0,padx=10,pady=10,sticky="w")
        int18=Entry(F4,width=15,font="arial 11 bold",relief=SUNKEN,bd=3)
        int18.grid(row=5,column=1,padx=10,pady=10)

        #=======================================BILL MENU=========================================================

        F5=LabelFrame(self.root,text="Bill Menu",bd=10,relief=GROOVE,font="times new roman,15,bold")
        F5.place(x=0,y=560,relwidth=1350,height=140)















root=Tk()
obj=Bill_App(root)
root.mainloop()