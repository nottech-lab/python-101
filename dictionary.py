'''
Write a simple script to demonstrate your understanding of dictionaries as data types
'''
def word_frequencies(words_list):
    dictionary = {}

    for word in words_list:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    return dictionary

words_list = ['i', 'messed', 'up', 'tonight', 'i', 'lost', 'another',
                'fight', 'i', 'will', 'still', 'messup', 'now', 'to',
                'see', 'what', 'is', 'next']

print(word_frequencies(words_list))
