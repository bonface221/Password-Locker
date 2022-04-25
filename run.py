#!/usr/bin/env python3.9
from user import User
from credentials import Credentials


def create_user(fname, lname, username, password):
    new_user = User(fname, lname, username, password)
    return new_user


def save_user(user):
    user.save_user()


def user_exists(user):
    return User.find_user_by_username(user)


def password_exists(password):
    return User.find_user_by_password(password)


def create_credentials(username, socialplatform, password):
    new_credential = Credentials(username, socialplatform, password)
    return new_credential


def save_credential(credential):
    credential.save_login_credentials()


def generate_password(length):
    return Credentials.generate_password(length)


def del_credential(social):
    return Credentials.delete_credentials(social)


def find_credential(social):
    return Credentials.find_by_name(social)


def check_existing_credentials(social):
    return Credentials.credential_exist(social)


def display_credentials():
    return Credentials.display_credential()


def main():
    print('Welcome to Password Locker. What is your name?')
    user_name = input()

    print(f'Hello {user_name}. Nice to have you here')
    print('\n')
    while True:
        print('use short codes : l - to login, s -to sign-up , ex- to exit')

        short_code1 = input().lower()
        if short_code1 == 's':
            print('Sign Up')
            print('-'*10)
            print('First name ......')
            f_name = input()

            print('Last name .....')
            l_name = input()

            print('Enter preffered Username......')
            u_name = input()

            print('Enter Preffered Password ......')
            p_word = input()

            save_user(create_user(f_name, l_name, u_name, p_word))

            print('\n')
            print(f'New user {f_name} {l_name} has been created successfully')
            print('-'*10)
            print('Proceed to logging in....')
            print('\n')

        elif short_code1 == 'l':
            print('Login')
            print('-'*10)

            print('Enter Username')
            user_input = input()
            if user_exists(user_input):
                print('Enter password')
                user_password = input()
                print('\n')
                if password_exists(user_password):
                    print('User found. Logging in......')
                    print('\n')
                    while True:
                        print('Welcome to your dashboard')
                        print('\n')
                        print(
                            'Use these short codes : cc- create credentials, dc-display credentials, fc- find credentials, dd-delete credentials ex: exit')

                        short_code2 = input().lower()

                        if short_code2 == 'cc':
                            print('New password credential')
                            print('-'*10)

                            print('Enter preffered Username......')
                            user_social = input()

                            print('Enter social media platform......')
                            social_p = input().lower()

                            print(
                                'Enter preffered password .or type g - to generate automatically')
                            user_pass = input()
                            if user_pass == 'g':
                                user_pass = generate_password(8)
                            else:
                                user_pass = user_pass

                            save_credential(create_credentials(
                                user_social, social_p, user_pass))

                            print('\n')
                            print(
                                f'New {social_p} Password credential has been saved successfully')
                            print('\n')

                        elif short_code2 == 'dc':
                            if display_credentials():
                                print(
                                    'Here is a list of all your stored Credentials')
                                print('\n')

                                for credential in display_credentials():
                                    print(
                                        f'{credential.social_platform}...{credential.user_name} .......{credential.password}')

                                    print('\n')

                            else:
                                print('\n')
                                print(
                                    'You don\'t seem to have any credentials stored ')
                                print('\n')

                        elif short_code2 == 'fc':
                            print('Enter the social handle to find credential')

                            search_handle = input()
                            if check_existing_credentials(search_handle):
                                found_handle = find_credential(search_handle)
                                print(
                                    f'{found_handle.social_platform} has been found')
                                print('-'*10)

                                print(
                                    f'User name .......{found_handle.user_name}')
                                print(
                                    f'password .........{found_handle.password}')

                            else:
                                print(
                                    'That Social handle does not exist. Please check the spelling')

                        elif short_code2 == 'dd':
                            print(
                                'Are you sure you want to delete a credential! It will be lost forever!!')
                            print('Enter ok to proceed : x to cancel')
                            entered = input()
                            if entered == 'ok':
                                print('Enter credential to delete')
                                to_delete = input()
                                del_credential(to_delete)

                            else:
                                return

                        elif short_code2 == 'ex':
                            print('Bye.....')
                            break
                        else:
                            print(
                                'I really didn\'t get that.Please use the short codes')

                else:
                    print('Sorry! Password did not match')

            else:
                print('Username does not exist')

        elif short_code1 == 'ex':
            print('Bye....')
            break
        else:
            print('I really didn\'t get that.Please use the short codes')


if __name__ == '__main__':
    main()
