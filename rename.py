# coding = utf-8
import os,os.path
import re
import shutil
from tkinter import *
from tkinter.filedialog import askdirectory,askopenfilename,font

class FindFiles():
	"""docstring for FindFile"""
	def __init__(self,path):
		self.path = os.path.normpath(path)

	def traversal_all(self):
		temp_list = [[],[]]
		file_list = os.walk(self.path)

		for root,dirs,files in file_list:
			for f in files:
				temp_list[0].append(f)
				temp_list[1].append(root)

		return temp_list

	def traversal_current(self):
		temp_list = [[],[]]
		file_list = os.listdir(self.path)

		for l in file_list:
			l = os.path.join(self.path,l)
			if os.path.isdir(l):
				continue
			else: 
				temp_list.append(l)

		return temp_list


class Regular():
	"""docstring for Regular"""
	def __init__(self, u_re,u_str):
		self.u_re = u_re
		self.u_str = u_str
		
	def findall(self):
		p = re.compile(self.u_re)
		f = p.findall(self.u_str)
		return f
			
class Dict():
	"""docstring for Dict"""
	def __init__(self, klist,vlist):
		self.klist = os.path.join(klist)
		self.vlist = os.path.join(vlist)

	def createDict(self):
		key_list = open(self.klist,'r')
		keys = key_list.read()
		keys = keys.split('\n')
		key_list.close()

		value_list = open(self.vlist,'r')
		values = value_list.read()
		values = values.split('\n')
		value_list.close()

		k_v = dict(zip(keys,values))

		return k_v

class App(Frame):
	"""docstring for App"""
	def __init__(self):
		Frame.__init__(self)

		# self.master.title("Example")
		# self.master.rowconfigure(5, weight=1)
		# self.master.columnconfigure(5, weight=1)

		self.grid(sticky=W+E+N+S)
		self.button1 = Button(self, text="浏览文件夹", command=self.load_dir, width=30)
		self.button1.grid(row=0, column=0, sticky=W)

		self.dirname = StringVar()
		self.entry1 = Entry(self, textvariable = self.dirname, width = 60)
		self.entry1.grid(row = 1, column = 0)

		self.button2 = Button(self, text="选择字典键（可选）", command=self.load_keyfile, width=30)
		self.button2.grid(row=2, column=0, sticky=W)

		self.keys = StringVar()
		self.entry2 = Entry(self,textvariable = self.keys, width = 60)
		self.entry2.grid(row = 3, column = 0)

		self.button3 = Button(self, text="选择字典值（可选）", command=self.load_valusefile, width=30)
		self.button3.grid(row=4, column=0,sticky = W)

		self.values = StringVar()
		self.entry3 = Entry(self,textvariable = self.values, width = 60)
		self.entry3.grid(row = 5, column = 0)

		self.label1 = Label(self,text = "正则表达式")
		self.label1.grid(row = 6,column = 0)

		self.pattern = StringVar()
		self.entry4 = Entry(self,  textvariable = self.pattern, width = 60)
		self.entry4.grid(row = 7, column = 0)

		self.button4 = Button(self, text="插入字典", command=self.insert_dict, width=10)
		self.button4.grid(row=8, column=0,sticky = W)

		self.rename = StringVar()
		self.entry5 = Entry(self,  textvariable = self.rename, width = 60)
		self.entry5.grid(row = 9, column = 0)

		self.buttonx = Button(self, text="X", command=self.run, width=10)
		self.buttonx.grid(row=10, column=0)

	def load_dir(self):
		self.entry1.delete(0,END)
		fname = askdirectory()
		if fname:
			self.entry1.insert(0,fname)

	def load_keyfile(self):
		self.entry2.delete(0,END)
		gl_keys = askopenfilename()
		if gl_keys:
			self.entry2.insert(0,gl_keys)

	def load_valusefile(self):
		self.entry3.delete(0,END)
		gl_values = askopenfilename()
		if gl_values:
			self.entry3.insert(0,gl_values)

	def insert_dict(self):
		if self.keys.get() and self.values.get():
			self.entry5.insert(0,'字典')
		else:
			top = Toplevel()
			top.geometry('300x30')
			top.title('错误')
			label_top = Label(top,text = '未选择文件夹或文件夹不存在',font = 30,fg = 'red',bg = 'blue').pack(fill = 'both')


	def run(self):
		if self.keys.get() and self.values.get():
			mydict = Dict(self.keys,self.values)

		if self.dirname.get():
			findfiles = FindFiles(self.dirname.get())
			sourse_list = findfiles.traversal_all()
			temp_list = []
			for i in range(len(sourse_list[0])):
				temp = sourse_list[0][i]
				regular = Regular(self.pattern.get(),temp)
				# temp_list.append(regular.findall()[0])
				shutil.copy(os.path.join(sourse_list[1][i],sourse_list[0][i]),'test/'+regular.findall()[0])

			top = Toplevel()
			top.geometry('300x30')
			top.title('成功')
			label_top = Label(top,text = '重命名完成',font = 30,fg = 'green',bg = 'black').pack(fill = 'both')

				
		else:
			top = Toplevel()
			top.geometry('300x30')
			top.title('错误')
			label_top = Label(top,text = '未选择文件夹或文件夹不存在',font = 30,fg = 'red',bg = 'blue').pack(fill = 'both')




root = App()
root.mainloop()

# def myrename(path,houzhui):
# 	nowName = os.listdir(path)
# 	afName = nowName

# 	key = open('key','r')
# 	keylist = key.read()
# 	keylist = keylist.split('\n')

# 	value = open('value','r')
# 	valuelist = value.read()
# 	valuelist = valuelist.split('\n')

# 	k_v = dict(zip(keylist,valuelist))

# 	tem_list = []

# 	myre = r'10459-?_?[a-zA-Z0-9]+-?_?(\d+\s?)_'

# 	for name in afName:
# 		the = re.findall(myre, name)
# 		if the != None:
# 			tem_list.append(the[0])
	
# 	tem_list = [x.strip() for x in tem_list]

# 	for i in range(len(nowName)):
# 		name0 = path+nowName[i]
# 		name1 = path+'10459_'+k_v[tem_list[i]]+'_'+tem_list[i]+'_'+houzhui	
# 		os.rename(name0,name1)	

# 	key.close()
# 	value.close()
# myrename('zpb/','ZPB.doc')
