import pronouncing as phones
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
with open('words.txt') as file:
    index = 0
    for word in file.readlines():
        if index >= len(final_sent)-1:
            break
        score = 0
        phone_word = phones.phones_for_word(word.strip())[0].split()
        if index + len(phone_word) >= len(final_sent)-1:
            continue
        comp_set = final_sent[index:index+len(phone_word)]
        print(comp_set)
        for i, phone in enumerate(phone_word):
            if phone == comp_set[i]:
                score += 1
        if len(phone_word)-1 > score > len(phone_word)-3 and len(phone_word) > 2:
            trans_sent.append(word.strip())
            index += len(phone_word)
print(trans_sent)
            