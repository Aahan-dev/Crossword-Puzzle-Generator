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

        # Try to place the word in the grid
        for _ in range(100):  # Limit attempts to find a valid position
            if direction == 'horizontal':
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - word_length)
            else:
                row = random.randint(0, self.size - word_length)
                col = random.randint(0, self.size - 1)


            # Check if the word fits
            if self.can_place_word(word, row, col, direction):
                for i in range(word_length):
                    if direction == 'horizontal':
                        self.grid[row][col + i] = word[i]  # Place the word
                    else:
                        self.grid[row + i][col] = word[i]  # Place the word
                return True  # Word added successfully
        return False  # Failed to place the word after many attempts


    