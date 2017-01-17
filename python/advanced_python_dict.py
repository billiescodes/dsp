#!/usr/bin/Python
# -*- coding: utf-8 -*-

#billiescodes 2017
"""
    Part III Dictionary 
    create a dictionary of format
    dict = { last name : [ 'degree','title','email'] }
"""
import sys
import re
from py_regex import find_degrees

# import file, read line by line
# extract last name, degree, title, email 
# then run through dictionary 


def create_dict(filename):

    input_file = open(filename, 'r')
    counter = 0
    faculty_1 = {}; faculty_2 = {}

    for line in input_file:
        if counter == 0:
            counter +=1
            continue
        if counter ==1: print line
        #first name before first comma
        full_name = re.search(r'([\w\.\s+\(\)]*)\s([\w]+)\,' ,line)

        degrees_match = re.search(r'\,([\s*\w+\.*]+)\,', line)
        title_match = re.search(r'\,\s*([\w\s*]*\s*Professor\s*[\w\s*]*)\,',line)
        email_match = re.search(r'[\w\.-]+@[\w\.-]+' ,line)
        counter +=1
        a=[]

        if degrees_match and title_match and email_match:
            #bbEDIT this creates a tuple, want list
            #a.append((degrees_match.group(1), title_match.group(1), email_match.group() ))
            a.append(degrees_match.group(1))
            a.append(title_match.group(1))
            a.append(email_match.group() )

        t=[]; count2 = 0

        if full_name:
            ### DICT 1
            if full_name.group(2) not in faculty_1.keys():
                faculty_1[full_name.group(2)] = [a]
            else:
                faculty_1[full_name.group(2)] += [a]

            ### DICT 2
            t.append((full_name.group(1),full_name.group(2) ))
            if t[0] not in faculty_2.keys():
                faculty_2[t[0]] = [a]
# view dict 
    for k, v in faculty_1.items(): print k, v

    print "\n",     faculty_1['Ellenberg']
    print "\n"

    ### print DICT 2 sorted by first element in tuple key
    for k, v in sorted(faculty_2.items()): print k,v
    print "\n"
    
 ## Sort dictionary whose keys are tuples according to the second value in the tuple
    ## sorted will work on .keys() but not on .items()
    ## so use keys only to print out whole dictionary

    for k in sorted(faculty_2.keys(), key=lambda key: key[1] ):
        print k, faculty_2[k]
 

def main():

    print " \n begin Dictionary functions"

    args = sys.argv[1:]

    if not args:
        print "please give a file name"
        sys.exit(1)
    else:
        myfile = args[0]

    #degrees = find_degrees(myfile)    
    #print "degrees are: ", degrees

    # first_dict, second_dict = 
    create_dict(myfile)

if __name__ == "__main__":
    main()
