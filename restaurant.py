from cgitb import text
from pickle import FRAME
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

        #======================================fastfoodlist====================================================================================
        #======================================intvar==========================================================================================

        self.burger=IntVar
        self.pizza=IntVar
        self.pasta=IntVar
        self.pati=IntVar
        self.fries=IntVar
        self.sandwich=IntVar
        #============================================stringvar==================================================================================
        #========================================indian food list==================================================================================
        self.chholebhature=IntVar
        self.nan=IntVar
        self.biryani=IntVar
        self.dosa=IntVar
        self.idlisabhar=IntVar
        self.sahipaneer=IntVar

        #================================================cold drinks=============================================================================
        self.due=IntVar
        self.mazza=IntVar
        self.mrinda=IntVar
        self.butterscoth=IntVar
        self.choclate=IntVar
        self.vanila=IntVar

        #=============================================firstframe stringvar=====================================================================
        self.custumername=StringVar
        self.phoneno=StringVar
        self.billno=StringVar

        #=================================================6th frme stringvar===================================================================

        self.totalfastfoodprice=StringVar
        self.totalindianfoodprice=StringVar
        self.totalcolddrinksprice=StringVar
        self.fastfoodtax=StringVar
        self.indianfoodtax=StringVar
        self.colddrinkstax=StringVar







       

        #========================================customer detail frame======================================================================
        F1=LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_labl=Label(F1,text="Custumer Name",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        cname_labl.grid(row=0,column=0,padx=15,pady=5)
        cname_text=Entry(F1,width=20,font="arial 15 bold",relief=SUNKEN,textvariable=self.custumername)
        cname_text.grid(row=0,column=1,padx=5,pady=10)

        cname_labl=Label(F1,text="Phone NO",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        cname_labl.grid(row=0,column=2,padx=15,pady=5)
        cname_text=Entry(F1,width=20,font="arial 15 bold",relief=SUNKEN,textvariable=self.phoneno)
        cname_text.grid(row=0,column=3,padx=5,pady=10)

        cname_labl=Label(F1,text="Bill NO",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        cname_labl.grid(row=0,column=4,padx=15,pady=5)
        cname_text=Entry(F1,width=20,font="arial 15 bold",relief=SUNKEN,textvariable=self.billno)
        cname_text.grid(row=0,column=5,padx=5,pady=10)

        bill_btn=Button(F1,text="Search",width=10,bd=7,font="arial 12 bold")
        bill_btn.grid(row=0,column=6,padx=60,pady=10)

        #======================================================food list======================================================

        F2=LabelFrame(self.root,text="FAST FOOD LIST",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=0,y=180,width=325,height=328)

        item1=Label(F2,text="Burger",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item1.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        int1=Entry(F2,width=15,font="arial 11 bold",relief=SUNKEN,bd=3,textvariable=self.burger)
        int1.grid(row=0,column=1,padx=10,pady=10)

        item2=Label(F2,text="Pizza",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item2.grid(row=1,column=0,padx=10,pady=10,sticky="w")
        int1=Entry(F2,width=15,font="arial 11 bold",relief=SUNKEN,bd=3,textvariable=self.pizza)
        int1.grid(row=1,column=1,padx=10,pady=10)

        item3=Label(F2,text="Pasta",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item3.grid(row=2,column=0,padx=10,pady=10,sticky="w")
        int1=Entry(F2,width=15,font="arial 11 bold",relief=SUNKEN,bd=3,textvariable=self.pasta)
        int1.grid(row=2,column=1,padx=10,pady=10)

        item4=Label(F2,text="Pati",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item4.grid(row=3,column=0,padx=10,pady=10,sticky="w")
        int4=Entry(F2,width=15,font="arial 11 bold",relief=SUNKEN,bd=3,textvariable=self.pati)
        int4.grid(row=3,column=1,padx=10,pady=10)

        item5=Label(F2,text="Fries",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item5.grid(row=4,column=0,padx=10,pady=10,sticky="w")
        int5=Entry(F2,width=15,font="arial 11 bold",relief=SUNKEN,bd=3,textvariable=self.fries)
        int5.grid(row=4,column=1,padx=10,pady=10)

        item6=Label(F2,text="Sandwich",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item6.grid(row=5,column=0,padx=10,pady=10,sticky="w")
        int6=Entry(F2,width=15,font="arial 11 bold",relief=SUNKEN,bd=3,textvariable=self.sandwich)
        int6.grid(row=5,column=1,padx=10,pady=10)
        #======================================================food list======================================================
        F3=LabelFrame(self.root,text="INDIAN FOOD LIST",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=326,y=180,width=325,height=328)

        item7=Label(F3,text="Chhole bhatture",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item7.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        int7=Entry(F3,width=15,font="arial 11 bold",relief=SUNKEN,bd=3,textvariable=self.chholebhature)
        int7.grid(row=0,column=1,padx=10,pady=10)

        item8=Label(F3,text="Nan",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item8.grid(row=1,column=0,padx=10,pady=10,sticky="w")
        int8=Entry(F3,width=15,font="arial 11 bold",relief=SUNKEN,bd=3,textvariable=self.nan)
        int8.grid(row=1,column=1,padx=10,pady=10)

        item9=Label(F3,text="Biryani",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item9.grid(row=2,column=0,padx=10,pady=10,sticky="w")
        int9=Entry(F3,width=15,font="arial 11 bold",relief=SUNKEN,bd=3,textvariable=self.biryani)
        int9.grid(row=2,column=1,padx=10,pady=10)

        item10=Label(F3,text="Dosa",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item10.grid(row=3,column=0,padx=10,pady=10,sticky="w")
        int10=Entry(F3,width=15,font="arial 11 bold",relief=SUNKEN,bd=3,textvariable=self.dosa)
        int10.grid(row=3,column=1,padx=10,pady=10)

        item11=Label(F3,text="Idli sabhar",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item11.grid(row=4,column=0,padx=10,pady=10,sticky="w")
        int11=Entry(F3,width=15,font="arial 11 bold",relief=SUNKEN,bd=3,textvariable=self.idlisabhar)
        int11.grid(row=4,column=1,padx=10,pady=10)

        item12=Label(F3,text="sahi paneer",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item12.grid(row=5,column=0,padx=10,pady=10,sticky="w")
        int12=Entry(F3,width=15,font="arial 11 bold",relief=SUNKEN,bd=3,textvariable=self.sahipaneer)
        int12.grid(row=5,column=1,padx=10,pady=10)


        #======================================================food list======================================================
        F4=LabelFrame(self.root,text="ICECREAM/COLD DRINKS LIST",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=650,y=180,width=325,height=328)

        item13=Label(F4,text="Due",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item13.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        int13=Entry(F4,width=15,font="arial 11 bold",relief=SUNKEN,bd=3,textvariable=self.due)
        int13.grid(row=0,column=1,padx=10,pady=10)

        item14=Label(F4,text="Mazza",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item14.grid(row=1,column=0,padx=10,pady=10,sticky="w")
        int14=Entry(F4,width=15,font="arial 11 bold",relief=SUNKEN,bd=3,textvariable=self.mazza)
        int14.grid(row=1,column=1,padx=10,pady=10)

        item15=Label(F4,text="Mrinda",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item15.grid(row=2,column=0,padx=10,pady=10,sticky="w")
        int15=Entry(F4,width=15,font="arial 11 bold",relief=SUNKEN,bd=3,textvariable=self.mrinda)
        int15.grid(row=2,column=1,padx=10,pady=10)

        item16=Label(F4,text="Butterscoth",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item16.grid(row=3,column=0,padx=10,pady=10,sticky="w")
        int16=Entry(F4,width=15,font="arial 11 bold",relief=SUNKEN,bd=3,textvariable=self.butterscoth)
        int16.grid(row=3,column=1,padx=10,pady=10)

        item17=Label(F4,text="Choclate",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item17.grid(row=4,column=0,padx=10,pady=10,sticky="w")
        int17=Entry(F4,width=15,font="arial 11 bold",relief=SUNKEN,bd=3,textvariable=self.choclate)
        int17.grid(row=4,column=1,padx=10,pady=10)

        item18=Label(F4,text="Vanila",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        item18.grid(row=5,column=0,padx=10,pady=10,sticky="w")
        int18=Entry(F4,width=15,font="arial 11 bold",relief=SUNKEN,bd=3,textvariable=self.vanila)
        int18.grid(row=5,column=1,padx=10,pady=10)

        #=======================================BILL MENU=========================================================

        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=350,height=328)
        bill_title=Label(F5,text="Bill Area",font=("arial 15 bold"),bd=7,relief=GROOVE)
        bill_title.pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)


        #=======================================BUTTON FRAME =======================================================

        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)


        item19=Label(F6,text="Total Fastfood price",bg=bg_color,fg="white",font=("times new roman",14,"bold"))
        item19.grid(row=0,column=0,padx=10,pady=5,sticky="w")
        int19=Entry(F6,width=12,font="arial 10 bold",relief=SUNKEN,bd=3,textvariable=self.totalfastfoodprice)
        int19.grid(row=0,column=1,padx=10,pady=5)

        item20=Label(F6,text="Total indianfood price ",bg=bg_color,fg="white",font=("times new roman",14,"bold"))
        item20.grid(row=1,column=0,padx=10,pady=5,sticky="w")
        int20=Entry(F6,width=12,font="arial 10 bold",relief=SUNKEN,bd=3,textvariable=self.totalindianfoodprice)
        int20.grid(row=1,column=1,padx=10,pady=5)

        item21=Label(F6,text="Total Colddrinks price",bg=bg_color,fg="white",font=("times new roman",14,"bold"))
        item21.grid(row=2,column=0,padx=10,pady=5,sticky="w")
        int21=Entry(F6,width=12,font="arial 10 bold",relief=SUNKEN,bd=3,textvariable=self.totalcolddrinksprice)
        int21.grid(row=2,column=1,padx=10,pady=5)

        item22=Label(F6,text="Fastfood Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold"))
        item22.grid(row=0,column=2,padx=10,pady=5,sticky="w")
        int22=Entry(F6,width=12,font="arial 10 bold",relief=SUNKEN,bd=3,textvariable=self.fastfoodtax)
        int22.grid(row=0,column=3,padx=10,pady=5)

        item23=Label(F6,text="Indianfood Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold"))
        item23.grid(row=1,column=2,padx=10,pady=5,sticky="w")
        int23=Entry(F6,width=12,font="arial 10 bold",relief=SUNKEN,bd=3,textvariable=self.indianfoodtax)
        int23.grid(row=1,column=3,padx=10,pady=5)

        item24=Label(F6,text="Colddrinks Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold"))
        item24.grid(row=2,column=2,padx=10,pady=5,sticky="w")
        int24=Entry(F6,width=12,font="arial 10 bold",relief=SUNKEN,bd=3,textvariable=self.colddrinkstax)
        int24.grid(row=2,column=3,padx=10,pady=5)

        #====================================buttons=================================================================

        


        btn_f=Frame(F6,bd=7,relief=GROOVE)
        btn_f.place(x=650,width=680,height=105)

        
        total_btn=Button(btn_f,text="Total",bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial 15 bold",command=self.total)
        total_btn.grid(row=0,column=0,padx=5,pady=5)

        gbill_btn=Button(btn_f,text="Genrate Bill",bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial 15 bold")
        gbill_btn.grid(row=0,column=1,padx=5,pady=5)

        clear_btn=Button(btn_f,text="Clear",bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial 15 bold")
        clear_btn.grid(row=0,column=2,padx=5,pady=5)

        exit_btn=Button(btn_f,text="Exit",bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial 15 bold")
        exit_btn.grid(row=0,column=3,padx=5,pady=5)


    def total(self):
        self.total_fast_food_price=float((self.burger.get()*40)+(self.pizza.get()*149)+(self.pasta.get()*149)+(self.pati.get()*15)
                                  +(self.fries.get()*70)+(self.sandwich.get()*49))
        self.totalfastfoodprice.set("RS  "+str(self.total_fastfood_price))

        
        self.total_indian_food_price=float((self.chholebhature.get())+(self.nan.get()*20)
                                  +(self.biryani.get()*70)+(self.dosa.get()*120)+(self.idlisabhar.get()*70)+(self.sahipaneer.get()*120))
        self.totalindianfoodprice.set("RS  "+str(self.total_indian_food_price)) 

        self.total_cold_drinks_price=float((self.due.get()*80)+(self.mazza.get()*60)+(self.mrinda.get()*60)+(self.butterscoth.get()*30)
                                  +(self.choclate.get()*30)+(self.vanila.get()*30))
        self.totalcolddrinksprice.set("RS  "+str(self.total_cold_drinks_price))

                                     
                                        






root=Tk()
obj=Bill_App(root)
root.mainloop()