#!/usr/bin/python

def merge_dictionaries(dict1, dict2):
    """ This function will merge these dictionaries and print out the results
        Runtime is O(n log n) where n is len(dict1) + len(dict2)
    """
    for key in sorted(set(dict1.keys() + dict2.keys())):  # O(nlog n). To merge duplicates, I covert the list to a set
        if key in dict1 and key not in dict2:  # O(1)
            print "Dict #1:\t%s -> %d" % (key, dict1[key]) # O(1)
        elif key in dict1 and key in dict2:   # O(1)
            print "Dict #1 & #2\t%s -> [%d,%d]" % (key, dict1[key], dict2[key]) # O(1)
        else:
            print "Dict #2:\t%s -> %d" % (key, dict2[key]) # O(1)



if __name__ == "__main__":
   # A sample run with the example given in the problem description
   merge_dictionaries({
        'd': 53,
        're': 23,
        'a': 44,
    },
    {
        'b': 3,
        'd': 32,
        'were': 43,
    }
)
