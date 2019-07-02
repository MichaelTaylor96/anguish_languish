import pronouncing as phones

sentence = input("Enter a sentence to be translated: ")
sentence = sentence.split()
phone_sent = []
for word in sentence:
    phone_sent.append(phones.phones_for_word(word))
final_sent = []
for phone_word in phone_sent:
    final_sent += phone_word[0].split()
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
for i in range(len(final_sent)):
    sentences[i+1] = [[], 0]

def pick_translation(sent, sentences, sentence):
    for i in range(len(sent)):
        j = i + 1
        remainingPhones = len(sent) - i
        for word in choices_at_positions[i].values():
            if len(word[2]) <= remainingPhones and word[1].strip() not in sentence:
                if sentences[j][1] + word[0] > sentences[j+len(word[2])][1]:
                    sentences[j+len(word[2])] = [sentences[j][0] + [word[1]], sentences[j][1] + word[0]]
    return sentences

        
sentences = pick_translation(final_sent, sentences, sentence)

sentence = [word.strip() for word in sentences[len(final_sent)-1][0]]
print(" ".join(sentence))
            