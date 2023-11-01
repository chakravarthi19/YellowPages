AnanList = ['cat', 'dog', 'god', 'tca', 'act']


def find_args(words_list):
    anagram_groups = {}
    for word in words_list:
        sorted_word = "".join(sorted(word))
        if sorted_word not in anagram_groups:
            anagram_groups[sorted_word] = []
        anagram_groups[sorted_word].append(word)
    print(anagram_groups)
    for ii in anagram_groups.values():
        print(ii)


find_args(AnanList)
