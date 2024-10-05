Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d = {}
>>> type(d)
<class 'dict'>
>>> d1 = dict()
>>> d1
{}
>>> type(d1)
<class 'dict'>
>>> # d = {<key immutable>:<mutable/immutable>,...}
>>> d = {1 :'o'}
>>> d = {[1,2]:'o'}
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    d = {[1,2]:'o'}
TypeError: unhashable type: 'list'
>>> d = {(1,2):'o'}
>>> d
{(1, 2): 'o'}
>>> d = {{1,2}:'o'}
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    d = {{1,2}:'o'}
TypeError: unhashable type: 'set'
>>> d = {{1:'o'}:'o'}
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    d = {{1:'o'}:'o'}
TypeError: unhashable type: 'dict'
>>> d
{(1, 2): 'o'}
>>> d= {(1,{1,2},2):'o'}
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    d= {(1,{1,2},2):'o'}
TypeError: unhashable type: 'set'
>>> d = {1:'a',2:'e',3:'i'}
>>> len(d)
3
>>> d1 = {4:'o',5:'u'}
>>> d + d1 #joining
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d + d1 #joining
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> d * 2 #repeating
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    d * 2 #repeating
TypeError: unsupported operand type(s) for *: 'dict' and 'int'
>>> d
{1: 'a', 2: 'e', 3: 'i'}
>>> 1 in d # membership
True
>>> 'a' in d
False
>>> 'x' in d
False
>>> 10 not in d
True
>>> dcopy = d
>>> id(d),id(dcopy)
(42516864, 42516864)
>>> for i in enumerate(d):
	print(i)

	
(0, 1)
(1, 2)
(2, 3)
>>> for i in d:
	print("key:",i,"Value:",d[i])

	
key: 1 Value: a
key: 2 Value: e
key: 3 Value: i
>>> for i in d:
	print("key:",i,"key id:",id(i),"Value:",d[i],"value id:",id(d[i]))

	
key: 1 key id: 1506305200 Value: a value id: 8006688
key: 2 key id: 1506305216 Value: e value id: 7962080
key: 3 key id: 1506305232 Value: i value id: 7960768
>>> d
{1: 'a', 2: 'e', 3: 'i'}
>>> dcopy
{1: 'a', 2: 'e', 3: 'i'}
>>> for i in dcopy:
	print("key:",i,"key id:",id(i),"Value:",dcopy[i],"value id:",id(dcopy[i]))

	
key: 1 key id: 1506305200 Value: a value id: 8006688
key: 2 key id: 1506305216 Value: e value id: 7962080
key: 3 key id: 1506305232 Value: i value id: 7960768
>>> d
{1: 'a', 2: 'e', 3: 'i'}
>>> d[2]
'e'
>>> L= [1,2,3]
>>> L[2]
3
>>> L[7]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    L[7]
IndexError: list index out of range
>>> L[4] = 8
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    L[4] = 8
IndexError: list assignment index out of range
>>> d
{1: 'a', 2: 'e', 3: 'i'}
>>> d[4]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    d[4]
KeyError: 4
>>> d[4] = 'o'
>>> d
{1: 'a', 2: 'e', 3: 'i', 4: 'o'}
>>> d[4] = 'y'
>>> d
{1: 'a', 2: 'e', 3: 'i', 4: 'y'}
>>> d[4] = 'o'
>>> d
{1: 'a', 2: 'e', 3: 'i', 4: 'o'}
>>> L
[1, 2, 3]
>>> del L[0]
>>> L
[2, 3]
>>> del L
>>> L
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    L
NameError: name 'L' is not defined
>>> t = 1,2,3
>>> del t[0]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    del t[0]
TypeError: 'tuple' object doesn't support item deletion
>>> del t
>>> del
SyntaxError: invalid syntax
>>> del t
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    del t
NameError: name 't' is not defined
>>> d1
{4: 'o', 5: 'u'}
>>> del d1[5]
>>> d1
{4: 'o'}
>>> del d1
>>> d1
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    d1
NameError: name 'd1' is not defined
>>> d1 = {4:'o',5:'u'}
>>> del d1 #data structure will be deleted
>>> d1 = {4:'o',5:'u'}
>>> d1.clear()
>>> d1 # clear only key :pairs
{}
>>> d1 = {4:'o',5:'u'}
>>> d.get(2) #value 'e'
'e'
>>> d
{1: 'a', 2: 'e', 3: 'i', 4: 'o'}
>>> d.get(5) #Error
>>> d
{1: 'a', 2: 'e', 3: 'i', 4: 'o'}
>>> d[5]
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    d[5]
KeyError: 5
>>> d.get(5,"Key not exists") #Error
'Key not exists'
>>> d.get()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    d.get()
TypeError: get expected at least 1 arguments, got 0
>>> d.get(3,"Key not exists") # value i
'i'
>>> d
{1: 'a', 2: 'e', 3: 'i', 4: 'o'}
>>> d.keys()
dict_keys([1, 2, 3, 4])
>>> x = d.keys()
>>> type(x)
<class 'dict_keys'>
>>> 
