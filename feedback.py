
from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
class Feedback:

	def __init__(self,root):
		root.title('Feedback')
		root.resizable(False,False)
		root.configure(background='#0099ff')

		self.style = ttk.Style()
		self.style.configure('TFrame',background='#0099ff')
		self.style.configure('TButton',background='#00ff00')
		self.style.configure('TLabel',background='#0099ff',font=('Arial',15))
		self.style.configure('Header.TLabel',font=('Arial', 18, 'bold'))
		self.header = ttk.Frame(root)
		self.header.pack()

		self.image = Image.open('logo.jpeg')
		self.logo = ImageTk.PhotoImage(self.image)
		ttk.Label(self.header,image=self.logo).grid(row=0,column=0,rowspan=2)
		ttk.Label(self.header,text = 'Thanks for Visiting',style='Header.TLabel').grid(row=0,column=1)
		ttk.Label(self.header,wraplength =400 ,text=("We are glad you chose Our college."
									"We hope you enjoyed and learnt a lot here."
									"Please provide your valuable feedback so that "
									"we can improve our system.")).grid(row=1,column=1)


		self.frame_content = ttk.Frame(root)
		self.frame_content.pack()

		ttk.Label(self.frame_content,text='Name:').grid(row=0,column=0,padx=5,sticky='sw')
		ttk.Label(self.frame_content,text='Email:').grid(row=0,column=1,padx=5,sticky='sw')
		ttk.Label(self.frame_content,text='Description:').grid(row=2,column=0,sticky='sw',pady=4)

		self.entry_name = ttk.Entry(self.frame_content,width=24,font =('Arial',10))
		self.entry_email = ttk.Entry(self.frame_content,width=24,font =('Arial',10))
		self.entry_comments = Text(self.frame_content,width=50,height=15,font =('Arial',15),wrap='word')

		self.entry_name.grid(row = 1,column=0,padx=5)
		self.entry_email.grid(row = 1,column=1,padx=5)
		self.entry_comments.grid(row = 3,column=0,columnspan=2,padx=5)


		ttk.Button(self.frame_content, text='Submit',command=self.submit).grid(row=4,column=0,pady=7,padx=7,sticky='e')
		ttk.Button(self.frame_content, text='Reset',command=self.reset).grid(row=4,column=1,pady=7,padx=7,sticky='w')



	def submit(self):
		name = self.entry_name.get()
		email = self.entry_email.get()

		content = self.entry_comments.get(1.0,'end')

		f_content=""
		count=0
		for word in content.split(" "):
			if count==8:
				f_content+='<br>'
				count=0
			f_content+=word+" "
			count+=1


		
		status=0
		
		fs = open('status.txt','r',encoding='utf-8')
		s = fs.read()
		status = int(s)+1
		fs.close()

		css_file = '<link rel="stylesheet" href="style.css">'
		header = '<html>\n'+'<head>\n'+'<title>Feedback-'+name+'</title>\n'+css_file+'\n'+'</head>'+'\n'+'<body>\n'+'<div>'
		footer = '<p>--'+name+'</p>'+'\n<br>'+'\n<p>Email-'+email+'</p>'+'</div>'+'\n'+'</body>\n'+'</html>'
		fs = open('status.txt','w',encoding='utf-8')
		fs.write(str(status))
		fs.close()

		with open('feedback_'+str(status)+'.html','w',encoding='utf-8') as f:
			f.write(header+f_content+footer)

		self.reset()
		messagebox.showinfo(title = 'Given Feedback', message = 'Feedback Submitted!')






	def reset(self):
		self.entry_name.delete(0,'end')
		self.entry_email.delete(0,'end')
		self.entry_comments.delete(1.0,'end')



def main():
	root = Tk()
	feedback = Feedback(root)
	root.mainloop()


if __name__ =="__main__":main()