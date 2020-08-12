import xml.etree.ElementTree as ET
from pprint import pprint
from collections import Counter


def SearchFor6digitsWords(list):
    news_str = ''
    for news in list:
        news_str += news  # получили строку состоящую из новостей

    news_strs = news_str.split()
    # получили отстортированный список из слов от большего количества символов к меньшему
    news_strs.sort(key=len, reverse=True)
    output_list = []
    for word in news_strs:
        if len(word) >= 6:
            output_list.append(word)
    return output_list


def main():
    news = []
    tree = ET.parse('file.xml')
    root = tree.getroot()
    descriptions = root.findall('channel/item/description')
    for text in descriptions:
        news.append(text.text)
    # получили список слов больше 6 знаков отсортированных по убыванию знаков
    output = Counter(SearchFor6digitsWords(news))
    pprint(output.most_common(10))


if __name__ == "__main__":
    main()
