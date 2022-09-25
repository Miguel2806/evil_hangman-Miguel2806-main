from __future__ import annotations
from collections import defaultdict # You might find this useful
import os

"""
************** READ THIS ***************
************** READ THIS ***************
************** READ THIS ***************
************** READ THIS ***************
************** READ THIS ***************

If you worked in a group on this project, please type the EIDs of your groupmates below (do not include yourself).
Leave it as TODO otherwise.
Groupmate 1: TODO
Groupmate 2: TODO
"""

class WordMakerHuman():
    def __init__(self, words_file, verbose):
        # we need to prompt the player for a word, then clear the screen so that player 2 doesn't see the word.
        self.verbose = verbose
        self.words = {} # Make sure that you understand dictionaries. They will be extremely useful for this project.
        with open(words_file) as wordfile:
            for line in wordfile:
                word = line.strip()
                if len(word) > 0:
                    self.words[word] = True # I could have made this a set() instead.

    def reset(self, word_length):
        # Your AI code should not call input() or print().
        question = ""
        while True:
            question = input(f"Please type in your word of length {word_length}: ")
            if question in self.words and len(question) == word_length:
                break
            print("Invalid word.")
        if not self.verbose:
            print("\n" * 100) # Clear the screen
        self.word = question

    def get_valid_word(self):
        return self.word

    def get_amount_of_valid_words(self):
        return 1 # the only possible word is self.word

    def guess(self, guess_letter):
        idx = self.word.find(guess_letter)
        ret = []
        while idx != -1:
            ret.append(idx)
            idx = self.word.find(guess_letter, idx + 1)
        return ret




class WordMakerAI():
    """
    A new WordMakerAI is instantiated every time you launch the game with evil_hangman.py.
    (However, the test harness can make multiple instances.)
    Between games, the reset() function is called. This should clear any internal gamestate that you have.
    The number of guesses, input gathering, winning, losing, etc. is all managed by the GameManager, so you don't
     have to prompt the user at all. All you need to do is keep track of the active dictionary of still-valid words
     in this game.

    Do not assume anything about the lengths of the words. You will be tested on dictionaries with extremely long words.
    """
    def __init__(self, words_file: str, verbose=False):

        self.verbose = verbose
        self.words={}
        self.words_tmp=[]

        # The chosen data structure is a dictionary where the key is a number and the value is a list with
        # all the words that have that number of letters

        with open(words_file) as file_obj:
            for line in file_obj:
                word = line.strip()
                n=len(word)
                if n>0:
                    if n in list(self.words.keys()):
                        self.words[n].append(word)
                    else:
                        self.words[n]=[]
                        self.words[n].append(word)
                # Use word


        pass # TODO: implement this

    def reset(self, word_length: int) -> None:

        self.words_tmp=[]
        self.words_tmp=self.words[word_length]

        # Every reset is just to pull from the dictionary the words with the right amount of letters.  Since the data
        # structure is a dictionary with the number of letter as a key, this is a O(1) process.
        # The self.words_tmp is a list that contains all the words that satisfies the current conditions.

        pass # TODO: implement this

    def get_valid_word(self) -> str:
        # This function deliver just the first word in the words_temp list (that always satisfies the conditions)
        return self.words_tmp[0]

        pass # TODO: implement this

    def get_amount_of_valid_words(self) -> int:
        # This functions just deliver the amount of words in the list words_tmp (satisfies all the conditions)
        return len(self.words_tmp)
        pass # TODO: implement this

    def get_letter_positions_in_word(self, word: str, guess_letter: str) -> tuple[int, ...]:
        # This function is almost the same that normal hangman uses.   The difference is this function needs a word as input.
        idx = word.find(guess_letter)
        result = []
        while idx != -1:
            result.append(idx)
            idx = word.find(guess_letter, idx + 1)
        return tuple(result)
        # TODO: add letters to result


    def guess(self, guess_letter) -> list[int]:

        # First, a list call c has the positions in all the words in words_tmp
        c=[]
        tmp={}
        for i in self.words_tmp:
            tmp[i] = self.get_letter_positions_in_word(i,guess_letter)
            c.append(tmp[i])

        # Then, a new dictionary, where the key is the how many words has certain positions, and the value is the list with
        # the positions that has the same numbers of words.
        cdict={}
        for i in c:
            if c.count(i) in list(cdict.keys()):
                cdict[c.count(i)].add(i)
            else:
                cdict[c.count(i)]=set([])
                cdict[c.count(i)].add(i)

        n=max(cdict.keys())  # maximum number of words with the same condition.
        l=list(cdict[n])

        # The following iteration get the "smaller" numbers of positions (to leave fewer guesses)
        h=len(l[0])
        j=l[0]
        for i in l:
            if len(i)<h:
                j=i
                h=len(i)

        # Create a new words_tmp that satisfies the new condition
        self.words_tmp=[]
        for i in tmp:
            if tmp[i] == j:
                self.words_tmp.append(i)

        return list(j)
        
        pass # TODO: implement this
