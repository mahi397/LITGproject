import hashlib, uuid;
input_pwd = "great_pAss6&."

salt = uuid.uuid4().hex
#salt has to be unique for each user

hashed_password = hashlib.sha512(input_pwd + salt).hexdigest()
