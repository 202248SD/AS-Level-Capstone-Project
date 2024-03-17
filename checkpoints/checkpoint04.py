import random
import numpy as np
import pandas as pd
from functions import *
import csv
from hashlib import sha256


def init_data(filename='Glossary.tsv'):
    df = pd.read_csv(filename, sep='\t')
    df = np.array(df)
    df = df.T
    return df


correct = 0
count = 0
running = True

df = init_data('Glossary.tsv')
keywords, definitions, topics = split_data(df)
keywords, definitions, topics = choose_course(keywords, definitions, topics)
n = len(keywords)


print('Do you want to login?')
login_method = int(input('1: Login, 2: Create Account, 3: Play as Guest'))
while login_method not in {1, 2, 3}:
    print('Invalid input! Choose the corresponding number:')
    login_method = int(input('1: Login, 2: Create Account, 3: Play as Guest'))
user_details = init_data('users.tsv')

users = [i.strip() for i in user_details[0]]
hashes = user_details[1]
pb = user_details[2]

if login_method == 1:
    username = str(input('Username:'))
    while username not in user_details:
        print('There is no user with that name!')
        username = str(input('Username:'))
    UID = users.index(username)

    password = str(input('Password:'))
    password_hash = sha256(password.encode('utf-8')).hexdigest()
    print(hashes[UID])
    while password_hash != hashes[UID]:
        print('Error: wrong password!')
        password = str(input('Password:'))
        password_hash = sha256(password.encode('utf-8')).hexdigest()

    print('Logged In!')
    personal_best = pb[UID]

if login_method == 2:
    UID = len(users)
    username = str(input('Username:'))
    while username in user_details:
        print('There is already a user with that name!')
        username = str(input('Username:'))

    password = str(input('Password:'))
    password_hash = sha256(password.encode('utf-8')).hexdigest()
    user_detail = [username, password_hash, -1]
    personal_best = -1
    with open('users.tsv', 'a', newline='') as f:
        writer = csv.writer(f, delimiter='\t', lineterminator='\n')
        writer.writerow(user_detail)
    users = np.append(users, username)
    hashes = np.append(hashes, password_hash)
    pb = np.append(pb, -1)
    user_details = np.array((users, hashes, pb))



while running:
    keyword, definition = pick_question(keywords, definitions, n)
    arr = [keyword]
    arr = pick_fake(arr, keywords, 3, n)

    correct_index = display_question(arr, definition, keyword)
    answer = input_answer()
    if answer == 'x':
        running = False
    else:
        correct, count = check_answer(correct_index, answer, correct, count, keyword)
print(f'Your Final Score is {correct}/{count}')


with open('HighScore.txt', 'r') as f:
    highscore = int(f.readline())

if login_method != 3:
    if correct > personal_best:
        print(f'You got your Highest achieved score! Your old personal best was {personal_best}, and your new score is {correct}')
        with open('users.tsv', 'w', newline='') as f:
            writer = csv.writer(f, delimiter='\t')
            user_details[2][UID] = correct
            writer.writerow(['username', 'passwordHash', 'personalBest'])
            data = user_details.T
            for row in data:
                writer.writerow(row)


if correct > highscore:
    print(f'You got a High score! The old score was {highscore}, and your new score is {correct}')
    with open('HighScore.txt', 'w') as f:
        f.write(str(correct))
