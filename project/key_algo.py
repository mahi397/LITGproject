import bcrypt;

input_pwd = "great_pAss6&."
salt = bcrypt.gensalt()
hashed_pwd = bcrypt.hashpw(input_pwd, salt)
