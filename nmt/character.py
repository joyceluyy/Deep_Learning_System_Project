import csv
import sys
import json

csv.field_size_limit(sys.maxsize)

episode =3
line_text =2
speaker = 1
d = {}

name = "../data/scripts.csv"
train = open("../data/train.en", "w")
test = open("../data/test.en", "w")
dev = open("../data/dev.en", "w")

f = open(name)

reader = csv.reader(f)
next(reader)
prevRow = next(reader)

vocab = {"<pad>": 0, "<s>": 1, "</s>": 2, "<unk>": 3}
data = {"tgt_word2id":_vocab}
count = 1

for currRow in reader:
    if currRow[speaker] == "JERRY" and prevRow[episode] == currRow[episode]:
        if int(float(currRow[episode])) <= 15:
            train.write(currRow[line_text] + "\n")
        elif int(float(currRow[episode])) <= 19:
            test.write(currRow[line_text] + "\n")
        else:
            dev.write(currRow[line_text] + "\n")
    for word in currRow[line_text].split(" "):
        if word not in vocab.keys():
            vocab[word] = count
            count += 1
    prevRow = currRow

write_file = open("vocab.json", "w")
json.dump(data, write_file)
