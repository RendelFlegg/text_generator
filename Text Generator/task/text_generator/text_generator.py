import nltk
import random
from nltk.tokenize import regexp_tokenize
from collections import Counter


class TextGenerator:
    def __init__(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            self.corpus = f.read()
        self.tokens = regexp_tokenize(self.corpus, r'\S+')
        self.bigrams = list(nltk.bigrams(self.tokens))
        self.model = {}

    def show_info(self):
        print(f'Corpus statistics\n'
              f'All tokens: {len(self.tokens)}\n'
              f'Unique tokens: {len(set(self.tokens))}\n')

    def print_tokens(self):
        user_input = input()
        while user_input != 'exit':
            try:
                idx = int(user_input)
                print(self.tokens[idx])
            except IndexError:
                print('Index Error. Please input an integer that is in the range of the corpus.')
            except ValueError:
                print('Type Error. Please input an integer.')
            finally:
                user_input = input()

    def print_bigrams(self):
        user_input = input()
        while user_input != 'exit':
            try:
                idx = int(user_input)
                bigram = self.bigrams[idx]
                print(f'Head: {bigram[0].ljust(10)} Tail: {bigram[1]}')
            except IndexError:
                print('Index Error. Please input an integer that is in the range of the corpus.')
            except ValueError:
                print('Type Error. Please input an integer.')
            finally:
                user_input = input()

    def get_model(self):
        for head, tail in self.bigrams:
            self.model.setdefault(head, []).append(tail)
        for head, tails in self.model.items():
            self.model[head] = Counter(tails)

    def print_model(self):
        user_input = input()
        while user_input != 'exit':
            if user_input not in self.model:
                print('Key Error. The requested word is not in the model. Please input another word.')
            else:
                print(f'Head: {user_input}')
                for tail, count in self.model[user_input].most_common():
                    print(f'Tail: {tail.ljust(10)} Count: {count}')
            user_input = input()

    def get_tail(self, head):
        population, weights = list(zip(*self.model[head].most_common()))
        return random.choices(population, weights)[0]

    def generate_pseudo_sentence(self):
        sentence = []
        while len(sentence) < 10:
            try:
                sentence.append(self.get_tail(sentence[-1]))
            except IndexError:
                sentence.append(random.choice(list(set(self.tokens))))
        return ' '.join(sentence)


if __name__ == "__main__":
    text_generator = TextGenerator(input())
    text_generator.get_model()
    for n in range(10):
        print(text_generator.generate_pseudo_sentence())
