# Write your code here
import re
from nltk import ngrams
import sys
from os.path import expanduser

filename = input()

with open(filename, "r", encoding="utf-8") as file:
    corpus = file.read()

n = 2
n_grams = ngrams(corpus.split(), n)
#tokens = re.split(r"[\s ]", corpus)
lst = [grams for grams in n_grams]
print(f"Number of bigrams: {len(lst)}")

#print("Corpus statistics")
#print(f"All tokens: {len(tokens)}")
#print(f"Unique tokens: {len(set(tokens))}")

print()
while True:
    cmd = input()
    match cmd.lower():
        case "exit":
            break
        case _:
            try:
                index = int(cmd)
                print(f"Head: {lst[index][0]}\tTail: {lst[index][1]}")
            except TypeError:
                print("Type Error. Please input an integer.")
            except ValueError:
                print("Type Error. Please input an integer.")
            except IndexError:
                print("Index Error. Please input an integer that is in the range of the corpus.")
