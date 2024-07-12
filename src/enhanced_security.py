import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def check_password(hashed_password, password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

if __name__ == "__main__":
    password = "securepassword"
    hashed_password = hash_password(password)
    print(f"Hashed password: {hashed_password}")

    assert check_password(hashed_password, password) == True
    print("Password verification successful")
