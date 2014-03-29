# coding = utf-8
import os,os.path
import re
import shutil
from tkinter import *
from tkinter.filedialog import askdirectory

class FindFiles():
	"""docstring for FindFile"""
	def __init__(self,path):
		self.path = os.path.normpath(path)

	def traversal_all(self):
		temp_list = []
		file_list = os.walk(self.path)

		for root,dirs,files in file_list:
			for f in files:
				f = os.path.join(root,f)
				temp_list.append(f)

		return temp_list

	def traversal_current(self):
		temp_list = []
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
		self.button1 = Button(self, text="浏览文件夹", command=self.load_dir, width=10)
		self.button1.grid(row=0, column=0, sticky=W)

		self.entry1 = Entry(self,width = 60)
		self.entry1.grid(row = 1, column = 0)

		self.button2 = Button(self, text="选择字典键", command=self.load_dir, width=10)
		self.button2.grid(row=2, column=0, sticky=W)
		self.button2 = Button(self, text="选择字典值", command=self.load_dir, width=10)
		self.button2.grid(row=2, column=1)

		self.entry2 = Entry(self,width = 60)
		self.entry2.grid(row = 3, column = 0)
		self.entry3 = Entry(self,width = 60)
		self.entry3.grid(row = 4, column = 0)

	def load_dir(self):
		self.entry1.delete(0,END)
		global fname
		fname = askdirectory()
		if fname:
			self.entry1.insert(0,fname)

	def load_keyfile(self):
		self.entry1.delete(0,END)
		global keys
		keys = askopenfilname()
		if keys:
			self.entry2.insert(0,keys)




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