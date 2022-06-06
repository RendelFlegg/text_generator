from nltk.tokenize import regexp_tokenize


file_path = input()
with open(file_path, 'r', encoding='utf-8') as f:
    corpus = f.read()

tokens = regexp_tokenize(corpus, r'\S+')

print('Corpus statistics')
print('All tokens:', len(tokens))
print('Unique tokens', len(set(tokens)))

while True:
    try:
        user_input = input()
        if user_input == 'exit':
            break
        idx = int(user_input)
        print(tokens[idx])
    except IndexError:
        print('Index Error. Please input an integer that is in the range of the corpus.')
    except ValueError:
        print('Type Error. Please input an integer.')
