from user import User


my_user = User.load_from_db_by_email('user@mail.oc')

print(my_user)
