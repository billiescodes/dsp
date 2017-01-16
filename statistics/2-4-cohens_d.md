[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)
Exercise 2.4 Using the variable totalwgt_lb, investigate whether first ba- bies are lighter or heavier than others. Compute Cohen’s d to quantify the difference between the groups. How does it compare to the difference in pregnancy length?

The mean weight for first born babies is 7.2 lbs, and others 7.32 lbs. The Cohen's d coefficient is computed as -0.088, showing that the difference in weight for first born/other babies is small. The weight difference is only slightly larger than for pregnancy length, with a Cohen's: d = 0.028. 


```python
from __future__ import print_function, division
import numpy as np
import nsfg
import first
import thinkplot
import thinkstats2
%matplotlib inline

# load the data 'nsfg'
preg = nsfg.ReadFemPreg()

# live birth results
live = preg[preg.outcome == 1]

# first vs. other babies
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

# Compute mean of Total Weight: 
print ("Mean total weight (firsts, others) ")
print (firsts.totalwgt_lb.mean(), others.totalwgt_lb.mean())
# Compute the mean values of pregnancy length
print ("Mean pregnancy length (firsts, others) ")
print (firsts.prglngth.mean(), others.prglngth.mean()) 


width = 0.45
#first plot individual histograms
hist_f = thinkstats2.Hist(firsts.totalwgt_lb,
                          label='totalwgt_lb (first babies)')
hist_o = thinkstats2.Hist(others.totalwgt_lb,
                          label='totalwgt_lb (all others)')
#put on same plot
thinkplot.Hist(hist_f, align='right', width=width)
thinkplot.Hist(hist_o,align='left', width=width  )


# compute Cohen effect Size on total weight:

d_totalwgt =  CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)

# compute Cohen effect Size on pregnancy length
d_prglngth =  CohenEffectSize(firsts.prglngth, others.prglngth)

print ("CohenEffectSize: (total weight, pregnancy length) ")
print ( d_totalwgt, d_prglngth)
```
