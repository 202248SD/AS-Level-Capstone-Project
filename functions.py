import random


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


def pick_question(keywords, definitions, n):
    i = random.randint(1, n - 1)
    keyword = keywords[i]
    definition = definitions[i]
    return keyword, definition


def pick_fake(arr, keywords, num, n):
    for _ in range(num):
        flag = True
        while flag:
            i = random.randint(1, n-1)
            if keywords[i] not in arr:
                flag = False
        arr.append(keywords[i])
    return arr


def display_question(arr, definition, real_k):
    print('Type x to exit')
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
    if answer == 'x':
        return answer
    elif answer not in [str(i) for i in range(10)]:
        print('Error: Your input should be the number next to the keyword you choose')
    else:
        return int(answer)


def check_answer(correct_index, answer, correct, count, keyword):
    count = count + 1
    if correct_index == answer:
        correct += 1
        print(f'You are correct!, Current Score: {correct}/{count}')
    else:
        print(f'You are wrong :c the answer was {keyword}, Current Score: {correct}/{count}')
    return correct, count
