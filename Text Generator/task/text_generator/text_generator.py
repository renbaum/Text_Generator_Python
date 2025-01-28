# Write your code here
import re
import sys
from os.path import expanduser

filename = input()

with open(filename, "r", encoding="utf-8") as file:
    corpus = file.read()

tokens = re.split(r"[\s ]", corpus)

print("Corpus statistics")
print(f"All tokens: {len(tokens)}")
print(f"Unique tokens: {len(set(tokens))}")

print()
while True:
    cmd = input()
    match cmd.lower():
        case "exit":
            break
        case _:
            try:
                index = int(cmd)
                print(tokens[index])
            except TypeError:
                print("Type Error. Please input an integer.")
            except ValueError:
                print("Type Error. Please input an integer.")
            except IndexError:
                print("Index Error. Please input an integer that is in the range of the corpus.")
