
import unittest

from credentials import Credentials
from user import User


class Testclass(unittest.TestCase):

    def setUp(self):
        self.new_user = User('John', 'Doe', 'johndoe', 'abc')
        self.new_credentials = Credentials(
            'johndoe', 'twitter', f'{Credentials.generate_password(8)}')

    def test_init(self):
        self.assertEqual(self.new_user.fist_name, 'John')
        self.assertEqual(self.new_user.last_name, 'Doe')
        self.assertEqual(self.new_user.user_name, 'johndoe')
        self.assertEqual(self.new_user.password, 'abc')

    def test_generate_password(self):
        self.assertTrue(len(Credentials.generate_password(8)) == 8)

    def test_save_login_credentials(self):
        self.new_credentials.save_login_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_find_user_by_name(self):
        self.new_user.save_user()
        test_contact = User('tes', 'odhiambo', 'stevo', '0000')
        test_contact.save_user()
        found_user = User.find_user_by_username('stevo')
        self.assertTrue(found_user)

    def test_find_user_by_password(self):
        self.new_user.save_user()
        test_contact = User('tes', 'odhiambo', 'stevo', '0000')
        test_contact.save_user()
        found_user = User.find_user_by_password('0000')
        self.assertTrue(found_user)

    def tearDown(self):
        Credentials.credentials_list = []
        User.user_list = []

    def test_save_multiple_credentials(self):
        self.new_credentials.save_login_credentials()
        test_credential = Credentials(
            'Test', 'twitter', Credentials.generate_password(8))
        test_credential.save_login_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_credential_exist(self):
        self.new_credentials.save_login_credentials()
        test_credential = Credentials(
            'test', 'facebook', Credentials.generate_password(8))
        test_credential.save_login_credentials()
        credential_exists = Credentials.credential_exist('facebook')
        self.assertTrue(credential_exists)

    def test_find_by_name(self):
        self.new_credentials.save_login_credentials()
        test_credential = Credentials(
            'test', 'facebook', Credentials.generate_password(8))
        test_credential.save_login_credentials()
        found_credential = Credentials.find_by_name('facebook')
        self.assertEqual(found_credential, test_credential)

    def test_delete_credentials(self):
        self.new_credentials.save_login_credentials()
        test_credential = Credentials(
            'test', 'facebook', Credentials.generate_password(8))
        test_credential.save_login_credentials()
        self.new_credentials.delete_credentials('facebook')
        self.assertTrue(len(Credentials.credentials_list) == 1)

    def test_display_credentials(self):
        self.new_credentials.save_login_credentials()
        self.assertEqual(Credentials.display_credential(),
                         Credentials.credentials_list)


if __name__ == '__main__':
    unittest.main()
