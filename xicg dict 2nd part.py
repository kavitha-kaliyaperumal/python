Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d = ()
>>> type(d)
<class 'tuple'>
>>> d = dict(zip(range(1,4),range(11,14)))
>>> d
{1: 11, 2: 12, 3: 13}
>>> # delete <dict>.pop(<key>[,default])
>>> L = [1,2,3]
>>> L.pop() # will remove last element from the list
3
>>> L
[1, 2]
>>> L.pop(-1)
2
>>> L
[1]
>>> # delete <dict>.pop(<key>[,default])
>>> d
{1: 11, 2: 12, 3: 13}
>>> d.pop()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> x =d.pop(2)
>>> x
12
>>> d
{1: 11, 3: 13}
>>> d1 = {'1st':'vaccum tube'}
>>> d1
{'1st': 'vaccum tube'}
>>> d.update(d1)
>>> d
{1: 11, 3: 13, '1st': 'vaccum tube'}
>>> d[5] = d1
>>> d
{1: 11, 3: 13, '1st': 'vaccum tube', 5: {'1st': 'vaccum tube'}}
>>> x =d.setdefault(1,300)
>>> x
11
>>> x =d.setdefault(13,300)
>>> x
300
>>> d
{1: 11, 3: 13, '1st': 'vaccum tube', 5: {'1st': 'vaccum tube'}, 13: 300}
>>> # delete <dict>.pop(<key>[,default])
>>> d.pop(23)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    d.pop(23)
KeyError: 23
>>> d.pop(3)
13
>>> d
{1: 11, '1st': 'vaccum tube', 5: {'1st': 'vaccum tube'}, 13: 300}
>>> d.pop(23,"Key not available")
'Key not available'
>>> d.get(1)
11
>>> d.get(23)
>>> d.get(23,"Key not available")
'Key not available'
>>> d
{1: 11, '1st': 'vaccum tube', 5: {'1st': 'vaccum tube'}, 13: 300}
>>> #<dict>.popitem()
>>> print(type(d.popitem()))
<class 'tuple'>
>>> d
{1: 11, '1st': 'vaccum tube', 5: {'1st': 'vaccum tube'}}
>>> d.popitem()
(5, {'1st': 'vaccum tube'})
>>> #del dict[<index>]
>>> t = 1,2,3
>>> d1
{'1st': 'vaccum tube'}
>>> del t
>>> del d1
>>> d1
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    d1
NameError: name 'd1' is not defined
>>> t = 1,2,3
>>> del t[0]
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    del t[0]
TypeError: 'tuple' object doesn't support item deletion
>>> d
{1: 11, '1st': 'vaccum tube'}
>>> del d['1st']
>>> d
{1: 11}
>>> 
