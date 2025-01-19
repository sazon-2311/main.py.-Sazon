class WordsFinder:
    def __init__(self, *name_file):
        self.name_file = name_file

    def get_all_words(self):
        all_words = {}
        for file_name in self.name_file:
            with open(file_name, 'r', encoding='utf-8') as file:
                line = file.read().lower()
                for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    line = line.replace(punct, ' ')
                words = line.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        dict = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                dict[name] = words.index(word.lower()) + 1
        return dict

    def count(self, word):
        dict = {}
        for name, words in self.get_all_words().items():
            dict[name] = words.count(word.lower())
            return dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
