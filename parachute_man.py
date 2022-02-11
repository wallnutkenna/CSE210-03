import random

#, "earthworm", "company", "mushroom", "battery", "observation", "question", "departure", "offensive"

class word:
    """Generates random word, turns it into "_", calcs if user guess is right or wrong
"""
    def __init__(self):
        self.word_bank = ["harmony"]
        self.hidden_word = []
        self.word_gen()

    def word_gen(self):
        word = random.choice(self.word_bank)
        for let in word:
            self.hidden_word.append(letter(let))

    def calc_guess(self, guess):
        ret = False #guess incorrect
        # ret = true when correct
        for lett in self.hidden_word:
            ret |= lett.guess_letter(guess)
        return ret

    def complete(self):
        count = 0
        ret = False
        for lett in self.hidden_word:
            if lett.found():
                count += 1
        if count == len(self.hidden_word):
            ret = True
        return ret
    
    def printWord(self):
        currentword = ""
        for lett in self.hidden_word:
            currentword  += lett.toString()
        return currentword

class letter:
    def __init__(self,letter):
        self.letter = letter
        self.discovered = False
    
    def guess_letter(self,newLetter):
        ret = False
        if self.letter == newLetter:
            self.discovered = True
            ret = True
        return ret

    def found(self):
        return self.discovered

    def toString(self):
        ret = ""
        if self.discovered:
            ret = self.letter
        else:
            ret = "_ "
        return ret




if __name__ == "__main__":
    print("TEST")
    test = word()
    print(test.printWord())
    test.calc_guess("h")
    print(test.printWord())
    if test.complete():
        print("Easy")
    test.calc_guess("a")
    print(test.printWord())
    if test.complete():
        print("Easy")
    test.calc_guess("r")
    print(test.printWord())
    if test.complete():
        print("Easy")
    test.calc_guess("m")
    print(test.printWord())
    if test.complete():
        print("Easy")
    test.calc_guess("o")
    print(test.printWord())
    if test.complete():
        print("Easy")
    test.calc_guess("n")
    print(test.printWord())
    if test.complete():
        print("Easy")
    test.calc_guess("y")
    print(test.printWord())
    if test.complete():
        print("Easy")