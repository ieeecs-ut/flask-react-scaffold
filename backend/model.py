import mongoengine as me

# defines fields for user accounts
class User(me.Document):
    username = me.StringField(max_length=50, required=True, unique=True)
    email = me.StringField(max_length=50, required=True, unique=True)
    password = me.StringField(max_length=72, required=True)
    projectList = me.ListField()
    payment_set = me.BooleanField(default=False)

# function to create and save a new user to the database
def create_user(username, email, pwd, project_list = None):
    projectList = []
    if project_list:
       projectList = project_list
    new_user = User(username=username, email=email, password=pwd, projectList=projectList)
    # creates a new document, doesn't allow for updates if this document already exists
    new_user.save(force_insert=True)
    return


# check if the username already exists in the database
def does_user_name_exist(username) -> bool:
    query = User.objects(username__exact=username)
    if len(query) != 1:
        return False  # not found
    current_user = query.first()
    if not current_user:
        return False  # not found
    if username != current_user.username:
        return False
    return True


# check if the user email already exists in the database
def does_user_email_exist(email) -> bool:
    query = User.objects(email__exact=email)
    if len(query) != 1:
        return False  # not found
    current_user = query.first()
    if not current_user:
        return False  # not found
    if email != current_user.email:
        return False
    return True


def compare_passwords(password_A, password_B) -> bool:
    # TODO: implement bcrypt hashing for password
    return password_A == password_B

# find document with exact username (they all should be unique so only one should be found if it exists)
# see if password is correct
def verify_login(username, password) -> int:
    query = User.objects(username__exact=username)
    if len(query) != 1:
        return 404  # not found
    current_user = query.first()
    if not current_user:
        return 404  # not found
    if compare_passwords(current_user.password, password):
        return 1
    return 401