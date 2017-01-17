#!/usr/bin/Python

#billiescodes 2017
# Metis assignment:

# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import sys

def parse_goals(filename):

    input_file = open(filename, 'r')
    count = 0
    difference = []

    for line in input_file:
        if count == 0:
            print "the header: \n", line
            count +=1
            continue

        stats = line.split(",")
        for_goals = int(stats[5])
        against_goals = int(stats[6])
        difference.append((stats[0], abs(for_goals - against_goals) ))

    new =  sorted(difference, key=lambda key: key[1])

    return new[0]

def main():

    print " \n \t Question 8: parsing \n"
    args = sys.argv[1:]

    if not args:
        print "please input a file name"
        sys.exit(1)
    else:
        myfile = args[0]

    smallest_diff = parse_goals(myfile)

    print " the team with the smallest difference in for/against goals is {}, with a difference of {}".format(smallest_diff[0], smallest_diff[1])

if __name__=='__main__':
    main()
