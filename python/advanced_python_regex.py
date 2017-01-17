#!/usr/bin/Python
# -*- coding: utf-8 -*-

#billiescodes 2017
# Second line: (Correct way to define Python source code encoding) 
"""
 Metis assignment:
     Q1. Find how many different degrees there are, and their frequencies: 
    #Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.
     Q2. Find how many different titles there are, and their frequencies: Ex: Assistant Professor, Professor
    Q3. Search for email addresses and put them in a list. Print the list of email addresses.

    usage: python py_regex.py [faculty.csv] -save
            [ ]         > file for analysis
            -save flag  >
"""

import re
import sys

def find_degrees(filename):

    # open the file 
    input_file = open(filename,'r')
    counter=0; test=0
    degrees = {} # dictionary of Degrees

    # go through input file line by line
    for line in input_file:
        # between the first two commas, where the right comma preceeds the words
        # (Assistant/Associate) Professor
        # find a group of chracters, repeated 1 or more times ([ ]+)
        # that match 1 or more letter, plus 0 or more periods, \s*\w+\.*
        # separated by zero or more spaces 

        degrees_match = re.findall(r'\,([\s*\w+\.*]+)\,\s*[\w]*\s*Professor', line)
        counter +=1

        for deg in degrees_match:
            #sperate multiple degrees into array of strings
            # and remove punctuation
            tmp_string = "".join( a for a in deg if a not in ('.', ',', '?', '!') ).split()
            #print "tmp is: ", tmp_string

            #iterate over tmp_string array
            for a in tmp_string:
                if not a.isdigit():
                    if a in degrees.keys():
                        degrees[a] +=1
                    else:
                        degrees[a] = 1

    #loop over dict degrees and look at degree frequencies
    for key in sorted(degrees.keys()):
        print key, degrees[key]

    return len(degrees)
    print "there are {} lines, ergo {} faculty members".format(counter-1, counter-1)

    
def find_titles(filename):
    input_file = open(filename,'r')
    titles = {} # dictionary of Degrees

    # go through input file line by line
    for line in input_file:
        # before the word Professor find a group of chracters, repeated 1 or more times ([ ]+)
        # that match 1 or more letter, plus 0 or more periods, \s*\w+\.*
        # do same after the word Professor
        titles_match = re.findall(r'\,\s*([\w\s*]*\s*Professor\s*[\w\s*]*)\,', line)

        for title in titles_match:
            #print title
            if title in titles.keys():
                titles[title] +=1
            else:
                titles[title] =1
    for key in sorted(titles.keys()):
        print key, titles[key]
    return len(titles)
  
  
  def find_emails(filename):
    input_file = open(filename,'r')
    emails = []
    counter=0

    for line in input_file:
        # match a group of any number letters, periods and dashes
        # before and after @ 
        email_match = re.search(r'[\w\.-]+@[\w+\.]+',line)

        if email_match:
            emails.append( email_match.group() )
    return emails

  
def find_domains(email_list):
    domains = []

    for a in email_list:
        dom_match = re.search(r'@([\w\.]+)', a)
        if dom_match:

            if dom_match.group(1) not in domains:
                domains.append(dom_match.group(1))
    print domains

    
def save_emails(emails_list):

    text = '\n'.join(emails_list)
    savefile = open('emails.csv', 'w')
    savefile.write(text)
    savefile.close()

    
    
def main():
    print " \n \t PART 1: regex  \n"
    args = sys.argv[1:]

    if not args:
        print " please give a file name"
        sys.exit(1)
    else:
        myfile = args[0]
    #################################### question1 
    print " Question 1 find_degrees(myfile)"
    num = find_degrees(myfile)
    print "the number of different degrees is: " , num

    #################################### question 2
    print " \nQuestion 2 find_titles(myfile)", myfile
    num_titles = find_titles(myfile)
    print "the number of different titles is: ", num_titles

    #################################### question 3
    print "\n Question 3 find_emails(myfile)"
    all_emails = find_emails(myfile)
    print " list of emails: ", all_emails
    #################################### question 4
    print "\n Question 4"
    find_domains(all_emails)


    ## Part 2 ##
    print "\n\n Part 2, only run if -save flag present"
    try:
        args[1] == '-save'
        save_emails(all_emails)
        print "'emails.csv' file created, check your directory"
    except IndexError:
        print ("nothing saved to file; exiting now")
        sys.exit(1)

if __name__ == "__main__":
    main()
