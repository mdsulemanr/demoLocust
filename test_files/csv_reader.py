import os
import csv


class UserLoader:
    users = []
    file_path = os.getcwd() + "/AutoQuote/users.csv"

    @staticmethod
    def load_users():
        open_file = open(UserLoader.file_path)
        reader = csv.DictReader(open_file)
        for user_ele in reader:
            UserLoader.users.append(user_ele)

    @staticmethod
    def get_user():
        if len(UserLoader.users) < 1:
            UserLoader.load_users()
        user_obj = UserLoader.users.pop()
        return user_obj


usr = UserLoader
print(type(usr.get_user()['username']))
print(usr.get_user()['username'])
print(usr.get_user()['password'])


# class UserLoader1:
#
#     def __int__(self, filepath):
#         self.file_path = filepath
#
#     def get_user_data_from_csv():
#         user_data = []
#
#         with open(self.file_path, 'r', newline='', encoding='utf-8') as csvfile:
#             csv_reader = csv.DictReader(csvfile)
#
#             for row in csv_reader:
#                 user_name = row.get('user_name')
#                 user_email = row.get('user_email')
#
#                 if user_name and user_email:
#                     user_data.append({'user_name': user_name, 'user_email': user_email})
#
#         return user_data
#
#     # Example usage:
#     csv_file_path = 'path/to/your/file.csv'
#     users = get_user_data_from_csv(csv_file_path)
#
#     for user in users:
#         print(f"User Name: {user['user_name']}, User Email: {user['user_email']}")
