import random


class Parachute:
    """This class will display the Jumper guy with a parachute.
    Every time the player guesses a letter from the secret word wrong,
    a line from the parachute will be erased."""

    def __init__(self):
        """Constructs a new jumper guy."""
        # A list of remaining attempts for the player to input letters
        # represented by the parachute parts.
        self._parachute = ["  ___  ", " /___\ ", " \   / ", "  \ /  ", "   |   "]
    def get_parachute (self, input_letter):
        """This method will print the Jumper and the parachute.
        
        Attributes:
            input_letter (True/False): defines if the letter input by the
            player is correct or wrong. 
        """
        
        # If the letter input by the player is in the word, the parachute
        # will display as it was.
        if input_letter == True:
            for i in self._parachute:
                print (i)
        # If the letter input by the player is not in the word, a part of
        # the parachute will be erased. 
        else:
            self._parachute.pop(0)
            for i in self._parachute:
                print (i)
        # If the jumper still has parachute, the head will be "O"
        # but once the parachute is over, the head turns to "X"
        head = lambda parachute_length: "   X   " if (parachute_length == 0) else "   O   "
        print (head (len(self._parachute)))
        print ("  /|\  ")
        print ("  / \  ")   

    def  is_guy_dead(self):
        """A method to define if the parachute guy is dead."""
        if len(self._parachute) == 0:
            is_guy_dead = True

        return is_guy_dead


#, "earthworm", "company", "mushroom", "battery", "observation", "question", "departure", "offensive"

class word:
    """Generates random word, turns it into "_", calcs if user guess is right or wrong
"""
    def __init__(self):
        self._word_bank = ["harmony", "earthworm", "company", "mushroom", "battery", "observation", "question", "departure", "offensive"]
        self._hidden_word = []

    def new_word(self):
        word = random.choice(self._word_bank)
        for let in word:
            self._hidden_word.append(letter(let))

    def calc_guess(self, guess):
        ret = False #guess incorrect
        # ret = true when correct
        for lett in self._hidden_word:
            ret |= lett.guess_letter(guess)
        return ret

    def complete(self):
        count = 0
        ret = False
        for lett in self._hidden_word:
            if lett.found():
                count += 1
        if count == len(self._hidden_word):
            ret = True
        return ret
    
    def printWord(self):
        currentword = ""
        for lett in self._hidden_word:
            currentword  += lett.toString()
        return currentword

    def word_test():
        test = word()
        test._word_bank = ["harmony"]
        test.new_word()
        count = 0
        print("TEST")
        print(test.printWord())
        test.calc_guess("h")
        print(test.printWord())
        if test.complete():
            print("Easy")
            count += 1
        test.calc_guess("a")
        print(test.printWord())
        if test.complete():
            print("Easy")
            count += 1
        test.calc_guess("r")
        print(test.printWord())
        if test.complete():
            print("Easy")
            count += 1
        test.calc_guess("m")
        print(test.printWord())
        if test.complete():
            print("Easy")
            count += 1
        test.calc_guess("o")
        print(test.printWord())
        if test.complete():
            print("Easy")
            count += 1
        test.calc_guess("n")
        print(test.printWord())
        if test.complete():
            print("Easy")
            count += 1
        test.calc_guess("y")
        print(test.printWord())
        if test.complete():
            print("Easy")
            count += 1
        if count == 1:
            print("internal test passed")


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
    print("put main here")