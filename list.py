Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> country=['india','usa','uk','china','pak']
>>> country
['india', 'usa', 'uk', 'china', 'pak']
>>> country
['india', 'usa', 'uk', 'china', 'pak']
>>> coountry[india='1']
SyntaxError: invalid syntax
>>> country['india:1','uk:2','usa:3','america:4','pak:5']
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    country['india:1','uk:2','usa:3','america:4','pak:5']
TypeError: list indices must be integers or slices, not tuple
>>> country=['india:1','uk:2','usa:3','america:4','pak:5']
>>> country
['india:1', 'uk:2', 'usa:3', 'america:4', 'pak:5']
>>> country.append('aus')
>>> country
['india:1', 'uk:2', 'usa:3', 'america:4', 'pak:5', 'aus']
>>> country.append('aus:6')
>>> country
['india:1', 'uk:2', 'usa:3', 'america:4', 'pak:5', 'aus', 'aus:6']
>>> 
