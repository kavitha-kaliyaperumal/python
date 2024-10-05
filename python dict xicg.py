Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d = {}
>>> d1 = dict()
>>> d2 = {1:6,2:5,3:7}
>>> d3 = dict(d2)
>>> d3
{1: 6, 2: 5, 3: 7}
>>> d4 =  d2
>>> d4
{1: 6, 2: 5, 3: 7}
>>> d5 = dict("hello")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    d5 = dict("hello")
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> d5 = dict("hello",[1,2,3,4,5])
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    d5 = dict("hello",[1,2,3,4,5])
TypeError: dict expected at most 1 arguments, got 2
>>> d5 = dict(list("hello"),[1,2,3,4,5])
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    d5 = dict(list("hello"),[1,2,3,4,5])
TypeError: dict expected at most 1 arguments, got 2
>>> d5 = dict(zip(tuple("hello"),[1,2,3,4,5]))
>>> d5
{'h': 1, 'e': 2, 'l': 4, 'o': 5}
>>> d5 = dict(["hello",[1,2,3,4,5]])
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    d5 = dict(["hello",[1,2,3,4,5]])
ValueError: dictionary update sequence element #0 has length 5; 2 is required
>>> d6 =dict(1,2)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    d6 =dict(1,2)
TypeError: dict expected at most 1 arguments, got 2
>>> d6 =dict(12)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d6 =dict(12)
TypeError: 'int' object is not iterable
>>> d6 =dict((1,2,))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    d6 =dict((1,2,))
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> d6 =dict((1,2))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    d6 =dict((1,2))
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> help(zip)
Help on class zip in module builtins:

class zip(object)
 |  zip(iter1 [,iter2 [...]]) --> zip object
 |  
 |  Return a zip object whose .__next__() method returns a tuple where
 |  the i-th element comes from the i-th iterable argument.  The .__next__()
 |  method continues until the shortest iterable in the argument sequence
 |  is exhausted and then it raises StopIteration.
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> zip([1,2],['a','b'])
<zip object at 0x026A1328>
>>> x = zip([1,2],['a','b'])
>>> x
<zip object at 0x026AEEE0>
>>> for i in x:
	print(i)

	
(1, 'a')
(2, 'b')
>>> x= dict(x)
>>> x
{}
>>> x
{}
>>> x = zip([1,2],['a','b'])
>>> y = dict(x)
>>> y
{1: 'a', 2: 'b'}
>>> dict(x)
{}
>>> d1
{}
>>> d2
{1: 6, 2: 5, 3: 7}
>>> d3
{1: 6, 2: 5, 3: 7}
>>> d4
{1: 6, 2: 5, 3: 7}
>>> d5
{'h': 1, 'e': 2, 'l': 4, 'o': 5}
>>> d6
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    d6
NameError: name 'd6' is not defined
>>> d6 = dict([name = 'neha', age =16,dob= '03-07-2006'])
SyntaxError: invalid syntax
>>> d6 = dict(name = 'neha', age =16,dob= '03-07-2006') #keyword argument
>>> d6
{'name': 'neha', 'age': 16, 'dob': '03-07-2006'}
>>> [a = 2]
SyntaxError: invalid syntax
>>> (t =3,)
SyntaxError: invalid syntax
>>> d7 =dict({1:6,2:5,3:7})
>>> d7
{1: 6, 2: 5, 3: 7}
>>> d8 = dict((1,2),(4,5))
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    d8 = dict((1,2),(4,5))
TypeError: dict expected at most 1 arguments, got 2
>>> d8 = dict(((1,2),(4,5)))
>>> d8
{1: 2, 4: 5}
>>> d8 = dict([(1,2),(4,5)])
>>> d9 = dict([['name','neha'],['age',16],['dob','03-07-2006']])
>>> d9
{'name': 'neha', 'age': 16, 'dob': '03-07-2006'}
>>> x
<zip object at 0x026AEEE0>
>>> w, p = x
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    w, p = x
ValueError: not enough values to unpack (expected 2, got 0)
>>> w,p =x
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    w,p =x
ValueError: not enough values to unpack (expected 2, got 0)
>>> d10 = {}
>>> d10.fromkeys([1,2,3,4])
{1: None, 2: None, 3: None, 4: None}
>>> d10
{}
>>> d11= d10.fromkeys([1,2,3,4])
>>> d11
{1: None, 2: None, 3: None, 4: None}
>>> d13
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    d13
NameError: name 'd13' is not defined
>>> d13 = {}
>>> d14 = d13.fromkeys ([1,2,3,4],[10,1,2,6])
>>> d13
{}
>>> d14
{1: [10, 1, 2, 6], 2: [10, 1, 2, 6], 3: [10, 1, 2, 6], 4: [10, 1, 2, 6]}
>>> d13 = {11:'5'}
>>> d14 = d13.fromkeys ([1,2,3,4],[10,1,2,6])
>>> d13
{11: '5'}
>>> d14
{1: [10, 1, 2, 6], 2: [10, 1, 2, 6], 3: [10, 1, 2, 6], 4: [10, 1, 2, 6]}
>>> 
