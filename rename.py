import os,os.path
import re

class FindFiles():
	"""docstring for FindFile"""
	def __init__(self,path):
		self.path = os.path.normpath(path)

	def 


def myrename(path,houzhui):
	nowName = os.listdir(path)
	afName = nowName

	key = open('key','r')
	keylist = key.read()
	keylist = keylist.split('\n')

	value = open('value','r')
	valuelist = value.read()
	valuelist = valuelist.split('\n')

	k_v = dict(zip(keylist,valuelist))

	tem_list = []

	myre = r'10459-?_?[a-zA-Z0-9]+-?_?(\d+\s?)_'

	for name in afName:
		the = re.findall(myre, name)
		if the != None:
			tem_list.append(the[0])
	
	tem_list = [x.strip() for x in tem_list]

	for i in range(len(nowName)):
		name0 = path+nowName[i]
		name1 = path+'10459_'+k_v[tem_list[i]]+'_'+tem_list[i]+'_'+houzhui	
		os.rename(name0,name1)	

	key.close()
	value.close()
myrename('zpb/','ZPB.doc')