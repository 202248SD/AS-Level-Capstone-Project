import random
import csv
from hashlib import sha256


def pick_question(keywords, definitions, n, mistake):
    arr = [i for i in range(1, n - 1)]
    arr += mistake
    i = random.choice(arr)
    keyword = keywords[i]
    definition = definitions[i]
    return keyword, definition, i


def pick_fake(keyword, keywords, num, n):
    num = min(num, n-1)
    arr = [keyword]
    for _ in range(num):
        flag = True
        while flag:
            i = random.randint(0, n - 1)
            if keywords[i] not in arr:
                flag = False
        arr.append(keywords[i])
    return arr


def display_question(arr, definition, real_k):
    definition = definition.strip()
    n = min(13+len(definition), 120)
    print(f'{"Choose the correct keyword":-^{n}}')

    try:
        definition[0] = definition[0].upper()
    except:
        pass
    if 13+len(definition) <= 120:
        print(f'Definition: {definition}')
    else:
        definition = 'Definition: ' + definition
        definition = definition.split()
        i = 0
        while i < len(definition):
            t = ''
            while len(t) <= 120 and i < len(definition):
                t += definition[i] + ' '
                i += 1
            print(t)
    keywords = ''
    random.shuffle(arr)
    n -= sum([len(i.strip()) for i in arr])+8
    n //= 3
    n = max(2, n)
    for i in range(len(arr)):
        if arr[i] == real_k:
            out = i + 1
        keywords += str(i + 1) + ':' + arr[i].strip() + ' '*n
    print(f'{keywords:^{n}}')
    return out


def check_answer(correct_index, answer, correct, count, keyword):
    count = count + 1
    if correct_index == answer:
        correct += 1
        print(f'You are correct! Current Score: {correct}/{count}')
    else:
        print(f'You are wrong! Answer was {str(keyword.strip())}. Current Score: {correct}/{count}')
    return correct, count


def update_users(data):
    with open('users.tsv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['username', 'passwordHash', 'personalBest', 'mistakes'])
        for row in data:
            writer.writerow(row)


def update_highscore(score):
    with open('HighScore.txt', 'r') as f:
        highscore = int(f.readline())

    if score > highscore:
        print(f'''{f'{f"You got a High Score!  Old: {highscore}  New: {score}":^48}':-^54}''')
        with open('HighScore.txt', 'w') as f:
            f.write(str(score))
    else:
        print(f'''{f'{f"Current Highest Score: {highscore}":^48}':-^54}''')


def update_personal_best(score, pb):
    if score > pb:
        print(f'''{f'{f"You got a Personal Best!  Old: {pb}  New: {score}":^48}':-^54}''')
        return score
    print(f'''{f'{f"Current Personal Best: {pb} ":^48}':-^54}''')
    return pb


def hash_password(password):
    return sha256(password.encode('utf-8')).hexdigest()


def reformat_mistake(mistake):
    t = ''
    for i in mistake:
        t += str(i) + ' '
    return t


def get_UID(user_details, users):
    username = str(input('Username:'))
    while username not in user_details:
        print('There is no user with that name!')
        username = str(input('Username:'))
    UID = users.index(username)
    return UID


def check_password(password, hashes, UID):
    password_hash = hash_password(password)

    while password_hash != hashes[UID]:
        print('Error: wrong password!')
        password = str(input('Password:'))
        password_hash = hash_password(password)

    print('Logged In!')


def create_user(user_details):
    username = str(input('Username:'))
    while username in user_details:
        print('There is already a user with that name!')
        username = str(input('Username:'))

    password = str(input('Password:'))
    password_hash = hash_password(password)
    return username, password_hash
