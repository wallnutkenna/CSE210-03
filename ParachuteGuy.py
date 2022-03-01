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

    def  _is_guy_dead(self):
        """A method to define if the parachute guy is dead."""
        
        if len(self._parachute) == 0:
            is_guy_dead = True

        return is_guy_dead
