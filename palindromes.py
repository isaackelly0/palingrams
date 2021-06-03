"""Find palindromes in a dictionary file"""
from load_dictionary import load
word_list = load('read book for text file address')
pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print("\nNumber of palindromes found ={}\n".format(len(pali_list)))
print(*pali_list, sep='\n')