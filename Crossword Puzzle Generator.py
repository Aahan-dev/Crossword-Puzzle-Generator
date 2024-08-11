import random

class CrosswordPuzzle:
    def __init__(self, size=10):
        """Initialize the crossword puzzle with a given size."""
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]  # Create an empty grid

    def add_word(self, word):
        """
        Add a word to the grid either horizontally or vertically.

        Args:
            word (str): The word to add to the grid.

        Returns:
            bool: True if the word was added successfully, False otherwise.
        """
        word_length = len(word)
        direction = random.choice(['horizontal', 'vertical'])  # Randomly choose direction

        