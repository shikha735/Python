import requests
from bs4 import BeautifulSoup
import operator

fw = open('words.txt', 'w')


def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")
    for content_words in soup.findAll('a', {'rel': 'bookmark'}):
        content = content_words.string
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    removeSymbols(word_list)


def removeSymbols(word_list):
    final_word_list = []
    symbols = "~`!@#$%^&*()_+=-';:\"{}[],\./<>?|"
    for word in word_list:
        for i in range(len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            final_word_list.append(word)
    word_dictionary(final_word_list)


def word_dictionary(final_word_list):
    word_count = {}
    for word in final_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for dict_key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        fw.write(dict_key + ' ' + str(value) + '\n')

    fw.close()
start('http://www.geeksforgeeks.org')
