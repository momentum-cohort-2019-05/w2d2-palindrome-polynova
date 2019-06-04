sentence = input("Give me sentences right now!")
print(sentence)

# all_letters = "abcdefghijklmnopqrstuvwxyz"
# found_letters = []
# for letter in sentence.lower():
#     if letter in all_letters and letter not in found_letters:
#         found_letters.append(letter)

# print(found_letters)

def clean_text(text):
    """
    Given a text, return the text with no spaces or punctuation and all lowercased.
    """
    new_text = ""
    text = text.lower()
    for character in text:
        if character.isalpha():
            new_text = new_text + character
    return new_text

cleanned_sentence = clean_text(sentence)
reverse_sentence = cleanned_sentence[::-1]

if cleanned_sentence == reverse_sentence:
    print ("It is a palindrome")

elif cleanned_sentence != reverse_sentence:
    print ("This is not a palindrome")



