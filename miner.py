# This file contains functions that might come in handy when dealing with text



class TextMiner():
    
    def __init__(self, data):
        self.data = data
        self.chunks = []
        
    
    # input: array
    # output: an array containing a specific word/phrase
    def chunks_width(self, word, left = 20, right = 20):
        for row in self.data:
            good_index = row.find(word)
            self.chunks.append(row[good_index - left:good_index + right].replace("\n", ""))
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
    
   
    
    
    
    
