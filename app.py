# Program to get total number of badges and number of points of specific subject from teamtreehouse

# Import statements
import profile  # Module to get profile data
import sys # Module for reading in command line args
from itertools import izip # Module to help loop through list two at a time

# Functions

# Function to turn (1, 2, 3, 4) to ((1, 2), (3, 4))
def pairwise(iterable):
    "s -> (s0,s1), (s2,s3), (s4, s5), ..."
    a = iter(iterable)
    return izip(a, a)

# Global Variables
people = [] # List of people to get data from

for name, subject in pairwise(sys.argv[1:]):
   people.append({"username": name, "subject": subject})


for person in people:
	profile.get(person["username"], person["subject"])