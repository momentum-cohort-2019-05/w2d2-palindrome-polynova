user_sentence = input("Give me sentences right now!")
print(user_sentence)

sentence = user_sentence 
all_letters = "abcdefghijklmnopqrstuvwxyz"
found_letters = []
for letter in sentence.lower():
    if letter in all_letters and letter not in found_letters:
        found_letters.append(letter)

print(found_letters)

