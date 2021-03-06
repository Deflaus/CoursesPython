import requests


class GetCountries:
    def __init__(self, url, path_out):
        self.wr_file = open(path_out, 'w', encoding='utf8')
        self.json = requests.get(url).json()
        self.counter = -1
        self.limit = len(self.json)

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < (self.limit - 1):
            self.counter += 1
            outdata = self.json[self.counter]['name']['common'] + ' - ' + 'https://en.wikipedia.org/wiki/' + self.json[self.counter]['name']['common'].replace(" ", "_") + '\n'
            return self.wr_file.write(outdata)
        else:
            raise StopIteration


if __name__ == "__main__":
    for item in GetCountries('https://raw.githubusercontent.com/mledoze/countries/master/countries.json', 'output.txt'):
        pass
