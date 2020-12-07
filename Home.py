import tkinter as tk
from tkinter import Message ,Text
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import tkinter.messagebox as tm
import sqlite3

from tkinter import filedialog
import tkinter.messagebox as tm
from tkinter import ttk
import createdatasets as cd
import LogisticRegression as LR
import NeuralNetwork as NN
import singlequery as single

def Main():
	global window
	bgcolor="#ECFDB0"
	fgcolor="black"
	window = tk.Tk()
	window.title("Authorship Attribution")

	window.geometry('1280x720')
	window.configure(background=bgcolor)
	#window.attributes('-fullscreen', True)
	
	window.grid_rowconfigure(0, weight=1)
	window.grid_columnconfigure(0, weight=1)

	message1 = tk.Label(window, text="Authorship Attribution" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
	message1.place(x=100, y=10)

	lbl = tk.Label(window, text="Select Dataset",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl.place(x=10, y=200)

	txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt.place(x=300, y=215)
	
	lbl1 = tk.Label(window, text="Query",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl1.place(x=10, y=300)

	txt1 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt1.place(x=300, y=315)
	
	lbl4 = tk.Label(window, text="Notification : ",width=20  ,fg=fgcolor,bg=bgcolor  ,height=2 ,font=('times', 15, ' bold underline ')) 
	lbl4.place(x=10, y=500)
	
	message = tk.Label(window, text="" ,bg="white"  ,fg="black",width=30  ,height=2, activebackground = bgcolor ,font=('times', 15, ' bold ')) 
	message.place(x=300, y=500)
	
	def submit():
		res = ""
		message.configure(text= res)

		sym=txt.get()
		sym1=txt1.get()
		if sym != "" and sym1 !="":
			q=[]
			q.append(sym1)
			res=single.process(sym,q)
			print(sym,sym1)
			message.configure(text= res)

		else:
			tm.showinfo("Input error", "Select Dataset and Enter Query")

	def browse():
		res = ""
		message.configure(text= res)

		path=filedialog.askopenfilename()
		print(path)
		txt.insert('end',path)
		if path !="":
			print(path)
		else:
			tm.showinfo("Input error", "Select Dataset")	
			res = "Select Dataset"
			message.configure(text= res)
	def createdataset():
		res = ""
		message.configure(text= res)
		cd.process()
		tm.showinfo("Input", "Created Dataset Successfully")
		res = "Created Dataset Successfully"
		message.configure(text= res)

	def nnet():
		sym=txt.get()
		if sym != "":
			res = ""
			message.configure(text= res)
			NN.process(sym)
			tm.showinfo("Input", "Neural Network finished Successfully")
			res = "Neural Network finished Successfully"
			message.configure(text= res)

		else:
			tm.showinfo("Input error", "Select Dataset")
			res = "Select Dataset"
			message.configure(text= res)

	def logreg():
		sym=txt.get()
		if sym != "":
			res = ""
			message.configure(text= res)
			LR.process(sym)
			tm.showinfo("Input", "Logistic Regression Finished Successfully")
			res = "Logistic Regression Finished Successfully"
			message.configure(text= res)

		else:
			tm.showinfo("Input error", "Select Dataset")
			#res = "Select Dataset"
			#message.configure(text= res)
		
		
	def logout():
		window.destroy()
		Home()
		
	clearButton = tk.Button(window, text="Submit", command=submit  ,fg=fgcolor  ,bg=bgcolor  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
	clearButton.place(x=760, y=600)
	
	browse = tk.Button(window, text="Browse", command=browse  ,fg=fgcolor  ,bg=bgcolor  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	browse.place(x=530, y=205)
	
	pre = tk.Button(window, text="Create Dataset", command=createdataset  ,fg=fgcolor  ,bg=bgcolor  ,width=18  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	pre.place(x=10, y=600)

	texta = tk.Button(window, text="Logistic Regression", command=logreg  ,fg=fgcolor ,bg=bgcolor  ,width=18  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	texta.place(x=260, y=600)
	
	pred = tk.Button(window, text="Neural Network", command=nnet  ,fg=fgcolor,bg=bgcolor  ,width=18  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	pred.place(x=520, y=600)
	
	#qr = tk.Button(window, text="Query", command=query  ,fg=fgcolor ,bg=bgcolor  ,width=18  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	#qr.place(x=780, y=600)
	

	quitWindow = tk.Button(window, text="Logout", command=logout  ,fg=fgcolor ,bg=bgcolor  ,width=18  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	quitWindow.place(x=1020, y=600)
	
 
	window.mainloop()



def Home():
	global window
	bgcolor="#ECFDB0"
	fgcolor="black"
	window = tk.Tk()
	window.title("Authorship Attribution")
	window.geometry('1280x720')
	window.configure(background=bgcolor)
	#window.attributes('-fullscreen', True)

	window.grid_rowconfigure(0, weight=1)
	window.grid_columnconfigure(0, weight=1)

	def login():
		print("Login")
		window.destroy()
		Login()
		
	def home():
		print("Home")
		window.destroy()
		Home()

	def signup():
		print("Signup")
		window.destroy()
		Signup()
	
	message1 = tk.Label(window, text="Authorship Attribution" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
	message1.place(x=100, y=10)		
    
	#message2 = tk.Label(window, text="Content Here dddddddddddddddd" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
	#message2.place(x=50, y=250)		
    

	home = tk.Button(window, text="Home", command=home  ,fg=fgcolor  ,bg=bgcolor  ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	home.place(x=140, y=120)

	signup = tk.Button(window, text="Signup", command=signup  ,fg=fgcolor  ,bg=bgcolor ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	signup.place(x=340, y=120)

 
	login = tk.Button(window, text="Login", command=login  ,fg=fgcolor  ,bg=bgcolor  ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	login.place(x=540, y=120)

	quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor  ,bg=bgcolor ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	quitWindow.place(x=740, y=120)



	
	text1 = Text(window, height=10, width=20)
	image = Image.open('images/Alcott.jpg')
	photo = ImageTk.PhotoImage(image)
	text1.insert('end','\n')
	text1.image_create('end', image=photo)
	
	text1.place(x=20, y=180)
	
	text2 = Text(window, height=10, width=50)
	scroll = tk.Scrollbar(window, command=text2.yview)
	text2.configure(yscrollcommand=scroll.set)
	text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
	text2.tag_configure('big', font=('Verdana', 20, 'bold'))
	text2.tag_configure('color', foreground='#476042',font=('Tempus Sans ITC', 12, 'bold'))
	text2.insert('end','\nAlcott\n', 'big')
	quote = """
	"Christmas won't be Christmas without any presents," grumbled Jo, lying	on the rug.
	"It's so dreadful to be poor!" sighed Meg, looking down at her old dress.
	"I don't think it's fair for some girls to have plenty of pretty things, and other girls nothing at all," added little Amy, with an injured sniff.
	"We've got Father and Mother, and each other," said Beth contentedly from her corner.
	"""
	text2.insert('end', quote, 'color')
	text2.place(x=190, y=180)
	#scroll.pack(side=RIGHT, fill=Y)

	text3 = Text(window, height=10, width=20)
	image1 = Image.open('images/Twain.jpg')
	photo1 = ImageTk.PhotoImage(image1)
	text3.insert('end','\n')
	text3.image_create('end', image=photo1)
	
	text3.place(x=600, y=180)
	
	text4 = Text(window, height=10, width=50)
	scroll = tk.Scrollbar(window, command=text4.yview)
	text4.configure(yscrollcommand=scroll.set)
	text4.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
	text4.tag_configure('big', font=('Verdana', 20, 'bold'))
	text4.tag_configure('color', foreground='#476042',font=('Tempus Sans ITC', 12, 'bold'))
	text4.insert('end','\nTwain\n', 'big')
	quote = """
	
	The old lady pulled her spectacles down and looked over them about the
	room; then she put them up and looked out under them. She seldom or
	never looked _through_ them for so small a thing as a boy; they were
	her state pair, the pride of her heart, and were built for style, not
	service--she could have seen through a pair of stove-lids just as well.
	She looked perplexed for a moment, and then said, not fiercely, but
	still loud enough for the furniture to hear:
	
	Well, I lay if I get hold of you I'll--

	"""
	text4.insert('end', quote, 'color')
	text4.place(x=770, y=180)
	#scroll.pack(side=RIGHT, fill=Y)

	text5 = Text(window, height=10, width=20)
	image2 = Image.open('images/Collins.jpg')
	photo2 = ImageTk.PhotoImage(image2)
	text5.insert('end','\n')
	text5.image_create('end', image=photo2)
	
	text5.place(x=20, y=350)
	
	text6 = Text(window, height=10, width=50)
	scroll = tk.Scrollbar(window, command=text2.yview)
	text6.configure(yscrollcommand=scroll.set)
	text6.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
	text6.tag_configure('big', font=('Verdana', 20, 'bold'))
	text6.tag_configure('color', foreground='#476042',font=('Tempus Sans ITC', 12, 'bold'))
	text6.insert('end','\nCollins\n', 'big')
	quote = """
	This is the story of what a Woman's patience can endure, and what a
	Man's resolution can achieve.
	
	If the machinery of the Law could be depended on to fathom every case
	of suspicion, and to conduct every process of inquiry, with moderate
	assistance only from the lubricating influences of oil of gold, the
	events which fill these pages might have claimed their share of the
	public attention in a Court of Justice.
	
	
	"""
	text6.insert('end', quote, 'color')
	text6.place(x=190, y=350)
	#scroll.pack(side=RIGHT, fill=Y)

	text7 = Text(window, height=10, width=20)
	image3 = Image.open('images/Doyle.png')
	photo3 = ImageTk.PhotoImage(image3)
	text7.insert('end','\n')
	text7.image_create('end', image=photo3)
	
	text7.place(x=600, y=350)
	
	text8 = Text(window, height=10, width=50)
	scroll = tk.Scrollbar(window, command=text4.yview)
	text8.configure(yscrollcommand=scroll.set)
	text8.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
	text8.tag_configure('big', font=('Verdana', 20, 'bold'))
	text8.tag_configure('color', foreground='#476042',font=('Tempus Sans ITC', 12, 'bold'))
	text8.insert('end','\nDoyle\n', 'big')
	quote = """
	IN the year 1878 I took my degree of Doctor of Medicine of the
	University of London, and proceeded to Netley to go through the course
	prescribed for surgeons in the army. Having completed my studies there,
	I was duly attached to the Fifth Northumberland Fusiliers as Assistant
	Surgeon. The regiment was stationed in India at the time, and before
	I could join it, the second Afghan war had broken out. On landing at
	Bombay, I learned that my corps had advanced through the passes, and
	was already deep in the enemys country. I followed, however, with many
	other officers who were in the same situation as myself, and succeeded
	in reaching Candahar in safety, where I found my regiment, and at once
	entered upon my new duties.


	"""
	text8.insert('end', quote, 'color')
	text8.place(x=770, y=350)
	#scroll.pack(side=RIGHT, fill=Y)

	text9 = Text(window, height=10, width=20)
	image4 = Image.open('images/Stoker.jpg')
	photo4 = ImageTk.PhotoImage(image4)
	text9.insert('end','\n')
	text9.image_create('end', image=photo4)
	
	text9.place(x=20, y=520)
	
	text10 = Text(window, height=10, width=50)
	scroll = tk.Scrollbar(window, command=text2.yview)
	text10.configure(yscrollcommand=scroll.set)
	text10.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
	text10.tag_configure('big', font=('Verdana', 20, 'bold'))
	text10.tag_configure('color', foreground='#476042',font=('Tempus Sans ITC', 12, 'bold'))
	text10.insert('end','\nStoker\n', 'big')
	quote = """
	_3 May. Bistritz._--Left Munich at 8:35 P. M., on 1st May, arriving at
	Vienna early next morning; should have arrived at 6:46, but train was an
	hour late. Buda-Pesth seems a wonderful place, from the glimpse which I
	got of it from the train and the little I could walk through the
	streets. I feared to go very far from the station, as we had arrived
	late and would start as near the correct time as possible. The
	impression I had was that we were leaving the West and entering the
	East; the most western of splendid bridges over the Danube, which is
	here of noble width and depth, took us among the traditions of Turkish
	rule.

	"""
	text10.insert('end', quote, 'color')
	text10.place(x=190, y=520)
	#scroll.pack(side=RIGHT, fill=Y)

	text11 = Text(window, height=10, width=20)
	image5 = Image.open('images/Montgomery.jpg')
	photo5 = ImageTk.PhotoImage(image5)
	text11.insert('end','\n')
	text11.image_create('end', image=photo5)
	
	text11.place(x=600, y=520)
	
	text12 = Text(window, height=10, width=50)
	scroll = tk.Scrollbar(window, command=text4.yview)
	text12.configure(yscrollcommand=scroll.set)
	text12.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
	text12.tag_configure('big', font=('Verdana', 20, 'bold'))
	text12.tag_configure('color', foreground='#476042',font=('Tempus Sans ITC', 12, 'bold'))
	text12.insert('end','\nMontgomery\n', 'big')
	quote = """
	MRS. Rachel Lynde lived just where the Avonlea main road dipped down
	into a little hollow, fringed with alders and ladies eardrops and
	traversed by a brook that had its source away back in the woods of the
	old Cuthbert place; it was reputed to be an intricate, headlong brook
	in its earlier course through those woods, with dark secrets of pool
	and cascade; but by the time it reached Lynde's Hollow it was a quiet,
	well-conducted little stream, for not even a brook could run past Mrs.
	Rachel Lynde's door without due regard for decency and decorum; it
	probably was conscious that Mrs. Rachel was sitting at her window,
	keeping a sharp eye on everything that passed, from brooks and children
	up, and that if she noticed anything odd or out of place she would never
	rest until she had ferreted out the whys and wherefores thereof.

	"""
	text12.insert('end', quote, 'color')
	text12.place(x=770, y=520)
	#scroll.pack(side=RIGHT, fill=Y)


	window.mainloop()


def Login():
	global window
	bgcolor="#ECFDB0"
	fgcolor="black"
	window = tk.Tk()
	window.title("Authorship Attribution")
	window.geometry('1280x720')
	window.configure(background=bgcolor)
	#window.attributes('-fullscreen', True)

	window.grid_rowconfigure(0, weight=1)
	window.grid_columnconfigure(0, weight=1)

		
	message1 = tk.Label(window, text="Authorship Attribution" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
	message1.place(x=100, y=10)		
    
	#message2 = tk.Label(window, text="Content Here dddddddddddddddd" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
	#message2.place(x=50, y=250)		
    
	def login():
		print("Login")
		window.destroy()
		Login()	
	def home():
		print("Home")
		window.destroy()
		Home()

	def signup():
		print("Signup")
		window.destroy()
		Signup()

	def submit():
		print("submit")
		sym=txt.get()
		sym1=txt1.get()
		if sym != "" and sym1 != "":
			conn= sqlite3.connect("Author")
			cmd="SELECT username,password FROM login WHERE username='"+str(sym)+"' and password='"+str(sym1)+"'"
			print(cmd)
			cursor=conn.execute(cmd)
			
			isRecordExist=0
			for row in cursor:
				isRecordExist=1
			if(isRecordExist==1):
			        #cmd="UPDATE student SET Name='"+str(name)+"',Mobile='"+mob+"' WHERE ID="+str(Id)
			        tm.showinfo("Input", "Lgoin Succesfully")
			        window.destroy()
			        Main()
			else:
				tm.showinfo("Input", "Check Username and Password")
		else:
			tm.showinfo("Input error", "Enter UserName And Password")
	
	home = tk.Button(window, text="Home", command=home  ,fg=fgcolor  ,bg=bgcolor  ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	home.place(x=140, y=150)

	signup = tk.Button(window, text="Signup", command=signup  ,fg=fgcolor  ,bg=bgcolor ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	signup.place(x=340, y=150)

 
	login = tk.Button(window, text="Login", command=login  ,fg=fgcolor  ,bg=bgcolor  ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	login.place(x=540, y=150)

	quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor  ,bg=bgcolor ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	quitWindow.place(x=740, y=150)
	
	lbl = tk.Label(window, text="User Name",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl.place(x=300, y=300)
	
	txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt.place(x=600, y=315)

	lbl1 = tk.Label(window, text="Password",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl1.place(x=300, y=400)
	
	txt1 = tk.Entry(window,show="*",width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt1.place(x=600, y=415)

	submit = tk.Button(window, text="Submit", command=submit  ,fg=fgcolor  ,bg=bgcolor  ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	submit.place(x=600, y=550)
	
	window.mainloop()
def Signup():
	global window
	bgcolor="#ECFDB0"
	fgcolor="black"
	window = tk.Tk()
	window.title("Authorship Attribution")
	window.geometry('1280x720')
	window.configure(background=bgcolor)
	#window.attributes('-fullscreen', True)

	window.grid_rowconfigure(0, weight=1)
	window.grid_columnconfigure(0, weight=1)

		
	message1 = tk.Label(window, text="Authorship Attribution" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
	message1.place(x=100, y=10)		
    
	#message2 = tk.Label(window, text="Content Here dddddddddddddddd" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
	#message2.place(x=50, y=250)		
    
	def login():
		print("Login")
		window.destroy()
		Login()	
	def home():
		print("Home")
		window.destroy()
		Home()

	def signup():
		print("Signup")
		window.destroy()
		Signup()

	def submit():
		print("submit")
		sym=txt.get()
		sym1=txt1.get()
		sym2=txt2.get()
		sym3=txt3.get()
		if sym != "" and sym1 != "" and sym2 != "" and sym3 != "":
			conn= sqlite3.connect("Author")
			cmd="SELECT * FROM login WHERE username='"+str(sym)+"'"
			print(cmd)
			cursor=conn.execute(cmd)
			isRecordExist=0
			for row in cursor:
				isRecordExist=1
			if(isRecordExist==1):
			        #cmd="UPDATE student SET Name='"+str(name)+"',Mobile='"+mob+"' WHERE ID="+str(Id)
			        tm.showinfo("Input", "Username Already Exists")
			else:
				print("insert")
				cmd="INSERT INTO login Values('"+str(sym)+"','"+str(sym1)+"','"+str(sym2)+"','"+str(sym3)+"')"
				print(cmd)
				tm.showinfo("Input","Inserted Successfully")
			conn.execute(cmd)
			conn.commit()
			conn.close() 

			
		else:
			tm.showinfo("Input error", "Enter UserName And Password")
	
	home = tk.Button(window, text="Home", command=home  ,fg=fgcolor  ,bg=bgcolor  ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	home.place(x=140, y=150)

	signup = tk.Button(window, text="Signup", command=signup  ,fg=fgcolor  ,bg=bgcolor ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	signup.place(x=340, y=150)

 
	login = tk.Button(window, text="Login", command=login  ,fg=fgcolor  ,bg=bgcolor  ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	login.place(x=540, y=150)

	quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor  ,bg=bgcolor ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	quitWindow.place(x=740, y=150)
	
	lbl = tk.Label(window, text="User Name",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl.place(x=300, y=250)
	
	txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt.place(x=600, y=265)

	lbl1 = tk.Label(window, text="Password",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl1.place(x=300, y=300)
	
	txt1 = tk.Entry(window,show="*",width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt1.place(x=600, y=315)

	lbl2 = tk.Label(window, text="Name",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl2.place(x=300, y=350)
	
	txt2 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt2.place(x=600, y=365)

	lbl3 = tk.Label(window, text="Email",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl3.place(x=300, y=400)
	
	txt3 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt3.place(x=600, y=415)

	submit = tk.Button(window, text="Submit", command=submit  ,fg=fgcolor  ,bg=bgcolor  ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	submit.place(x=600, y=550)
	
	window.mainloop()
	
Home()