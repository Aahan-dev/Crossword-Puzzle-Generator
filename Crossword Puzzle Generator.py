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


    def can_place_word(self, word, row, col, direction):
        """
        Check if a word can be placed in the grid at the specified position.


        Args:
            word (str): The word to check.
            row (int): The starting row for placement.
            col (int): The starting column for placement.
            direction (str): The direction to place the word ('horizontal' or 'vertical').


        Returns:
            bool: True if the word can be placed, False otherwise.
        """
        word_length = len(word)


        for i in range(word_length):
            if direction == 'horizontal':
                if self.grid[row][col + i] not in [' ', word[i]]:
                    return False
            else:
                if self.grid[row + i][col] not in [' ', word[i]]:
                    return False
        return True


    def fill_grid(self):
        """Fill the empty spaces in the grid with random letters."""
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col] == ' ':
                    self.grid[row][col] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')




    def display(self):
        """Display the crossword puzzle grid."""
        for row in self.grid:
            print(' '.join(row))




    def generate(self, words):
        """
        Generate the crossword puzzle with the given list of words.




        Args:
            words (list): A list of words to include in the crossword.
        """
        for word in words:
            success = self.add_word(word)
            if not success:
                print(f"Failed to place word: {word}")




        self.fill_grid()  # Fill remaining spaces with random letters




def main():
    """Main function to run the crossword puzzle generator."""
    size = int(input("Enter the size of the crossword (e.g., 10): "))  # Size of the grid
    words = input("Enter words separated by commas: ").upper().split(',')  # User input for words




    crossword = CrosswordPuzzle(size)  # Create a crossword puzzle instance
    crossword.generate(words)  # Generate the puzzle
    crossword.display()  # Display the generated puzzle




if __name__ == "__main__":
    main()  # Run the main function


