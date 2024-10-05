Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a= {}
>>> dict([1,2])
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    dict([1,2])
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> dict()
{}
>>> a = dict()
>>> a  = dict('a':1,'b':2,'c':3)
SyntaxError: invalid syntax
>>> a  = dict('a',1,'b',2,'c',3)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a  = dict('a',1,'b',2,'c',3)
TypeError: dict expected at most 1 arguments, got 6
>>> a = dict(['a',1,'b',2])
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a = dict(['a',1,'b',2])
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> a = dict([['a',1],['b',2]])
>>> a
{'a': 1, 'b': 2}
>>> a['a']
1
>>> a.get(a)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.get(a)
TypeError: unhashable type: 'dict'
>>> a.get('a')
1
>>> a.get('a',"nothing")
1
>>> a.get('c',"nothing")
'nothing'
>>> a
{'a': 1, 'b': 2}
>>> a.setdefault('c',3)
3
>>> a
{'a': 1, 'b': 2, 'c': 3}
>>> b = {'d':4,'e':5}
>>> a.update(b)
>>> a
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
>>> b
{'d': 4, 'e': 5}
>>> a.clear()
>>> a = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
>>> a
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
>>> #[('a',1),('b',2)]
>>> a.pack()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.pack()
AttributeError: 'dict' object has no attribute 'pack'
>>> a.items()
dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
>>> b
{'d': 4, 'e': 5}
>>> c = dict(zip([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]))
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    c = dict(zip([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]))
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> c = dict(zip(('a','b','c'),(1,2,3)))
>>> c]
SyntaxError: invalid syntax
>>> c
{'a': 1, 'b': 2, 'c': 3}
>>> d = dict(list((1,3),('a','b')))
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    d = dict(list((1,3),('a','b')))
TypeError: list expected at most 1 arguments, got 2
>>> e .fromkeys('hi':4)
SyntaxError: invalid syntax
>>> e .fromkeys('hi',4)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    e .fromkeys('hi',4)
NameError: name 'e' is not defined
>>> e = {}
>>> e .fromkeys('hi',4)
{'h': 4, 'i': 4}
>>> e .fromkeys('hill',4)
{'h': 4, 'i': 4, 'l': 4}
>>> e
{}
>>> f = dict({'a':1})
>>> f
{'a': 1}
>>> g = dict(name= 'Raj',age = 18,dob = '15-08-2004') # keyword
>>> g
{'name': 'Raj', 'age': 18, 'dob': '15-08-2004'}
>>> h = dict(g)
>>> h
{'name': 'Raj', 'age': 18, 'dob': '15-08-2004'}
>>> i = zip(g)
>>> i
<zip object at 0x028A4F80>
>>> for x in i:
	print(x)

	
('name',)
('age',)
('dob',)
>>> zip(((1,2,3),(10,20,20)))
<zip object at 0x028AA058>
>>> x = dict(zip(((1,2,3),(10,20,20))))
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    x = dict(zip(((1,2,3),(10,20,20))))
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> x = dict(zip((1,2,3),(10,20,20)))
>>> x
{1: 10, 2: 20, 3: 20}
>>>  z = [1,2,4],[4,5,6]
 
SyntaxError: unexpected indent
>>> z = [1,2,4],[4,5,6]
>>> x = dict(zip(z))
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    x = dict(zip(z))
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> s = {'*' :*}
SyntaxError: invalid syntax
>>> a
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> a.pop('e')
5
>>> a
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> type(a. values())
<class 'dict_values'>
>>> type(list(a. values()))
<class 'list'>
>>> a.pop('e',"not available")
'not available'
>>> a.pop('e')
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a.pop('e')
KeyError: 'e'
>>> a.pop('e','e')
'e'
>>> a
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> a.popitem()
('d', 4)
>>> x =  a.popitem()
>>> type(x)
<class 'tuple'>
>>> x
('c', 3)
>>> max(('a','aa','aab'))
'aab'
>>> a
{'a': 1, 'b': 2}
>>> del a['b']
>>> a
{'a': 1}
>>> t =  1,2,3
>>> del t[2]
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    del t[2]
TypeError: 'tuple' object doesn't support item deletion
>>> 
