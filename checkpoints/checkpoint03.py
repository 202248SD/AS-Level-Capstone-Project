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
    while password_hash != hashes[UID]:
        print('Error: wrong password!')
        password = str(input('Password:'))
        password_hash = sha256(password.encode('utf-8')).hexdigest()

    print('Logged In!')
    personal_best = pb[UID]

if login_method == 2:
    username = str(input('Username:'))
    while username in user_details:
        print('There is already a user with that name!')
        username = str(input('Username:'))

    password = str(input('Password:'))
    password_hash = sha256(password.encode('utf-8')).hexdigest()
    user_detail = [username, password_hash, -1]

    with open('users.tsv', 'a', newline='') as f:
        writer = csv.writer(f, delimiter='\t', lineterminator='\n')
        writer.writerow(user_detail)

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
if correct > highscore:
    print(f'You got a new high score! The old score was {highscore}, and your new score is {correct}')
    with open('HighScore.txt', 'w') as f:
        f.write(str(correct))
