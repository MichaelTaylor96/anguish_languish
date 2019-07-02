import pronouncing as phones
import random
import sys
sys.setrecursionlimit(2000)

sentence = input("Enter a sentence to be translated: ")
sentence = sentence.split()
phone_sent = []
for word in sentence:
    phone_sent.append(phones.phones_for_word(word))
final_sent = []
for phone_word in phone_sent:
    final_sent += phone_word[0].split()
print(final_sent)
trans_sent = []

def rank_words(index):
    with open('words.txt') as file:
        choices = {}
        for word in file.readlines():
            score = 0
            phone_word = phones.phones_for_word(word.strip())[0].split()
            length = len(phone_word)
            if index + length >= len(final_sent):
                continue
            comp_set = final_sent[index:index+length]
            for i, phone in enumerate(phone_word):
                if phone == comp_set[i]:
                    score += 1
            if length not in choices:
                choices[length] = [score, word, phone_word]
            elif score > choices[length][0]:
                choices[length] = [score, word, phone_word]
        return choices


i = 0
choices_at_positions = []
while i < len(final_sent):
    choices_at_positions.append(rank_words(i))
    i += 1
sentences = {}

def pick_translation(index, start, frag):
    translation_choices = []
    blank = False
    if not (choices_at_positions[index]):
        blank = True
    for choice in choices_at_positions[index]:
        frag_right = frag[start + len(choice[2]):-1]
        frag_left = frag[0:start]
        if not (frag_left or frag_right):
            translation_choices.append([choice[1], choice[0]])
            return [choice[1], choice[0]]
        if frag_right:
            new_start = random.randint(0, len(frag_right)-1)
            Rbest = pick_translation(new_start + index + len(choice) - 1, new_start, frag_right)
        else:
            Rbest = [0, ""]
        if frag_left:
            new_start = random.randint(0, len(frag_left)-1)
            Lbest = pick_translation(new_start, new_start, frag_left)
        else:
            Lbest = [0, ""]
        translation_choices.append([choice[1] + Lbest[0] + Rbest[0], choice[0] + Lbest[1] + Rbest[1]])
    if blank:
        return [0, ""]
    sorted_choices = sorted(translation_choices, key=lambda item: item[0])
    return sorted_choices[0]

        
translation = pick_translation(0, 0, final_sent)

print(translation)
            