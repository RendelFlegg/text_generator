import nltk
from nltk.tokenize import regexp_tokenize


class TextGenerator:
    def __init__(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            self.corpus = f.read()
        self.tokens = regexp_tokenize(self.corpus, r'\S+')
        self.bigrams = list(nltk.bigrams(self.tokens))

    def show_info(self):
        print(f'Corpus statistics\n'
              f'All tokens: {len(self.tokens)}\n'
              f'Unique tokens: {len(set(self.tokens))}\n')

    def print_tokens(self):
        while True:
            try:
                user_input = input()
                if user_input == 'exit':
                    break
                idx = int(user_input)
                print(self.tokens[idx])
            except IndexError:
                print('Index Error. Please input an integer that is in the range of the corpus.')
            except ValueError:
                print('Type Error. Please input an integer.')

    def print_bigrams(self):
        while True:
            try:
                user_input = input()
                if user_input == 'exit':
                    break
                idx = int(user_input)
                bigram = self.bigrams[idx]
                print(f'Head: {bigram[0]} Tail: {bigram[1]}')
            except IndexError:
                print('Index Error. Please input an integer that is in the range of the corpus.')
            except ValueError:
                print('Type Error. Please input an integer.')


if __name__ == "__main__":
    text_generator = TextGenerator(input())
    # text_generator.show_info()
    # text_generator.print_tokens()
    print(f'Number of bigrams: {len(text_generator.bigrams)}')
    text_generator.print_bigrams()
