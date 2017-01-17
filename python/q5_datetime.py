# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

####b)  
date_start = '12312013'  
date_stop = '05282015'  

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

```python
#!/usr/bin/Python
# -*- coding: utf-8 -*-

from datetime import datetime

def find_days(begin_date, end_date, date_format):

    begin = datetime.strptime(begin_date, date_format)
    end = datetime.strptime(end_date, date_format)
    print begin
    print end
    difference = abs(end-begin)
    print difference.days , "days"


date_start = '01-02-2013'
date_stop = '07-28-2015'
print "\t part a :"
find_days(date_start, date_stop, '%m-%d-%Y')

print "\t part b"
date_start = '12312013'
date_stop = '05282015'

find_days(date_start, date_stop, '%m%d%Y')


print '\t part c'
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

find_days(date_start, date_stop, '%d-%b-%Y')
```
