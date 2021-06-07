"""Find word-pair palingrams in a dictionary file"""
from load_dictionary import load
import time
word_list = load('./lang/International/2of4brif.txt')
#find word pairs
def find_palingrams():
    """find dictionary palingrams"""
    pali_list = []
    words = set(word_list)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-1]and rev_word[end-1:]in words:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-1:]and rev_word[:end-1]in words:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list
start_time = time.time()
palingrams = find_palingrams()
end_time = time.time()

#sort palingrams on first word
palingrams_sorted = sorted(palingrams)

#display palingrams
print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}".format(first, second))

print("Runtime for this program was {} seconds".format(end_time - start_time))