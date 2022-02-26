import random
from ParachuteGuy import Parachute

def main():
    again = "y"
    while (again.lower() == "y"):
        game = play_game()
        if not game.check_win():
            again = input("Game over! Play again? (y/n): ")
        else:
            again = input("Congrats! You guessed the word! Play again? (y/n): ")
    print("Bye!")

class play_game:

    def __init__(self):
        self.game_parachute = Parachute()
        self.game_word = word()
        self.game_word.new_word()
        print(self.game_word.printWord())
        while(not self.game_parachute.is_guy_dead() and not self.check_win()):
            self.player_turn()
        
    def player_turn(self):
        correct = self.player_guess()
        self.game_parachute.get_parachute(correct)
        print(self.game_word.printWord())

            

    def check_win(self):
        return self.game_word.complete()
        
    
    def player_guess(self):
        return self.game_word.calc_guess(input("What is your guess? ").lower())



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

    # def word_test():
    #     test = word()
    #     test._word_bank = ["harmony"]
    #     test.new_word()
    #     count = 0
    #     print("TEST")
    #     print(test.printWord())
    #     test.calc_guess("h")
    #     print(test.printWord())
    #     if test.complete():
    #         print("Easy")
    #         count += 1
    #     test.calc_guess("a")
    #     print(test.printWord())
    #     if test.complete():
    #         print("Easy")
    #         count += 1
    #     test.calc_guess("r")
    #     print(test.printWord())
    #     if test.complete():
    #         print("Easy")
    #         count += 1
    #     test.calc_guess("m")
    #     print(test.printWord())
    #     if test.complete():
    #         print("Easy")
    #         count += 1
    #     test.calc_guess("o")
    #     print(test.printWord())
    #     if test.complete():
    #         print("Easy")
    #         count += 1
    #     test.calc_guess("n")
    #     print(test.printWord())
    #     if test.complete():
    #         print("Easy")
    #         count += 1
    #     test.calc_guess("y")
    #     print(test.printWord())
    #     if test.complete():
    #         print("Easy")
    #         count += 1
    #     if count == 1:
    #         print("internal test passed")


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
    main()  