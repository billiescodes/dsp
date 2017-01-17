[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

**Exercise 3.1** *Use the NSFG respondent variable NUMKDHH to construct the actual distribution for the number of children under 18 in the household.
Now compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in their household.
Plot the actual and biased distributions, and compute their means. As a starting place, you can use chap03ex.ipynb.*

The results from surveying children, and the official household survey are indeed different. In the children survey, households with between 2 to 6 children are overrepresented, by a factor of up to 3 times more. Households with no children would not be represented at all, even though they make up around 47% of total households.  
The PMF mean is **1.02**, whereas the Biased mean is ** 2.4**.

```python
from __future__ import print_function, division

%matplotlib inline

import numpy as np

import nsfg
import first
import thinkstats2
import thinkplot

resp = nsfg.ReadFemResp()

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf


#create a Pmf object
pmf = thinkstats2.Pmf(resp.numkdhh, label='numkdhh')

# biased PMF plot:

biased = BiasPmf (pmf, label='biased')

# plot solution:
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Config(xlabel='Number of children in household',
                    ylabel='PMF')


# print the Mean/Biased mean:

print ("The mean of pmf: ", pmf.Mean())
print ("The Biased mean: ", biased.Mean())


```
