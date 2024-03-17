from functions import *
from modules import *


def main():
    score = 0
    count = 0
    LOGIN, CREATE, GUEST = 1, 2, 3
    NUM_CHOICES = 4
    running = True
    login_method = login()

    user_details, users, hashes, pb, mistakes = init_user_data()
    if login_method == LOGIN:
        UID = get_UID(user_details, users)

        password = str(input('Password:'))
        check_password(password, hashes, UID)

        personal_best = pb[UID]
        mistake = [int(i) for i in str(mistakes[UID]).split() if i != 'nan']
    elif login_method == CREATE:
        UID = len(users)
        username, password_hash = create_user(user_details)

        mistake = []
        personal_best = 0

        user_details = np.array(
            (np.append(users, username), np.append(hashes, password_hash), np.append(pb, 0), np.append(mistakes, '')))
    else:
        UID = -1
        personal_best = float('inf')
        mistake = []

    keywords, definitions, topics, n = init_question_data()
    print('Type x to exit')
    while running:
        keyword, definition, QID = pick_question(keywords, definitions, n, mistake)
        arr = pick_fake(keyword, keywords, NUM_CHOICES - 1, n)

        correct_index = display_question(arr, definition, keyword)
        answer = input_answer(NUM_CHOICES)

        if answer == 'x':
            running = False
        else:
            if answer == 'ERROR':
                continue
            if answer == correct_index and QID in mistake:
                mistake.remove(QID)
            if answer != correct_index:
                mistake.append(QID)
            score, count = check_answer(correct_index, answer, score, count, keyword)
            print('')

    print('\n\n\n')
    print(f'{"<< Game Over >>":-^54}')
    print(f'''{f'{f"Your Final Score is {score}/{count}":^48}':-^54}''')

    if login_method != GUEST:
        user_details[3][UID] = reformat_mistake(mistake)
        user_details[2][UID] = update_personal_best(score, personal_best)
        data = user_details.T
        update_users(data)

    update_highscore(score)


if __name__ == '__main__':
    main()
