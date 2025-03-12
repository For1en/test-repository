#!/bin/python3
from random import choice

words_lists = {1:["apple", "grape", "table", "chair", "stone", "light", "smile", "cloud", "house", "water"],
               2:["banana", "forest", "breeze", "winter", "bottle", "pencil", "sudden", "golden", "throne", "jungle"],
               3:["elephant", "umbrella", "mountain", "chocolate", "adventure", "harmonica", "dolphins", "fantastic", "fireworks", "telephone"]}
        
class Hangman:
    def __init__(self):
        print('Hello gamer!\nThis is hungman game.')
        
        self.word = ''
        self.guessed_letters = []
        self.attempts = 6
        
        
    def level(self):
        
        while True:
            game_level = input('Please select your level by entering a single number --> (1) (2) (3): ')
            if game_level.isdigit() and int(game_level) in words_lists:
                self.word = choice(words_lists[int(game_level)])
                break
            else:
                print('Invalid character, please enter 1, 2, or 3.')
        
        
    def progress(self):
        output = ''.join([j if j in self.guessed_letters else '-' for j in self.word])
        print(f'Your word: {output}\n')
    
    def play(self):
        self.guessed_letters = []
        self.attempts = 6

        while self.attempts > 0:
            self.progress()
            letter = input('Enter your letter: ').lower()
            
            if len(letter) != 1 or not letter.isalpha():
                print('Invalid! Please enter one letter.')
                continue
            
            if letter in self.guessed_letters:
                print("You already guessed that letter. Try again.")
                continue
            
            self.guessed_letters.append(letter)
            
            if letter not in self.word:
                self.attempts -= 1
                print(f"Wrong guess! You have {self.attempts} attempts left.")
                
            if self.win():
                print(f'You guessed the word {self.word}!')
                return 
                  
                  
    def win(self):  
        return all(letter in self.guessed_letters for letter in self.word)
    
    
    def start_game(self):
        while True:
            self.level()
            self.play()
            replay = input("Do you want to play again? (yes/no): ").strip().lower()
            if replay != "yes":
                print("Thanks for playing! Goodbye.")
                break
            

#The start of the game
    
        
if __name__ == "__main__":
    game = Hangman()
    game.start_game()
    