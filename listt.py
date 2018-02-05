Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list=[1,2,3,4,5,6,7,8,9]
>>> list[:8],list[1:-],list[1:2:1]
SyntaxError: invalid syntax
>>> list[:8]
[1, 2, 3, 4, 5, 6, 7, 8]
>>> list[1:-]
SyntaxError: invalid syntax
>>> list[1:_]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    list[1:_]
TypeError: slice indices must be integers or None or have an __index__ method
>>> list[1:2:1]
[2]
>>> list[1: ]
[2, 3, 4, 5, 6, 7, 8, 9]
>>> list[1:4:1]
[2, 3, 4]
>>> list[1:5:2]
[2, 4]
>>> 'i' in 'sunil'
True
>>> 2 in list
True
>>> name=input("hello")
hellohi
>>> name=input("hi")
hi hello
>>> 
