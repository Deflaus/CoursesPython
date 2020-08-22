
import json
from pprint import pprint
from collections import Counter


def SearchFor6digitsWords(dict_json):
    news_str = ''
    for news in dict_json['rss']['channel']['items']:
        # получили строку состоящую из новостей
        news_str += news['description']

    news_strs = news_str.split()
    # получили отстортированный список из слов от большего количества символов к меньшему
    news_strs.sort(key=len, reverse=True)
    output_list = []
    for word in news_strs:
        if len(word) >= 6:
            output_list.append(word)
    return output_list


def main():
    with open('file.json', encoding='utf-8') as json_file:
        news = json.load(json_file)
    # получили список слов больше 6 знаков отсортированных по убыванию знаков
    output = Counter(SearchFor6digitsWords(news))
    pprint(output.most_common(10))


if __name__ == "__main__":
    main()
