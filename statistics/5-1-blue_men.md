[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)
**Exercise 5.1** In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters μ = 178 cm and σ = 7.7 cm for men, and μ = 163 cm and σ = 7.3 cm for women.
In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the U.S. male population is in this range?

About 34% of the US male population is in this range. 


```python
import scipy.stats
from thinkstats2 import Pmf, Cdf
%matplotlib inline

m_male = 178
s_male = 7.7
male_heights = scipy.stats.norm(loc=m_male, scale=s_male)

# To get the fraction in between heights:
male_heights.cdf(185.4)-male_heights.cdf(177.8)

>> 0.34209468
```
