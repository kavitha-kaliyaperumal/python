Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = []
>>> L1= list()
>>> L2 = eval([])
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    L2 = eval([])
TypeError: eval() arg 1 must be a string, bytes or code object
>>> L2 = eval('[]')
>>> type(L2)
<class 'list'>
>>> L1 # 1- 10
[]
>>> for i in range(1,11):
	if i% 2 == 0:
		L1.append(i)

		
>>> L1
[2, 4, 6, 8, 10]
>>> L1.extend((12,14))
>>> L1
[2, 4, 6, 8, 10, 12, 14]
>>> L1.append([16,18])
>>> L1
[2, 4, 6, 8, 10, 12, 14, [16, 18]]
>>> L1.insert(0,0)
>>> L1
[0, 2, 4, 6, 8, 10, 12, 14, [16, 18]]
>>> L1.remove(14)# L1.pop(7)
>>> L1
[0, 2, 4, 6, 8, 10, 12, [16, 18]]
>>> L1.pop()
[16, 18]
>>> L1
[0, 2, 4, 6, 8, 10, 12]
>>> del L1[5]
>>> L1
[0, 2, 4, 6, 8, 12]
>>> del L1[2:5]
>>> L1
[0, 2, 12]
>>> L1
[0, 2, 12]
>>> L1.clear()
>>> L1
[]
>>> L1 = [2,45,6,8]
>>> del L1
>>> L1
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    L1
NameError: name 'L1' is not defined
>>> L2
[]
>>> L2 = [3,2,9,1,3,5,7,5,9]
>>> L2.count(2)
1
>>> L2.count(5)
2
>>> L2.count(11)
0
>>> L2.index(2)
1
>>> L2.index(5)
5
>>> L2.count(100)
0
>>> t = 3,5,6,7,4,5,3,3,3
>>> t.count(3)
4
>>> t.index(3)
0
>>> t.index
<built-in method index of tuple object at 0x015DAD70>
>>> t.index(100)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    t.index(100)
ValueError: tuple.index(x): x not in tuple
>>> t[100]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    t[100]
IndexError: tuple index out of range
>>> L2
[3, 2, 9, 1, 3, 5, 7, 5, 9]
>>> L2.sort()
>>> L2
[1, 2, 3, 3, 5, 5, 7, 9, 9]
>>> L2.reverse()
>>> L2
[9, 9, 7, 5, 5, 3, 3, 2, 1]
>>> sorted(L2)
[1, 2, 3, 3, 5, 5, 7, 9, 9]
>>> sorted(t)
[3, 3, 3, 3, 4, 5, 5, 6, 7]
>>> min(t)
3
>>> max(t)
7
>>> min(L2)
1
>>> max(L2)
9
>>> sum(L2)
44
>>> sum(t)
39
>>> reversed(L2)
<list_reverseiterator object at 0x015F55F0>
>>> L2
[9, 9, 7, 5, 5, 3, 3, 2, 1]
>>> t
(3, 5, 6, 7, 4, 5, 3, 3, 3)
>>> sl = reversed(L2)
>>> for i in sl:
	print(i)

	
1
2
3
3
5
5
7
9
9
>>> st = reversed(t)
>>> st
<reversed object at 0x0253DCF0>
>>> for i in st:
	print(i,end =' ')

	
3 3 3 5 4 7 6 5 3 
>>> l = range(10)
>>> l
range(0, 10)
>>> l = list(range(10))
>>> l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> l.sort
