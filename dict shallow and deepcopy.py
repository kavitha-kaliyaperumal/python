Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d= dict(school= "Kurinji",city="Namakkal")
>>> d
{'school': 'Kurinji', 'city': 'Namakkal'}
>>> d1 = d
>>> id(d1),id(d)
(40554592, 40554592)
>>> d2 = d.copy()
>>> id(d),id(d2)
(40554592, 40247136)
>>> for i in d2:
	print(i,id(i),d2[i],id(d2[i]))

	
school 40511136 Kurinji 40511008
city 40511168 Namakkal 40322496
>>> for i in d:
	print(i,id(i),d[i],id(d[i]))

	
school 40511136 Kurinji 40511008
city 40511168 Namakkal 40322496
>>> d
{'school': 'Kurinji', 'city': 'Namakkal'}
>>> d2['pincode'] =637003
>>> d2
{'school': 'Kurinji', 'city': 'Namakkal', 'pincode': 637003}
>>> d
{'school': 'Kurinji', 'city': 'Namakkal'}
>>> for i in d:
	print(i,id(i),d[i],id(d[i]))

	
school 40511136 Kurinji 40511008
city 40511168 Namakkal 40322496
>>> for i in d2:
	print(i,id(i),d2[i],id(d2[i]))

	
school 40511136 Kurinji 40511008
city 40511168 Namakkal 40322496
pincode 41213760 637003 40308432
>>> d = {'school': 'Kurinji', 'city': 'Namakkal','total' :[500,700]}
>>> for i in d:
	print(i,id(i),d[i],id(d[i]))

	
school 40511136 Kurinji 40511008
city 40511168 Namakkal 40322496
total 39775008 [500, 700] 30997520
>>> d3 = d.copy()
>>> id(d),id(d3)
(41280976, 41280880)
>>> d3
{'school': 'Kurinji', 'city': 'Namakkal', 'total': [500, 700]}
>>> d3['total'].append(100)
>>> d3
{'school': 'Kurinji', 'city': 'Namakkal', 'total': [500, 700, 100]}
>>> d
{'school': 'Kurinji', 'city': 'Namakkal', 'total': [500, 700, 100]}
>>> d3['emailid']= 'kurinjischoolnkl@gmail.com'
>>> 
>>> d3
{'school': 'Kurinji', 'city': 'Namakkal', 'total': [500, 700, 100], 'emailid': 'kurinjischoolnkl@gmail.com'}
>>> d
{'school': 'Kurinji', 'city': 'Namakkal', 'total': [500, 700, 100]}
>>> d3['total'].pop()
100
>>> d3
{'school': 'Kurinji', 'city': 'Namakkal', 'total': [500, 700], 'emailid': 'kurinjischoolnkl@gmail.com'}
>>> d
{'school': 'Kurinji', 'city': 'Namakkal', 'total': [500, 700]}
>>> d['cno'] = 7373785101
>>> d
{'school': 'Kurinji', 'city': 'Namakkal', 'total': [500, 700], 'cno': 7373785101}
>>> d3
{'school': 'Kurinji', 'city': 'Namakkal', 'total': [500, 700], 'emailid': 'kurinjischoolnkl@gmail.com'}
>>> del d3['total']
>>> d3
{'school': 'Kurinji', 'city': 'Namakkal', 'emailid': 'kurinjischoolnkl@gmail.com'}
>>> d
{'school': 'Kurinji', 'city': 'Namakkal', 'total': [500, 700], 'cno': 7373785101}
>>> d3 = {'school': 'Kurinji', 'city': 'Namakkal', 'total': [500, 700], 'cno': 7373785101}
>>> id(d),id(d3)
(41280976, 41281360)
>>> d4 = d.copy()
>>> d4
{'school': 'Kurinji', 'city': 'Namakkal', 'total': [500, 700], 'cno': 7373785101}
>>> d
{'school': 'Kurinji', 'city': 'Namakkal', 'total': [500, 700], 'cno': 7373785101}
>>> d4['total'].append(100)
>>> d4
{'school': 'Kurinji', 'city': 'Namakkal', 'total': [500, 700, 100], 'cno': 7373785101}
>>> d
{'school': 'Kurinji', 'city': 'Namakkal', 'total': [500, 700, 100], 'cno': 7373785101}
>>> import copy
>>> d5 = copy.deepcopy(d)
>>> id(d5),id(d)
(41281792, 41280976)
>>> id(d5['total']),id(d['total'])
(30997080, 30997520)
>>> d5
{'school': 'Kurinji', 'city': 'Namakkal', 'total': [500, 700, 100], 'cno': 7373785101}
>>> d
{'school': 'Kurinji', 'city': 'Namakkal', 'total': [500, 700, 100], 'cno': 7373785101}
>>> d5['total'].pop()
100
>>> d5
{'school': 'Kurinji', 'city': 'Namakkal', 'total': [500, 700], 'cno': 7373785101}
>>> d
{'school': 'Kurinji', 'city': 'Namakkal', 'total': [500, 700, 100], 'cno': 7373785101}
>>> 
