"""Find word-pair palingrams in a dictionary file"""
from load_dictionary import load
word_list = load('./lang/International/2of4brif.txt')
#find word pairs
def find_palingrams():
    """find dictionary palingrams"""
    pali_list = []

    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-1]and rev_word[end-1:]in word_list:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-1:]and rev_word[:end-1]in word_list:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list

palingrams = find_palingrams()

#sort palingrams on first word
palingrams_sorted = sorted(palingrams)

#display palingrams
print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}".format(first, second))