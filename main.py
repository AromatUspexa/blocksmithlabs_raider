from api import sign_request

with open('tokens.txt', 'r') as file:
    token_list = file.read().splitlines()


if __name__ == '__main__':

    raid_id = input('Введите ID события: ')

    for token in token_list:
        sign_request(token, raid_id)








