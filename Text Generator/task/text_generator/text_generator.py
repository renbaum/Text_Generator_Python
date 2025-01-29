# Write your code here
import re
import random

from nltk import ngrams
import sys
from os.path import expanduser

class Tails:
    def __init__(self, tail: str = None):
        self.tails = {}
        if tail is not None:
            self.add(tail)

    def add(self, tail):
        if tail in self.tails:
            self.tails[tail] += 1
        else:
            self.tails[tail] = 1

    def print_tails(self):
        for tail, count in self.tails.items():
            print(f"Tail: {tail}\tCount: {count}")

    def get_keys_sorted_by_values(self) -> list:
        return sorted(self.tails, key=self.tails.get, reverse=True)
    
    def get_most_probable_tail(self, not_end: bool) -> str:
        sorted_keys = self.get_keys_sorted_by_values()

        for tail in sorted_keys:
            if is_end_of_sentence(tail) and not_end:
                continue
            return tail

        return ""

def is_end_of_sentence(word: str) -> bool:
    try:
        return word[-1] in ".!?"
    except IndexError:
        return False

class Bigrams:
    def __init__(self, bigram: tuple = None):
        self.bigrams = {}
        if bigram is not None:
            self.add(bigram)


    def add(self, bigram: tuple):
        head1, head2, tail = bigram
        key = tuple([head1, head2])
        if key not in self.bigrams:
            self.bigrams[key] = Tails(tail)
        else:
            self.bigrams[key].add(tail)

    def print_bigrams(self, head: str):
        print(f"Head: {head}")
        if head not in self.bigrams:
            print("Key Error. The requested word is not in the model. Please input another word.")
            print()
            return

        self.bigrams[head].print_tails()
        print()

    def get_sentence(self, head: tuple, n: int) -> list:
        lst = []
        if head not in self.bigrams:
            head = self.get_random_head()
#            return lst

        lst.extend(head)
        cnt = 1
        while True:
#        for i in range(n-1):
            tail = self.bigrams[head].get_most_probable_tail(cnt < 5)
            lst.append(tail)
            head = lst[-2], lst[-1]
            if head not in self.bigrams:
                break
            cnt += 1
            if is_end_of_sentence(tail):
                break
        return lst

    def get_most_probable_tail(self, head: tuple, not_end: bool) -> str:
        if head not in self.bigrams:
            return ""
        return self.bigrams[head].get_most_probable_tail(not_end)

    def get_random_head(self) -> list:
        while True:
            lst = random.choice(list(self.bigrams.keys()))
            if not is_end_of_sentence(lst[0]) and re.match(r"[A-Z]", lst[0]):
                return lst

filename = input()

with open(filename, "r", encoding="utf-8") as file:
    corpus = file.read()

n = 3
n_grams = ngrams(corpus.split(), n)
#tokens = re.split(r"[\s ]", corpus)
b = Bigrams()
for grams in n_grams:
    b.add(grams)
#lst = [Bigrams(grams) for grams in n_grams]

#print(f"Number of bigrams: {len(lst)}")

#print("Corpus statistics")
#print(f"All tokens: {len(tokens)}")
#print(f"Unique tokens: {len(set(tokens))}")

head = b.get_random_head()
for _ in range(10):
    l = b.get_sentence(head, 10)
    print(" ".join(l))
    tail = b.get_most_probable_tail((l[-2], l[-1]), True)
    head = head[1], tail

'''
while True:
    cmd = input()
    match cmd.lower():
        case "exit":
            break
        case _:
            try:
                b.print_bigrams(cmd)
            except TypeError:
                print("Type Error. Please input an integer.")
            except ValueError:
                print("Type Error. Please input an integer.")
            except IndexError:
                print("Index Error. Please input an integer that is in the range of the corpus.")
'''