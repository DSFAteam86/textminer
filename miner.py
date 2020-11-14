# This file contains functions that might come in handy when dealing with text
from nltk.corpus import stopwords
import re
import unidecode
import nltk
nltk.download('stopwords')
esp_stopwords = stopwords.words('spanish')


class TextMiner():

    def __init__(self, data):
        self.data = data
        self.chunks = []

    def chunks_width(self, word, left=20, right=20):
        for text in self.data:
            good_index = text.find(word)
            self.chunks.append(
                text[good_index - left:good_index + right].replace("\n", ""))
        return self.chunks

    def find_all(self, word):
        findings = []
        for text in self.data:
            findings.append([m.start() for m in re.finditer(word, text)])
        return findings

    def get_chunks_width(self, word, left=20, right=20):
        index = 0
        for positions in self.find_all(word):
            for current_pos in positions:
                self.chunks.append(
                    self.data[index][current_pos - left:current_pos + right].replace("\n", ""))
            index = index + 1

        return self.chunks

    def get_chunks_in_array(self, arr, left=20, right=20):
        clean_chunks = []
        chunks = []
        for value in arr:
            chunks += (self.get_chunks_width(value, left, right))

        for value in chunks:
            if value not in clean_chunks:
                clean_chunks.append(value)

        self.data = clean_chunks
        return clean_chunks

    def extract_exact(self, func):
        ccs = []
        for chunk in self.get_data():
            word_tokens = nltk.word_tokenize(chunk)
            word_tokens_clean = [each for each in word_tokens if each.lower(
            ) not in esp_stopwords and len(each.lower()) > 2]
            for word in word_tokens_clean:
                if func(word):
                    ccs.append(func(word))
        self.data = ccs
        return ccs

    def numbers_only(self, data):
        numbers = []
        for chunk in data:
            numeric_filter = filter(str.isdigit, chunk)
            numeric_string = "".join(numeric_filter)
            numbers.append(numeric_string)
        return numbers

    def get_data(self):
        return self.data
