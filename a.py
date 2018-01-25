Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a="sunil"
>>> a+"suwan"
'sunilsuwan'
>>> a[0]
's'
>>> a[2]
'n'
>>> 
a[6]
Traceback (most recent call last):
  File "<pyshell#4>", line 2, in <module>
    a[6]
IndexError: string index out of range
>>> a[0:3]
'sun'
>>> a[:5]
'sunil'
>>> str(42)
'42'
>>> x="hello bai"
>>> x.capitalize
<built-in method capitalize of str object at 0x03CC09D0>
>>> x.capitalize()
'Hello bai'
>>> x.islower()
True
>>> x.isalphanumeric()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x.isalphanumeric()
AttributeError: 'str' object has no attribute 'isalphanumeric'
>>> 
