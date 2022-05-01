from user import User
from database import Database
import cred


Database.initialise(user=cred.login, password=cred.passwd, database='learning', host='localhost')

my_user = User('kszksz@mail.oc', 'halo', 'tsz', None)
my_user.save_to_db()

user_from_db = User.load_from_db_by_email('adam@mail.oc')
print(user_from_db)

my_user.save_to_db()
