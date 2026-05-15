import time
import random

words_list = [
    "python",
    "coding",
    "improves",
    "logic",
    "skills",
    "practice",
    "typing",
    "computer",
    "learning",
    "technology",
    "programming",
    "students",
    "projects",
    "development",
    "creative"
]


sentence = ""

for i in range(6):
    random_word = random.choice(words_list)
    sentence = sentence + random_word + " "

print("===== Typing Speed Tester =====\n")
print("Type the following sentence:\n")
print(sentence)
input("\nPress Enter when you are ready...")

start_time = time.time()
typed_text = input("\nStart typing: ")
end_time = time.time()
time_taken = end_time - start_time

words = len(sentence.split())
wpm = (words / time_taken) * 60
correct_characters = 0

for i in range(min(len(sentence), len(typed_text))):
    if sentence[i] == typed_text[i]:
        correct_characters = correct_characters + 1

accuracy = (
    correct_characters / len(sentence)
) * 100

print("\n===== Results =====")
print("Time Taken:", round(time_taken, 2), "seconds")
print("Typing Speed:", round(wpm, 2), "WPM")
print("Accuracy:", round(accuracy, 2), "%")