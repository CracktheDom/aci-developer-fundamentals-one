def create_profile(username, age):
    """Creates dictionary with user details
    and calls function to create homepage"""
    try:
        if age < 13:
            raise Exception("Account holders must be 13 or older.")
        user_dict = {"name": username, "age": age}
        print(user_dict)
        create_homepage(user_dict)
    except Exception as e:
        print(e)


def create_profile_two(username: str, age: int):
    """Creates dictionary with user details
    and calls function to create homepage"""
    try:
        if age < 13:
            raise ValueError("Account holders must be 13 or older.")
        user_dict = {"name": username, "age": age}
        print(user_dict)
        create_homepage(user_dict)
    except Exception as e:
        print(type(e))
        print(e)
