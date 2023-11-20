from tkinter import *
import subprocess as sp
import sqlite3
#from persiantools.jdatetime import JalaliDate
import jdatetime




class DataBase:
    
    def __init__(self,table,window):
        self.table=table
        self.window=window
        
        self.window.title('اطلاعات تعمیرات')
        self.window.geometry('1350x1000+0+0')
        self.window.configure(background='powder blue')
        mainFrame=Frame(self.window)
        mainFrame.pack()
        topFrame=Frame(mainFrame,width=900,height=70,borderwidth=2,relief=SUNKEN,padx=20,bg='powder blue')
        topFrame.pack(side=TOP,fill=X)
        centerFrame=Frame(mainFrame,width=900,height=800,relief=RIDGE)
        centerFrame.pack(side=TOP)
        leftFrame=Frame(centerFrame,width=300,height=700,borderwidth=2,relief=SUNKEN)
        leftFrame.pack(side=LEFT)
        rightFrame=Frame(centerFrame,width=600,height=700,borderwidth=2,relief=SUNKEN,bg='powder blue')
        rightFrame.pack(side=RIGHT)
        self.scroll_bar=Scrollbar(rightFrame)
        self.scroll_bar.pack(fill=Y,side=RIGHT)


        self.btn_exit=Button(topFrame,text='خروج',padx=40,bg='white smoke',font='arial 12 bold',command=self.close,bd=5)
        self.btn_exit.pack(side=LEFT)
        self.btn_help=Button(topFrame,text='جایگذاری در فیلد',padx=40,font='arial 12 bold',bd=5,bg='powderblue',command=self.insert_selection)
        self.btn_help.pack(side=LEFT)
        self.btn_balance=Button(topFrame,text='تیپاکس',padx=40,bg='white smoke',font='arial 12 bold',command=self.tipax,bd=5)
        self.btn_balance.pack(side=LEFT)
        self.btn_order=Button(topFrame,text='انتقال به نوت پد',padx=40,font='arial 12 bold',bd=5,bg='powderblue',command=self.get_selection)
        self.btn_order.pack(side=LEFT)
        self.btn_search=Button(topFrame,text=' جست و جو',padx=40,bg='white smoke',font='arial 12 bold',command=self.search,bd=5)
        self.btn_search.pack(side=LEFT)
        self.btn_delete=Button(topFrame,text='حذف',padx=40,font='arial 12 bold',command=self.delete,bd=5,bg='powderblue')
        self.btn_delete.pack(side=LEFT)
        self.btn_update=Button(topFrame,text='ویرایش',padx=40,font='arial 12 bold',command=self.update,bg='white smoke',bd=5)
        self.btn_update.pack(side=LEFT)
        self.btn_show=Button(topFrame,text=' نمایش',padx=40,font='arial 12 bold',command=self.show,bd=5,bg='powderblue')
        self.btn_show.pack(side=LEFT)
        self.btn_add=Button(topFrame,text='اضافه',padx=40,font='arial 12 bold',command=self.add,bg='white smoke',bd=5)
        self.btn_add.pack(side=LEFT)
        title=LabelFrame(leftFrame,text='بخش خدمات پس از فروش طراحان نوین مدار',labelanchor='n',font='arial 30 bold',bg='green2',bd=10)
        title.pack(fill=BOTH)
        fields_bar=LabelFrame(leftFrame,width=300,height=75,text='فیلدها',font='arial 20 bold',bg='yellow2',bd=10)
        fields_bar.pack(fill=BOTH)

        self.lbl_title=Label(title,text='تهران نوین تک',pady=20,bg='green2',bd=5,font='arial 30 bold')
        self.lbl_title.pack(fill=BOTH)
        self.lbl_title=Label(title,text=' سیاوش برسرخی:09126173521',bg='green2',bd=5,font='arial 20 bold')
        self.lbl_title.pack(fill=BOTH)
        self.lbl_row=Label(fields_bar,text=' ردیف: ',font='arial 14 bold',bg='powderblue')
        self.lbl_row.grid(row=0,column=0)
        self.ent_row=Entry(fields_bar,bd=10,font=50)
        
        self.ent_row.grid(row=0,column=1)
        self.lbl_bs=Label(fields_bar,text=' سریال جعبه: ',font='arial 14 bold',bg='powderblue')
        self.lbl_bs.grid(row=1,column=0)
        self.ent_bs=Entry(fields_bar,bd=10,font=50)
        self.ent_bs.grid(row=1,column=1)
        
        self.lbl_ps=Label(fields_bar,text='سریال PCB: ',font='arial 14 bold',bg='powderblue')
        self.lbl_ps.grid(row=2,column=0)
        self.ent_ps=Entry(fields_bar,bd=10,font=50)
        self.ent_ps.grid(row=2,column=1)
        
        self.lbl_id=Label(fields_bar,text=' تاریخ ورود: ',font='arial 14 bold',bg='powderblue')
        self.lbl_id.grid(row=3,column=0)
        self.ent_id=Entry(fields_bar,bd=10,font=50)
        self.ent_id.insert(0,jdatetime.date.today())
        self.ent_id.grid(row=3,column=1)
        
        self.lbl_ed=Label(fields_bar,text=' تاریخ خروج: ',font='arial 14 bold',bg='powderblue')
        self.lbl_ed.grid(row=4,column=0)
        self.ent_ed=Entry(fields_bar,bd=10,font=50)
        self.ent_ed.insert(0,jdatetime.date.today())
        self.ent_ed.grid(row=4,column=1)
        
        self.lbl_cc=Label(fields_bar,text='  هزینه قطعات: ',font='arial 14 bold',bg='powderblue')
        self.lbl_cc.grid(row=5,column=0)
        self.ent_cc=Entry(fields_bar,bd=10,font=50)
        self.ent_cc.grid(row=5,column=1)
        
        
        self.lbl_rc=Label(fields_bar,text='هزینه تعمیر: ',font='arial 14 bold',bg='powderblue')
        self.lbl_rc.grid(row=6,column=0)
        self.ent_rc=Entry(fields_bar,bd=10,font=50)
        self.ent_rc.grid(row=6,column=1)
        
        
        self.lbl_tc=Label(fields_bar,text='کد فعال سازی: ',font='arial 14 bold',bg='powderblue')
        self.lbl_tc.grid(row=7,column=0)
        self.ent_tc=Entry(fields_bar,bd=10,font=50)
        self.ent_tc.grid(row=7,column=1)
        
        
        self.lbl_sc=Label(fields_bar,text='هزینه سرویس: ',font='arial 14 bold',bg='powderblue')
        self.lbl_sc.grid(row=0,column=2)
        self.ent_sc=Entry(fields_bar,bd=10,font=50)
        self.ent_sc.grid(row=0,column=3)
        self.lbl_on=Label(fields_bar,text='نام مالک دستگاه: ',font='arial 14 bold',bg='powderblue')
        self.lbl_on.grid(row=1,column=2)
        self.ent_on=Entry(fields_bar,bd=10,font=50)
        self.ent_on.grid(row=1,column=3)
        self.lbl_nc=Label(fields_bar,text='کد ملی: ',font='arial 14 bold',bg='powderblue')
        self.lbl_nc.grid(row=2,column=2)
        self.ent_nc=Entry(fields_bar,bd=10,font=50)
        self.ent_nc.grid(row=2,column=3)
        self.lbl_ad=Label(fields_bar,text='آدرس: ',font='arial 14 bold',bg='powderblue')
        self.lbl_ad.grid(row=3,column=2)
        self.ent_ad=Entry(fields_bar,bd=10,font=50)
        self.ent_ad.grid(row=3,column=3)
        self.lbl_ph=Label(fields_bar,text='شماره موبایل: ',font='arial 14 bold',bg='powderblue')
        self.lbl_ph.grid(row=4,column=2)
        self.ent_ph=Entry(fields_bar,bd=10,font=50)
        self.ent_ph.grid(row=4,column=3)
        self.lbl_dm=Label(fields_bar,text='مدل دستگاه: ',font='arial 14 bold',bg='powderblue')
        self.lbl_dm.grid(row=5,column=2)
        self.ent_dm=Entry(fields_bar,bd=10,font=50)
        self.ent_dm.grid(row=5,column=3)
        self.lbl_rd=Label(fields_bar,text='شرح تعمیر: ',font='arial 14 bold',bg='powderblue')
        self.lbl_rd.grid(row=6,column=2)
        self.ent_rd=Entry(fields_bar,bd=10,font=50)
        self.ent_rd.grid(row=6,column=3)
        self.lbl_opt=Label(fields_bar,text='OPT: ',font='arial 14 bold',bg='powderblue')
        self.lbl_opt.grid(row=7,column=2)
        self.ent_opt=Entry(fields_bar,bd=10,font=50)
        self.ent_opt.grid(row=7,column=3)
        
        self.lt=Listbox(rightFrame,height=700,width=800,fg='blue',font='arial 13 bold',bd=10,yscrollcommand=self.scroll_bar.set,selectmode=MULTIPLE)
        self.lt.pack(padx=20,pady=20,fill=BOTH)
        self.scroll_bar.config(command=self.lt.yview)
        self.btn_clr_ent=Button(leftFrame,text='پاک کردن فیلد ها',font='arial 14 bold',bg='yellow2',command=self.clr_ent,bd=10)
        self.btn_clr_ent.pack(side=LEFT)        
        self.btn_clr=Button(leftFrame,text='پاک کردن صفحه نمایش',font='arial 14 bold',bg='powder blue',command=self.clr_box,bd=10)
        self.btn_clr.pack(side=LEFT)
        self.btn_clr=Button(leftFrame,text='ردیف و تاریخ پیشنهادی',font='arial 14 bold',bg='white smoke',command=self.rowDate_offer,bd=10)
        self.btn_clr.pack(side=LEFT)

    def insert_selection(self):
        
        row=''
        bs=''
        ps=''
        id=''
        ed=''
        cc=''
        rc=''
        tc=''
        sc=''
        on=''
        nc=''
        ad=''
        ph=''
        dm=''
        
        rd=''
        opt=''
        
        lst=['A','D','R','E','S',':','O','M','B','I','L','N','K',' ','H','G','T','F','J','P','C','H','V','-','Z','F']
              
        for i in self.lt.curselection():
            word=''
            for j in self.lt.get(i):
                
                if j!=':':
                    word+=j
                else:
                    break
                
            for j in self.lt.get(i):
                if word=='RADIF' and j not in lst:
                    self.ent_row.delete(0,END)
                    row+=j
                elif word=='SERIAL JABE' and j not in lst:
                    self.ent_bs.delete(0,END)
                    bs+=j 
                elif word=='SERIAL PCB' and j not in lst:
                    self.ent_ps.delete(0,END)
                    ps+=j 
                elif word=='TARIKH VOROD' and j not in lst:
                    self.ent_id.delete(0,END)
                    id+=j 
                elif word=='TARIKH KHOROJ' and j not in lst:
                    self.ent_ed.delete(0,END)
                    ed+=j 
                elif word=='HAZINE GHATE' and j not in lst:
                    self.ent_cc.delete(0,END)
                    cc+=j 
                elif word=='HAZINE TAMIR' and j not in lst:
                    self.ent_rc.delete(0,END)
                    rc+=j 
                elif word=='CODE FAAL-SAZI' and j not in lst:
                    self.ent_tc.delete(0,END)
                    tc+=j 
                elif word=='HAZINE SERVICE' and j not in lst:
                    self.ent_sc.delete(0,END)
                    sc+=j 
                elif word=='NAME MALEK DASTGAH' and j not in lst:
                    self.ent_on.delete(0,END)
                    on+=j 
                elif word=='CODE MELLI' and j not in lst:
                    self.ent_nc.delete(0,END)
                    nc+=j 
                elif word=='ADDRESS' and j not in lst:
                    self.ent_ad.delete(0,END)
                    ad+=j 
                elif word=='SHOMARE MOBILE' and j not in lst:
                    self.ent_ph.delete(0,END)
                    ph+=j 
                elif word=='MODEL DASTGAH' and j not in lst:
                    self.ent_dm.delete(0,END)
                    dm+=j 
                elif word=='SHARHE TAMIR' and j not in lst:
                    self.ent_rd.delete(0,END)
                    rd+=j 
                elif word=='OPT' and j not in lst:
                    self.ent_opt.delete(0,END)
                    opt+=j 
                       
                          

                    
        self.ent_row.insert(0,row)                    
        self.ent_bs.insert(0,bs)                    
        self.ent_ps.insert(0,ps)                    
        self.ent_id.insert(0,id)                    
        self.ent_ed.insert(0,ed)                    
        self.ent_cc.insert(0,cc)                    
        self.ent_rc.insert(0,rc)                    
        self.ent_tc.insert(0,tc)                    
        self.ent_sc.insert(0,sc)                    
        self.ent_on.insert(0,on)                    
        self.ent_nc.insert(0,nc)                    
        self.ent_ad.insert(0,ad)                    
        self.ent_ph.insert(0,ph)                    
        self.ent_rd.insert(0,rd)                    
        self.ent_dm.insert(0,dm)                    
        self.ent_opt.insert(0,opt)                    
         
       
    def tipax(self):
        
        

        if self.ent_row.get()!='':
         self.clr_box()
         db=sqlite3.connect('dataBase.db')
         cr=db.cursor() 
         cr.execute(f'select * from {self.table}')
         rows=cr.fetchall()
         lst_rows=[]
         for i in rows:
            lst_rows.append(f'{i[0]}')
            


         if len(rows)==0:
            self.lt.insert(0,'جدول خالی است')
         else:
            count=0
            
            lst_fields=[self.ent_row.get(),self.ent_bs.get(),self.ent_ps.get(),self.ent_id.get(),self.ent_ed.get(),self.ent_cc.get(),self.ent_rc.get(),self.ent_tc.get(),self.ent_sc.get(),self.ent_on.get(),self.ent_nc.get(),self.ent_ad.get(),self.ent_ph.get(),self.ent_dm.get(),self.ent_rd.get(),self.ent_opt.get()]
            
            for i in lst_fields:
                if i!='':
                    count+=1
            if  count!=1:
                self.lt.insert(0,'فقط ردیف را پر کنید')       
            elif self.ent_row.get().lower() not in lst_rows:
                self.lt.insert(0,'ردیف یافت نشد')
            else:
                cr.execute(f'select * from {self.table} where ROW="{self.ent_row.get().lower()}"')
                db.commit()
                rows=cr.fetchall()
                
                text=rows[0][11]+'-'+rows[0][9]+'-'+rows[0][12]
                sp.Popen(['notepad', "fields.txt"])  
                file=open('fields.txt','w',encoding="utf-16-le")
                file.write(' فرستنده:تهران-خیابان آزادی-بین نواب و اسکندری-جنب بانک تجارت-ساختمان پانامال-طبقه ششم-واحد 610-شرکت طراحان نوین مدار-02165010001-09126173521'+'\n')
                file.write('\n')
                file.write('گیرنده:'+text)
                file.close()
        elif self.ent_on.get()!='' and self.ent_ph.get()!='' and self.ent_ad.get()!='':
                sp.Popen(['notepad', "fields.txt"])  
                file=open('fields.txt','w',encoding="utf-16-le")
                file.write(' فرستنده:تهران-خیابان آزادی-بین نواب و اسکندری-جنب بانک تجارت-ساختمان پانامال-طبقه ششم-واحد 610-شرکت طراحان نوین مدار-02165010001-09126173521'+'\n')
                file.write('\n')
                file.write('گیرنده:'+self.ent_ad.get()+'-'+self.ent_on.get()+'-'+self.ent_ph.get())
                file.close()
                    
        else:  
         lst=['A','D','R','E','S',':','O','M','B','I','L','N','K',' ','H','G','T']
         sp.Popen(['notepad', "fields.txt"])   
         file=open('fields.txt','w',encoding="utf-16-le")
         
         file.write(' فرستنده:تهران-خیابان آزادی-بین نواب و اسکندری-جنب بانک تجارت-ساختمان پانامال-طبقه ششم-واحد 610-شرکت طراحان نوین مدار-02165010001-09126173521'+'\n')      
         ph=''
         name=''
     
         add=''
        
      
        
         for i in self.lt.curselection():
            count=0
            for j in self.lt.get(i):
                if j=='D':
                    count+=1
            for j in self.lt.get(i):
                if j not in lst and count==2:
                    add+=j
                elif j not in lst and count==1:
                    name+=j
                elif j not in lst and count==0:
                    ph+=j
         file.write('\n')           
         file.write('گیرنده:'+add+'-'+name+'-'+ph)            
         file.close()  
                        

            

            


            
                    
        

        
        
        
        
            
    def rowDate_offer(self):
        db=sqlite3.connect('dataBase.db')
        cr=db.cursor() 
        cr.execute(f'select ROW from {self.table}')
        
        rows=cr.fetchall()
        if len(rows)==0:
            last_row=1
        else:
                
            last_row=int(rows[-1][0])+1 
        self.ent_row.delete(0,END)
        self.ent_id.delete(0,END)
        self.ent_ed.delete(0,END)
        self.ent_row.insert(0,last_row)
        self.ent_id.insert(0,jdatetime.date.today())
        self.ent_ed.insert(0,jdatetime.date.today())

      

    def get_selection(self):
        sp.Popen(['notepad', "fields.txt"])
        file=open('fields.txt','w',encoding="utf-16-le")
        fields=''
        for i in self.lt.curselection():
            fields+=self.lt.get(i)+'\n'
        file.write(fields)
        file.close()       
        
    def connect(self):
        db=sqlite3.connect('dataBase.db')
        cr=db.cursor()
        cr.execute(f'create table if not exists {self.table}(ROW int,BS varchar(80),PS varchar(80),ID varchar(80),ED varchar(80),CC varchar(80),RC varchar(80),TC varchar(80),SC varchar(80),NF varchar(80),NC varchar(80),AD varchar(80),PH varchar(80),DM varchar(80),RD varchar(80),OPT varchar(80))')
        cr.execute(f'select ROW from {self.table}')
        
        rows=cr.fetchall()
        if len(rows)==0:
            last_row=1
        else:
                
            last_row=int(rows[-1][0])+1 
        self.ent_row.insert(0,last_row)
    def show(self):
        self.clr_box()
        db=sqlite3.connect('dataBase.db')
        cr=db.cursor() 
        cr.execute(f'select * from {self.table}')
        rows=cr.fetchall()
        if len(rows)==0:
            self.lt.insert(0,'جدول خالی است')
        else:
            index=0
            lst=['RADIF','SERIAL JABE','SERIAL PCB','TARIKH VOROD','TARIKH KHOROJ','HAZINE GHATE','HAZINE TAMIR','CODE FAAL-SAZI','HAZINE SERVICE','NAME MALEK DASTGAH','CODE MELLI','ADDRESS','SHOMARE MOBILE','MODEL DASTGAH','SHARHE TAMIR','OPT']
            for i in rows:
                counter=0
                for j in i:
                 if 'س' in str(j) and 'ر' in str(j) and 'ق' in str(j) and 'ت' in str(j):
                        
                         if str(j[0])=='س' and str(j[1])=='ر' and str(j[2])=='ق' and str(j[3])=='ت':
                             
                             
                             self.lt.insert(index,f'{lst[counter]}:{j}')
                             
                             self.lt.itemconfig(index,foreground='red')
                         else:
                             self.lt.insert(index,f'{lst[counter]}:{j}') 
                 else:
                     self.lt.insert(index,f'{lst[counter]}:{j}')     
                 counter+=1 
                 index+=1  
                index=0 
                self.lt.insert(index,'--------------------------------------------------')    

    def add(self):
        self.clr_box()
        db=sqlite3.connect('dataBase.db')
        cr=db.cursor()
        cr.execute(f'select * from {self.table}')
        rows=cr.fetchall()
        if self.ent_row.get()=='' or self.ent_bs.get()=='' or self.ent_ps.get()=='' or self.ent_id.get()=='' or self.ent_ed.get()=='' or self.ent_cc.get()=='' or self.ent_rc.get()=='' or self.ent_tc.get()=='' or self.ent_sc.get()=='' or self.ent_on.get()=='' or self.ent_nc.get()=='' or self.ent_ad.get()=='' or self.ent_ph.get()=='' or self.ent_dm.get()=='' or self.ent_rd.get()=='' or self.ent_opt.get()=='':
            
            self.lt.insert(0,'تمامی فیلد ها پر شود')
        else:
                
         for i in rows:
            
            if self.ent_row.get().lower() ==  f'{i[0]}':
                self.lt.insert(0,'این ردیف وارد شده است')
                break

         else:
            cr.execute(f'insert into {self.table} values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(self.ent_row.get().lower(),self.ent_bs.get().lower(),self.ent_ps.get().lower(),self.ent_id.get().lower(),self.ent_ed.get().lower(),self.ent_cc.get().lower(),self.ent_rc.get().lower(),self.ent_tc.get().lower(),self.ent_sc.get().lower(),self.ent_on.get().lower(),self.ent_nc.get().lower(),self.ent_ad.get().lower(),self.ent_ph.get().lower(),self.ent_dm.get().lower(),self.ent_rd.get().lower(),self.ent_opt.get().lower()))
            
            db.commit()   
            self.lt.insert(0,'فیلد ها اضافه شدند')
            cr.execute(f'select ROW from {self.table}')
        
            rows=cr.fetchall()
            last_row=int(rows[-1][0])+1 
            self.ent_row.delete(0,END)
            self.ent_bs.delete(0,END)
            self.ent_ps.delete(0,END)
            self.ent_cc.delete(0,END)
            self.ent_rc.delete(0,END)
            self.ent_tc.delete(0,END)
            self.ent_sc.delete(0,END)
            self.ent_on.delete(0,END)
            self.ent_nc.delete(0,END)
            self.ent_ad.delete(0,END)
            self.ent_ph.delete(0,END)
            self.ent_dm.delete(0,END)
            self.ent_rd.delete(0,END)
            self.ent_opt.delete(0,END)
            self.ent_row.insert(0,last_row) 
     

    def clr_box(self):
        self.lt.delete(0,END)            
    def clr_ent(self):
        self.ent_row.delete(0,END)
        self.ent_bs.delete(0,END)
        self.ent_ps.delete(0,END)
        self.ent_id.delete(0,END)
        self.ent_ed.delete(0,END)
        self.ent_cc.delete(0,END)
        self.ent_rc.delete(0,END)
        self.ent_tc.delete(0,END)
        self.ent_sc.delete(0,END)
        self.ent_on.delete(0,END)
        self.ent_nc.delete(0,END)
        self.ent_ad.delete(0,END)
        self.ent_ph.delete(0,END)
        self.ent_dm.delete(0,END)
        self.ent_rd.delete(0,END)
        self.ent_opt.delete(0,END)
    def update(self):
        self.clr_box()
        db=sqlite3.connect('dataBase.db')
        cr=db.cursor() 
        cr.execute(f'select * from {self.table}')
        rows=cr.fetchall()
        lst_rows=[]
        for i in rows:
            lst_rows.append(f'{i[0]}')
            


        if len(rows)==0:
            self.lt.insert(0,'جدول خالی است')
        else:
            count=0
            
            lst_fields=[self.ent_row.get(),self.ent_bs.get(),self.ent_ps.get(),self.ent_id.get(),self.ent_ed.get(),self.ent_cc.get(),self.ent_rc.get(),self.ent_tc.get(),self.ent_sc.get(),self.ent_on.get(),self.ent_nc.get(),self.ent_ad.get(),self.ent_ph.get(),self.ent_dm.get(),self.ent_rd.get(),self.ent_opt.get()]
            
            for i in lst_fields:
                if i!='':
                    count+=1
            if  self.ent_row.get()=='' or count!=2:
                self.lt.insert(0,'فقط فیلد ردیف و فیلدی را که خواهان تغیر آن هستید وارد کنید')       
            elif self.ent_row.get().lower() not in lst_rows:
                self.lt.insert(0,'ردیف یافت نشد')
            else:
                if self.ent_bs.get()!='':
                    cr.execute(f'update {self.table} set  BS="{self.ent_bs.get().lower()}" where ROW="{self.ent_row.get().lower()}"')
                    db.commit()
                    self.lt.insert(0,'عملیات ویرایش با موفقیت انجام شد')              
                elif self.ent_ps.get()!='':
                    cr.execute(f'update {self.table} set  PS="{self.ent_ps.get().lower()}" where ROW="{self.ent_row.get().lower()}"')
                    db.commit()
                    self.lt.insert(0,'عملیات ویرایش با موفقیت انجام شد')              
                elif self.ent_id.get()!='':
                    cr.execute(f'update {self.table} set  ID="{self.ent_id.get().lower()}" where ROW="{self.ent_row.get().lower()}"')
                    db.commit()
                    self.lt.insert(0,'عملیات ویرایش با موفقیت انجام شد')              
                elif self.ent_ed.get()!='':
                    cr.execute(f'update {self.table} set  ED="{self.ent_ed.get().lower()}" where ROW="{self.ent_row.get().lower()}"')
                    db.commit()
                    self.lt.insert(0,'عملیات ویرایش با موفقیت انجام شد')              
                elif self.ent_cc.get()!='':
                    cr.execute(f'update {self.table} set  CC="{self.ent_cc.get().lower()}" where ROW="{self.ent_row.get().lower()}"')
                    db.commit()
                    self.lt.insert(0,'عملیات ویرایش با موفقیت انجام شد')              
                elif self.ent_rc.get()!='':
                    cr.execute(f'update {self.table} set  RC="{self.ent_rc.get().lower()}" where ROW="{self.ent_row.get().lower()}"')
                    db.commit()
                    self.lt.insert(0,'عملیات ویرایش با موفقیت انجام شد')              
                elif self.ent_tc.get()!='':
                    cr.execute(f'update {self.table} set  TC="{self.ent_tc.get().lower()}" where ROW="{self.ent_row.get().lower()}"')
                    db.commit()
                    self.lt.insert(0,'عملیات ویرایش با موفقیت انجام شد')              
                elif self.ent_sc.get()!='':
                    cr.execute(f'update {self.table} set  SC="{self.ent_sc.get().lower()}" where ROW="{self.ent_row.get().lower()}"')
                    db.commit()
                    self.lt.insert(0,'عملیات ویرایش با موفقیت انجام شد')              
                elif self.ent_on.get()!='':
                    cr.execute(f'update {self.table} set  NF="{self.ent_on.get().lower()}" where ROW="{self.ent_row.get().lower()}"')
                    db.commit()
                    self.lt.insert(0,'عملیات ویرایش با موفقیت انجام شد')              
                elif self.ent_nc.get()!='':
                    cr.execute(f'update {self.table} set  NC="{self.ent_nc.get().lower()}" where ROW="{self.ent_row.get().lower()}"')
                    db.commit()
                    self.lt.insert(0,'عملیات ویرایش با موفقیت انجام شد')              
                elif self.ent_ad.get()!='':
                    cr.execute(f'update {self.table} set  AD="{self.ent_ad.get().lower()}" where ROW="{self.ent_row.get().lower()}"')
                    db.commit()
                    self.lt.insert(0,'عملیات ویرایش با موفقیت انجام شد')              
                elif self.ent_ph.get()!='':
                    cr.execute(f'update {self.table} set  PH="{self.ent_ph.get().lower()}" where ROW="{self.ent_row.get().lower()}"')
                    db.commit()
                    self.lt.insert(0,'عملیات ویرایش با موفقیت انجام شد')              
                elif self.ent_dm.get()!='':
                    cr.execute(f'update {self.table} set  DM="{self.ent_dm.get().lower()}" where ROW="{self.ent_row.get().lower()}"')
                    db.commit()
                    self.lt.insert(0,'عملیات ویرایش با موفقیت انجام شد')              
                elif self.ent_rd.get()!='':
                    cr.execute(f'update {self.table} set  RD="{self.ent_rd.get().lower()}" where ROW="{self.ent_row.get().lower()}"')
                    db.commit()
                    self.lt.insert(0,'عملیات ویرایش با موفقیت انجام شد')              

                elif self.ent_opt.get()!='':
                    cr.execute(f'update {self.table} set  OPT="{self.ent_opt.get().lower()}" where ROW="{self.ent_row.get().lower()}"')
                    db.commit()
                    self.lt.insert(0,'عملیات ویرایش با موفقیت انجام شد')   

    def delete(self):
        self.clr_box()
        db=sqlite3.connect('dataBase.db')
        cr=db.cursor() 
        cr.execute(f'select * from {self.table}')
        rows=cr.fetchall()
        lst_rows=[]
        lst_bs=[]
        lst_ps=[]
        lst_id=[]
        lst_ed=[]
        lst_cc=[]
        lst_rc=[]
        lst_tc=[]
        lst_sc=[]
        lst_on=[]
        lst_nc=[]
        lst_ad=[]
        lst_ph=[]
        lst_dm=[]
        lst_rd=[]
        lst_opt=[]
        
        for i in rows:
            lst_rows.append(f'{i[0]}')
            lst_bs.append(f'{i[1]}')
            lst_ps.append(f'{i[2]}')
            lst_id.append(f'{i[3]}')
            lst_ed.append(f'{i[4]}')
            lst_cc.append(f'{i[5]}')
            lst_rc.append(f'{i[6]}')
            lst_tc.append(f'{i[7]}')
            lst_sc.append(f'{i[8]}')
            lst_on.append(f'{i[9]}')
            lst_nc.append(f'{i[10]}')
            lst_ad.append(f'{i[11]}')
            lst_ph.append(f'{i[12]}')
            lst_dm.append(f'{i[13]}')
            lst_rd.append(f'{i[14]}')
            lst_opt.append(f'{i[15]}')
            


        if len(rows)==0:
            self.lt.insert(0,'جدول خالی است')
            
        else:
            count=0
            lst_fields=[self.ent_row.get(),self.ent_bs.get(),self.ent_ps.get(),self.ent_id.get(),self.ent_ed.get(),self.ent_cc.get(),self.ent_rc.get(),self.ent_tc.get(),self.ent_sc.get(),self.ent_on.get(),self.ent_nc.get(),self.ent_ad.get(),self.ent_ph.get(),self.ent_dm.get(),self.ent_rd.get(),self.ent_opt.get()]
            for i in lst_fields:
                if i=='':
                    count+=1
            if count==len(lst_fields):
                self.lt.insert(0,'حداقل یک فیلد باید پر شود')        
            elif   self.ent_row.get().lower() not in lst_rows and self.ent_bs.get().lower() not in lst_bs and self.ent_ps.get().lower() not in lst_ps and self.ent_id.get().lower() not in lst_id and self.ent_ed.get().lower() not in lst_ed and self.ent_cc.get().lower() not in lst_cc and self.ent_rc.get().lower() not in lst_rc and self.ent_tc.get().lower() not in lst_tc and self.ent_sc.get().lower() not in lst_sc and self.ent_on.get().lower() not in lst_on and self.ent_nc.get().lower() not in lst_nc and self.ent_ad.get().lower() not in lst_ad and self.ent_ph.get().lower() not in lst_ph and self.ent_dm.get().lower() not in lst_dm and self.ent_rd.get().lower() not in lst_rd and self.ent_opt.get().lower() not in lst_opt:
                self.lt.insert(0,'مقداری یافت نشد')
            else:
                cr.execute(f'delete from {self.table} where ROW="{self.ent_row.get().lower()}" or BS="{self.ent_bs.get().lower()}" or PS="{self.ent_ps.get().lower()}" or ID="{self.ent_id.get().lower()}" or ED="{self.ent_ed.get().lower()}" or CC="{self.ent_cc.get().lower()}" or RC="{self.ent_rc.get().lower()}" or TC="{self.ent_tc.get().lower()}" or SC="{self.ent_sc.get().lower()}" or NF="{self.ent_on.get().lower()}" or NC="{self.ent_nc.get().lower()}" or AD="{self.ent_ad.get().lower()}" or PH="{self.ent_ph.get().lower()}" or DM="{self.ent_dm.get().lower()}" or RD="{self.ent_rd.get().lower()}" or OPT="{self.ent_opt.get().lower()}"')
                db.commit()
                self.lt.insert(0,'فیلد های مورد نظر حذف شدند')
                    
                

    def search(self):
        self.clr_box()
        db=sqlite3.connect('dataBase.db')
        cr=db.cursor() 
        cr.execute(f'select * from {self.table}')
        rows=cr.fetchall()
        lst_rows=[]
        lst_bs=[]
        lst_ps=[]
        lst_id=[]
        lst_ed=[]
        lst_cc=[]
        lst_rc=[]
        lst_tc=[]
        lst_sc=[]
        lst_on=[]
        lst_nc=[]
        lst_ad=[]
        lst_ph=[]
        lst_dm=[]
        lst_rd=[]
        lst_opt=[]        
        
        for i in rows:
            lst_rows.append(f'{i[0]}')
            lst_bs.append(f'{i[1]}')
            lst_ps.append(f'{i[2]}')
            lst_id.append(f'{i[3]}')
            lst_ed.append(f'{i[4]}')
            lst_cc.append(f'{i[5]}')
            lst_rc.append(f'{i[6]}')
            lst_tc.append(f'{i[7]}')
            lst_sc.append(f'{i[8]}')
            lst_on.append(f'{i[9]}')
            lst_nc.append(f'{i[10]}')
            lst_ad.append(f'{i[11]}')
            lst_ph.append(f'{i[12]}')
            lst_dm.append(f'{i[13]}')
            lst_rd.append(f'{i[14]}')

            lst_opt.append(f'{i[15]}')           


        if len(rows)==0:
            self.lt.insert(0,'جدول خالی است')
        else:
            count=0
            lst_fields=[self.ent_row.get(),self.ent_bs.get(),self.ent_ps.get(),self.ent_id.get(),self.ent_ed.get(),self.ent_cc.get(),self.ent_rc.get(),self.ent_tc.get(),self.ent_sc.get(),self.ent_on.get(),self.ent_nc.get(),self.ent_ad.get(),self.ent_ph.get(),self.ent_dm.get(),self.ent_rd.get(),self.ent_opt.get()]
            for i in lst_fields:
                if i=='':
                    count+=1
            if count==len(lst_fields):
                self.lt.insert(0,'حداقل یک فیلد باید پر شود')        
            elif   self.ent_row.get().lower() not in lst_rows and self.ent_bs.get().lower() not in lst_bs and self.ent_ps.get().lower() not in lst_ps and self.ent_id.get().lower() not in lst_id and self.ent_ed.get().lower() not in lst_ed and self.ent_cc.get().lower() not in lst_cc and self.ent_rc.get().lower() not in lst_rc and self.ent_tc.get().lower() not in lst_tc and self.ent_sc.get().lower() not in lst_sc and self.ent_on.get().lower() not in lst_on and self.ent_nc.get().lower() not in lst_nc and self.ent_ad.get().lower() not in lst_ad and self.ent_ph.get().lower() not in lst_ph and self.ent_dm.get().lower() not in lst_dm and self.ent_rd.get().lower() not in lst_rd and self.ent_opt.get().lower() not in lst_opt:
                self.lt.insert(0,'مقداری یافت نشد')
            else:
                 cr.execute(f'select * from {self.table} where ROW="{self.ent_row.get().lower()}" or BS="{self.ent_bs.get().lower()}" or PS="{self.ent_ps.get().lower()}" or ID="{self.ent_id.get().lower()}" or ED="{self.ent_ed.get().lower()}" or CC="{self.ent_cc.get().lower()}" or RC="{self.ent_rc.get().lower()}" or TC="{self.ent_tc.get().lower()}" or SC="{self.ent_sc.get().lower()}" or NF="{self.ent_on.get().lower()}" or NC="{self.ent_nc.get().lower()}" or AD="{self.ent_ad.get().lower()}" or PH="{self.ent_ph.get().lower()}" or DM="{self.ent_dm.get().lower()}" or RD="{self.ent_rd.get().lower()}" or OPT="{self.ent_opt.get().lower()}"')
                 db.commit()
                 rows=cr.fetchall()
                 index=0
                 
                 lst=['RADIF','SERIAL JABE','SERIAL PCB','TARIKH VOROD','TARIKH KHOROJ','HAZINE GHATE','HAZINE TAMIR','CODE FAAL-SAZI','HAZINE SERVICE','NAME MALEK DASTGAH','CODE MELLI','ADDRESS','SHOMARE MOBILE','MODEL DASTGAH','SHARHE TAMIR','OPT']
                 for i in rows:
                    counter=0
                    for j in i:
                     
                     if 'س' in str(j) and 'ر' in str(j) and 'ق' in str(j) and 'ت' in str(j):
                         if str(j[0])=='س' and str(j[1])=='ر' and str(j[2])=='ق' and str(j[3])=='ت':
                             
                             
                             self.lt.insert(index,f'{lst[counter]}:{j}')
                             
                             self.lt.itemconfig(index,foreground='red')
                         else:
                             self.lt.insert(index,f'{lst[counter]}:{j}')        
                     else:
                         self.lt.insert(index,f'{lst[counter]}:{j}') 
                     counter+=1 
                     index+=1  
                    index=0 
                    self.lt.insert(index,'--------------------------------------------------')                       
                
                        
            


                





    def close(self):
        self.window.destroy()
if __name__=='__main__':
    
    window=Tk()
    device=DataBase('DEVICE',window)
    device.connect()
    device.lt.insert(0,'پایگاه داده متصل است')
    

    
    window.mainloop()
        
            
