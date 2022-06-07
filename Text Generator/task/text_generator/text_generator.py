import nltk
import random
from nltk.tokenize import regexp_tokenize
from collections import Counter


class TextGenerator:
    def __init__(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            self.corpus = f.read()
        self.tokens = regexp_tokenize(self.corpus, r'\S+')
        self.unique_tokens = list(set(self.tokens))
        self.bigrams = list(nltk.bigrams(self.tokens))
        self.trigrams = list(nltk.trigrams(self.tokens))
        self.model = {}

    def show_info(self):
        print(f'Corpus statistics\n'
              f'All tokens: {len(self.tokens)}\n'
              f'Unique tokens: {len(self.unique_tokens)}\n')

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
        for head, body, tail in self.trigrams:
            self.model.setdefault(f'{head} {body}', []).append(tail)
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

    def get_head(self):
        options = [pair for pair in self.model.keys() if pair[0].isupper()]
        starter = random.choice(options)
        while starter.split()[0][-1] in '.!?':
            starter = random.choice(options)
        return starter

    def get_tail(self, head, ending):
        population, weights = list(zip(*self.model[head].most_common()))
        tail = random.choices(population, weights)[0]
        while ending and tail[-1] not in '.?!':
            tail = random.choices(population, weights)[0]
        return tail

    def is_dead_end(self, word):
        population = set(self.model[word].keys())
        ending_words = [w for w in population if w[-1] in '.?!']
        return ending_words == []

    def generate_pseudo_sentence(self):
        sentence = self.get_head().split()
        while len(sentence) < 10:
            if len(sentence) == 9 and self.is_dead_end(' '.join(sentence[-2:])):
                sentence = self.get_head().split()
                continue
            word = self.get_tail(' '.join(sentence[-2:]), len(sentence) == 9)
            sentence.append(word)
            if len(sentence) > 4 and word[-1] in '.?!':
                break
        return ' '.join(sentence)


if __name__ == "__main__":
    text_generator = TextGenerator(input())
    text_generator.get_model()
    for n in range(10):
        print(text_generator.generate_pseudo_sentence())
