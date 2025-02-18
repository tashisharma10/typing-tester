import random
import time

def generate_random_sentence():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Programming is fun and rewarding.",
        "Python is a versatile programming language.",
        "Practice makes perfect.",
        "Coding is an essential skill for developers.",
        "All the wheels on the bus go round and round",
        "In a world full of tigers become a lion"
    ]
    return random.choice(sentences)

def typing_speed_test():
    sentence = generate_random_sentence()
    print("Type the following sentence as quickly as possible:")
    print("\n" + sentence + "\n")

    input("Press Enter to start...")

    start_time = time.time()

    user_input = input("Type the sentence here: ")

    end_time = time.time()

    elapsed_time = end_time - start_time

    words = sentence.split()
    word_count = len(words)

    correct_words = 0

    for i in range(min(len(words), len(user_input.split()))):
        if words[i] == user_input.split()[i]:
            correct_words += 1

    wpm = (correct_words / elapsed_time) * 60

    print("\nYou typed at {:.2f} words per minute.".format(wpm))
    print("You got {} out of {} words correct.".format(correct_words, word_count))

if __name__ == "__main__":
    typing_speed_test()
