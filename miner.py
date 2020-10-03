# This file contains functions that might come in handy when dealing with text
import re
import unidecode
import nltk

class TextMiner():
    
    def __init__(self, data):
        self.data = data
        self.chunks = []
    
    # input: array
    # output: an array containing a specific word/phrase (only retuns first occurrence)
    def chunks_width(self, word, left = 20, right = 20):
        for text in self.data:
            good_index = text.find(word)
            self.chunks.append(text[good_index - left:good_index + right].replace("\n", ""))
        return self.chunks
    
    # input: search a word
    # output: an array in which each item is an array, 
    # every item has indexes of ocurrences for every page
    def find_all(self, word):
        findings = []
        for text in self.data:
            findings.append([m.start() for m in re.finditer(word, text)])
        return findings
    
    # find all ocurrences of a word
    # and return an array with chunks that contain that word
    def get_chunks_width(self, word, left=20, right=20):
        index = 0
        for positions in self.find_all(word):
            for current_pos in positions:
                self.chunks.append(self.data[index][current_pos - left:current_pos + right].replace("\n", ""))
                
            index = index + 1
        
        return self.chunks

    # get all the numbers in a string
    def numbers_only(self):
        numbers = []
        for chunk in self.chunks:
            numeric_filter = filter(str.isdigit, chunk)
            numeric_string = "".join(numeric_filter)
            numbers.append(numeric_string)
        return numbers
    
    # getters
    def get_data(self):
        return self.data
    

    
    
    
    
