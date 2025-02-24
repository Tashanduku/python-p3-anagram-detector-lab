# your code goes here!
# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word.lower() 
        self.sorted_word = sorted(self.word)  
    def match(self, word_list):
        
        return [word for word in word_list if sorted(word.lower()) == self.sorted_word and word.lower() != self.word]

# Example usage:
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))  # Output: ['inlets']
