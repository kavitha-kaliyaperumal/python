Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
Type "help", "copyright", "credits" or "license()" for more information.
SyntaxError: invalid syntax
>>> d = {1:'a',2:'e':,3:'i',4:'o'}
SyntaxError: invalid syntax
>>> d = {1:'a',2:'e',3:'i',4:'o'}
>>> len(d)
4
>>> d[3]
'i'
>>> d.get(3)
'i'
>>> d.get(7)
>>> d.get(7,"No key")
'No key'
>>> d.keys(3)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    d.keys(3)
TypeError: keys() takes no arguments (1 given)
>>> d.keys()
dict_keys([1, 2, 3, 4])
>>> x = d.keys()
>>> x
dict_keys([1, 2, 3, 4])
>>> x[1]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x[1]
TypeError: 'dict_keys' object is not subscriptable
>>> x = d.keys()
>>> x = list(d.keys())
>>> x
[1, 2, 3, 4]
>>> x[1]
2
>>> d.values()
dict_values(['a', 'e', 'i', 'o'])
>>> y = list(d.values())
>>> y
['a', 'e', 'i', 'o']
>>> y[1]
'e'
>>> d
{1: 'a', 2: 'e', 3: 'i', 4: 'o'}
>>> d[5]='u'
>>> d
{1: 'a', 2: 'e', 3: 'i', 4: 'o', 5: 'u'}
>>> del d[5]
>>> d
{1: 'a', 2: 'e', 3: 'i', 4: 'o'}
>>> d.items()
dict_items([(1, 'a'), (2, 'e'), (3, 'i'), (4, 'o')])
>>> z= list(d.items())
>>> z
[(1, 'a'), (2, 'e'), (3, 'i'), (4, 'o')]
>>> z[1]
(2, 'e')
>>> d.setdefault(5,'u')
'u'
>>> d
{1: 'a', 2: 'e', 3: 'i', 4: 'o', 5: 'u'}
>>> d.setdefault(5,'x')
'u'
>>> d
{1: 'a', 2: 'e', 3: 'i', 4: 'o', 5: 'u'}
>>> d[5]= 'x'
>>> d
{1: 'a', 2: 'e', 3: 'i', 4: 'o', 5: 'x'}
>>> d1= {'raj':999999999,'sameer':99999944444}
>>> d2 = {'sunil':8888844444}
>>> d1
{'raj': 999999999, 'sameer': 99999944444}
>>> d2
{'sunil': 8888844444}
>>> d1.update(d2)
>>> d1
{'raj': 999999999, 'sameer': 99999944444, 'sunil': 8888844444}
>>> d2
{'sunil': 8888844444}
>>> d1
{'raj': 999999999, 'sameer': 99999944444, 'sunil': 8888844444}
>>> d2 = {'sunil': 7777774444}
>>> d1.update(d2)
>>> d1
{'raj': 999999999, 'sameer': 99999944444, 'sunil': 7777774444}
>>> 
>>> d
{1: 'a', 2: 'e', 3: 'i', 4: 'o', 5: 'x'}
>>> d3 = {}
>>> d4.clear()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    d4.clear()
NameError: name 'd4' is not defined
>>> d3.fromkeys([1,2,3,4,5,6,7])
{1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None}
>>> d3
{}
>>> d3.fromkeys(['a','b','c','d'],100)
{'a': 100, 'b': 100, 'c': 100, 'd': 100}
>>> d3
{}
>>> d3= d3.fromkeys('abcde',100)
>>> d3
{'a': 100, 'b': 100, 'c': 100, 'd': 100, 'e': 100}
>>> d3= d3.fromkeys('abcde',(100,200))
>>> d3
{'a': (100, 200), 'b': (100, 200), 'c': (100, 200), 'd': (100, 200), 'e': (100, 200)}
>>> #pop(<key>,"default")
>>> d
{1: 'a', 2: 'e', 3: 'i', 4: 'o', 5: 'x'}
>>> d.pop()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> d.pop(5)
'x'
>>> d
{1: 'a', 2: 'e', 3: 'i', 4: 'o'}
>>> d.pop(5)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    d.pop(5)
KeyError: 5
>>> d.pop(5,"Key not exists")
'Key not exists'
>>> #popitem()
>>> d
{1: 'a', 2: 'e', 3: 'i', 4: 'o'}
>>> d1
{'raj': 999999999, 'sameer': 99999944444, 'sunil': 7777774444}
>>> d1.popitem()
('sunil', 7777774444)
>>> d1
{'raj': 999999999, 'sameer': 99999944444}
>>> d.
