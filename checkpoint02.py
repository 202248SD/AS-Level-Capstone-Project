import random
import numpy as np
import pandas as pd


def init_data(filename='Glossary.tsv'):
    df = pd.read_csv(filename, sep='\t')
    df = np.array(df)
    df = df.T
    return df


def split_data(df):
    keywords, definitions, topics = df[0], df[1], df[2]
    return keywords, definitions, topics


def choose_course(k, d, t):
    print('Do you want to learn AS Level, A Level, or both? (AS/A/both)')
    course = str(input())
    if course == 'AS':
        k, d, t = k[:201], d[:201], t[:201]
    elif course == 'A':
        k, d, t = k[202:], d[202:], t[202:]
    return k, d, t


def pick_question(keywords, definitions):
    i = random.randint(1, n - 1)
    keyword = keywords[i]
    definition = definitions[i]
    return keyword, definition


def pick_fake(arr, keywords, num):
    for _ in range(num):
        flag = True
        while flag:
            i = random.randint(1, n-1)
            if keywords[i] not in arr:
                flag = False
        arr.append(keywords[i])
    return num


def display_question(arr, definition, real_k):
    print(f'Choose the corresponding keyword to the following definition:{definition}')
    random.shuffle(arr)
    for i in range(len(arr)):
        if arr[i] == real_k:
            out = i+1
        arr[i] = str(i+1)+': '+arr[i].strip()
    print(f'KeyWords:{*arr,}')
    return out


def input_answer():
    answer = input()
    if answer not in [str(i) for i in range(10)]:
        print('Error: Your input should be the number next to the keyword you choose')
    else:
        return int(answer)


def check_answer(correct_index, answer, correct, count):
    count = count + 1
    if correct_index == answer:
        correct += 1
        print(f'You are correct!, Current Score: {correct}/{count}')
    else:
        print(f'You are wrong :c the answer was {keyword}, Current Score: {correct}/{count}')
    return correct, count


def cont():
    cont = input('Do you want to continue? y/n')

    if cont == 'n':
        return False
    return True


correct = 0
count = 0
running = True

df = init_data('Glossary.tsv')
keywords, definitions, topics = split_data(df)
keywords, definitions, topics = choose_course(keywords, definitions, topics)
n = len(keywords)


while running:
    keyword, definition = pick_question(keywords, definitions)
    arr = [keyword]
    pick_fake(arr, keywords, 3)

    correct_index = display_question(arr, definition, keyword)
    answer = input_answer()
    correct, count = check_answer(correct_index, answer, correct, count)

    running = cont()

print(f'Your Final Score is {correct}/{count}')
