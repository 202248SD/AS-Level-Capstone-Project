import random
import numpy as np
import pandas as pd


df = pd.read_csv('Glossary.csv')
df = np.array(df)
df = df.T

keywords, definitions, topics = df[0], df[1], df[2]
m, n = df.shape
running = True
correct = count = 0

while running:
    i = random.randint(1, n-1)
    keyword = keywords[i]
    definition = definitions[i]
    arr = [keyword]

    for _ in range(3):
        Flag = True
        while Flag:
            i = random.randint(1, n-1)
            if keywords[i] not in arr:
                Flag = False
        arr.append(keywords[i])

    print(f'Choose the corresponding keyword to the following definition:{definition}')
    print(f'KeyWords:{*arr, }')
    answer = input()
    count += 1

    if keyword.lower().find(answer.lower()) != -1:
        correct += 1
        print(f'You are correct!, Current Score: {correct}/{count}')
    else:
        print(f'You are wrong :c the answer was {keyword}, Current Score: {correct}/{count}')

    cont = input('Do you want to continue? y/n')

    if cont == 'n':
        running = False

print(f'Your Final Score is {correct}/{count}')
