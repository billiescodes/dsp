# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?
>
A list, or an array, is an ordered sequence of values, where the values can be any type (int, float, string). A tuple is an immutable list.

Because Dictionary use hash tables to store key-value pairs, the keys have to be immutable. Only tuples can be used as keys in a dictionary. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Both lists and sets are ordered sequences of values. The difference is that lists may contain redundant values, while sets only contain unique values. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

> Lambda is an anonymys function that lives inside methods. It is used to perform a quick action without explicitly writing a definition.

```python
>>> a = [1, 27,3, 5, 112, 2]
>>> sorted(a, key = lambda x : x, reverse=True)
[112, 27, 5, 3, 2, 1]
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

> List comprehension is quick way of creating a new list, by iterating over each member and applying some action on it.  It also uses simple brackets to encompass the creation of the list, which is a very natural, mathematical way of thinking about a list of items.
```python
>>> [a+2 for a in range(1,5)]
[3, 4, 5, 6]
```
> Map and Filter are python built-in functions that act like list comprehensions. 
using Map: 
```python
>>> a = [1, 27,3, 5, 112, 2]
>>> def sqrt(x): return x ** 2

>>> list(map(sqrt, a))
[1, 729, 9, 25, 12544, 4]
```
> Using Filter (which extracts each member of the list for which the condition returns true) :
```python
>>> list(filter(lambda x: x>50, a))
[112]
```
> Set comprehension:
```python
>>> {x * y for x in [0, 1, 2] for y in [0, 1, 2]}
set([0, 1, 2, 4])
```
> Dictionary comprehension:
```python 
>>> { x: str(len(x)*100)+'$' for x in ['London', 'Paris', 'New York'] }
{'Paris': '500$', 'New York': '800$', 'London': '600$'}
```



---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days


b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days


c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





