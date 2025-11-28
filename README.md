# NYT Spelling Bee Solver

## The Rules

The NYT Spelling Bee game is a word game where you are given a list of 7 letters, one of which is the 'center' letter. Your goal is to find words that can be formed from the letters, and the words must contain the center letter. A valid word must be at least 4 letters long. A valid word must be an English word found in the dictionary. Note that every letter can be used more than once.

## The Solution

The solution to the NYT Spelling Bee game is to use a dictionary of valid English words. The dictionary is a JSON file that contains a list of words, one word per line. The words are sorted by word length, so the longest words are at the top of the file.

The solution is to read the dictionary file, and then for each word, check if it can be formed from the letters and the center letter. If it can, add it to the list of valid words. Then, sort the list of valid words by word length, and print the list.

## The Code

The code is a Python script that reads the dictionary file, and then for each word, check if it can be formed from the letters and the center letter. If it can, add it to the list of valid words. Then, sort the list of valid words by word length, and print the list.

## Credits

@dwyl for the list of english words, which you can find at the following repo:

https://github.com/dwyl/english-words
