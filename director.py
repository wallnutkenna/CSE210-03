from ParachuteGuy import Parachute
from word import word

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        ParachuteGuy : The player's lifes count.
        is_playing (boolean): Whether or not to keep playing.
        word : A random word the player needs to guess to win.
        letter : For chicking if the letter input by the player is correct.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._ParachuteGuy = Parachute()
        self._is_playing = True
        self._is_word_complete = False
        self._word = word()

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._get_word()
        print (self._word.printWord())
        while self._is_playing:
            user_input = self._get_inputs()
            correct_input = self._verify_input(user_input)
            print (self._word.printWord())
            self._get_jumper(correct_input)
            self._keep_playing()   
            self._complete()  

            if self._is_word_complete == True: 
                print ("Well done!")
                break

    def _get_word(self):
        """Generates a random word for the player to guess."""
        self._word.new_word()

    def _get_inputs(self):
        """Gets a letter input by the player.
        """
        letter_guess = input("\nGuess a letter [a-z]: ")
        return letter_guess

    def _verify_input(self, user_input):
        """Veryfies if the user input letter is among the secret word's
        letter.
        """
        correct_input = self._word.calc_guess(user_input)
        return correct_input

    def _get_jumper (self, correct_input):
        """Print the Jumper guy and the parachute.
        
        Attributes:
            correct_input (True/False): defines if the letter input by the
            player is correct or wrong.
        """
        self._ParachuteGuy.get_parachute(correct_input)

    def _keep_playing(self):
        """A method to define if the parachute guy is dead."""
        if self._ParachuteGuy._is_guy_dead == True:
            self._is_playing = False

    def _complete(self):
        """A method to define if the word has been completed."""
        complete_word = self._word._complete
        return complete_word
        