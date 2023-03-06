"""
Function checks user's password with hashing.
"""
import hashlib
import json

salt = 'u_salt'


def get_hash(passwd):
    return hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()


def check_password():
    passwd = input('Enter password: ')
    passwd_hash = get_hash(passwd)
    # print(f'Password hash: {passwd_hash}')
    data = {salt: passwd_hash}
    with open('passwords.json', 'w') as f:
        json.dump(data, f)

    check_passwd = input('Enter password one more time for validation: ')
    check_passwd_hash = get_hash(check_passwd)
    with open('passwords.json', 'r') as f:
        data = json.load(f)
        if data[salt] == check_passwd_hash:
            print('Correct password')
        else:
            print("Passwords don't match")


check_password()
