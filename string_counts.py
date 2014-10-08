#!/usr/bin/python

# A highly readable parser with clean syntax
class ClarityParser(object):
    def __init__(self, input_string):
        self.input_string = input_string
        self.split_string = input_string.split()
        
    def parse(self):
        completed_strings = []
        for string in self.split_string:
            if string not in completed_strings:
                # We'll use python's build in string counter (not sure what the runtime is)
                print string + ":", self.input_string.count(string)
                completed_strings.append(string)


# A Trie will complete with O(n) memory where n = len(input) and O(p * q) where p is the number of words and q is the max length of a word
class TimeAndSpaceRuntime(ClarityParser):
    def __init__(self, input_string):
        ClarityParser.__init__(self, input_string)
        self.trie_root = {}

    # Too late I relize that a Trie is really the wrong data structure and I should have used a suffix tree instead
    def parse(self):
        for string in self.split_string:
            walk_element = self.trie_root
            for character in string:
                if character not in walk_element:
                    walk_element[character] = {}
                if "count" in walk_element:
                    walk_element["count"] += 1
                else:
                    walk_element["count"] = 1
                walk_element = walk_element[character]
            walk_element["terminate"] = True
    

                

if __name__ == "__main__":
    input_string = "this is a very very basic sentence and is only an abstract sample"

    parser = ClarityParser(input_string)
    parser.parse()

    parser = TimeAndSpaceRuntime(input_string)
    parser.parse()

