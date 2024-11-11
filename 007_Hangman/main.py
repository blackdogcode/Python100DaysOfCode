# https://hangmanwordgame.com/
import os
import random
import hangman_art
import hangman_words


# def clear():
#     # for windows
#     if os.name == 'nt':
#         _ = os.system('cls')
#     # for mac and linux
#     else:
#         _ = os.system('clear')


def all_indices_letter_in_word(word: str, target_letter: str) -> list:
    indices = []
    for idx in range(len(word)):
        if word[idx] == target_letter:
            indices.append(idx)
    return indices


print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
# print(chosen_word)

guess_word = []
for _ in range(len(chosen_word)):
    guess_word.append("_")

guess_letters = set()
remain_life = len(hangman_art.stages)
while "_" in guess_word and remain_life != 0:
    # clear()
    print('Word to Guess: ' + ''.join(guess_word))
    letter = input("Guess a letter: ").lower()

    if letter in guess_letters:
        print(f"You already guessed {letter} try another letter")
        continue
    else:
        letter_indices = all_indices_letter_in_word(chosen_word, letter)
        if not letter_indices:
            remain_life -= 1
        else:
            for index in letter_indices:
                guess_word[index] = letter
        print(''.join(guess_word))
    guess_letters.add(letter)

    if remain_life < len(hangman_art.stages):
        print(hangman_art.stages[remain_life])
    print(f"**********{remain_life}/{len(hangman_art.stages)} LIVES LEFT**********")

if remain_life != 0:
    print("You win!")
else:
    print("You lose!")
