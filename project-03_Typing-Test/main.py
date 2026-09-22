import time
import random

sentances = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question."
]

def measure_accuracy(user_input, test_sentence):
    correct_chars = sum(1 for a, b in zip(user_input, test_sentence) if a == b)
    accuracy = (correct_chars / len(test_sentence)) * 100 if test_sentence else 0
    return accuracy

def typing_test():
    test_sentence = random.choice(sentances)
    print("Type the following sentence:")
    print(test_sentence)
    input("Press Enter when you're ready to start...")
    start_time = time.time()
    user_input = input("\nStart typing: \n")
    end_time = time.time()
    time_taken = end_time - start_time
    word_count = len(test_sentence.split(" "))

    print("Results:")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Words typed: {word_count}")
    print(f"Typing speed: {word_count / time_taken * 60:.2f} words per minute")
    accuracy = measure_accuracy(test_sentence, user_input)
    print(f"Accuracy: {accuracy:.2f}%")

typing_test()