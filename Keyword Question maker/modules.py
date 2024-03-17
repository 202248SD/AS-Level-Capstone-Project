import numpy as np
import pandas as pd


def init_question_data():
    def split_data(df):
        return df[0], df[1], df[2]

    def choose_course(k, d, t):
        course = str(input('Do you want to learn AS Level, A Level, or both? (AS/A/both)'))
        print('')
        if course == 'AS':
            k, d, t = k[:201], d[:201], t[:201]
        elif course == 'A':
            k, d, t = k[202:], d[202:], t[202:]
        return k, d, t

    df = init_file('Glossary.tsv')
    keywords, definitions, topics = choose_course(*split_data(df))
    n = len(keywords)
    return keywords, definitions, topics, n


def init_file(filename='Glossary.tsv'):
    df = pd.read_csv(filename, sep='\t')
    df = np.array(df)
    df = df.T
    return df


def init_user_data():
    user_details = init_file('users.tsv')
    users = [i.strip() for i in user_details[0]]
    hashes = user_details[1]
    pb = user_details[2]
    mistakes = user_details[3]
    return user_details, users, hashes, pb, mistakes


def input_answer():
    answer = input()
    if answer == 'x':
        return answer
    elif answer not in [str(i) for i in range(10)]:
        print('Error: Your input should be the number next to the keyword you choose')
        return 'ERROR'
    else:
        return int(answer)


def login():
    print('Do you want to login?')
    login_method = str(input('1: Login, 2: Create Account, 3: Play as Guest'))
    while login_method not in {'1', '2', '3'}:
        print('Invalid input! Choose the corresponding number:')
        login_method = str(input('1: Login, 2: Create Account, 3: Play as Guest'))
    return int(login_method)
