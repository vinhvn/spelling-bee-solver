# the nyt spelling bee game is a game where you are given a list of 7 letters, one of which is the 'center' letter.
# you need to find words that can be formed from the letters, and the words must contain the center letter.
# a valid word must be at least 4 letters long.
# a valid word must be an english word found in the dictionary.
# note that every letter can be used more than once.

import json


# a function to load the dictionary of valid english words.
def load_dictionary():
    # import dictionary from json
    # credit to https://github.com/dwyl/english-words
    with open("words_dictionary.json", "r") as file:
        # return a dictionary with the word as the key and the word length as the value, and remove all words that are less than 4 letters long
        return {word: n for word in json.load(file) if (n := len(word)) >= 4}


# a function to return all valid words that can be formed from the letters and the center letter.
def get_valid_words(letters, center_letter, dictionary):
    # basic checks
    if len(letters) != 6:
        return []
    if len(center_letter) != 1:
        return []
    allowed_letters = set(letters) | {center_letter}
    return [
        word
        for word in dictionary
        if center_letter in word and set(word).issubset(allowed_letters)
    ]


# a function that returns the sorted list of valid words by word length.
def spelling_bee(letters, center_letter, dictionary):
    valid_words = get_valid_words(letters, center_letter, dictionary)
    return sorted(valid_words, key=lambda x: dictionary[x])


if __name__ == "__main__":
    # load the dictionary
    dictionary = load_dictionary()
    # get the list of 6 non-center letters and the center letter from user input
    letters = list(input("Enter the 6 non-center letters: "))
    print(letters)
    center_letter = input("Enter the center letter: ")
    print(center_letter)
    # print the list of valid answers
    answers = spelling_bee(letters, center_letter, dictionary)
    # print the number of answers
    print(f"Number of answers: {len(answers)}")
    for word in answers:
        print(word)
