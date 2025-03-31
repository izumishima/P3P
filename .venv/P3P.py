import re

user_list = []

def get_valid_username(user_list, username):
    if not username:
        return "Username cannot be empty"
    if username in user_list:
        return f"Username '{username}' is already taken. Please choose another"
    if len(username) < 3 or len(username) > 20:
        return "Username must be between 3 and 20 characters."

    user_list.append(username)
    return f"Username '{username}' successfully added!"

if __name__ == "__main__":
    try:
        # Prompt the user for a username
        username = input("Enter a username to validate: ")

        # Validate the username
        valid_username = get_valid_username(user_list, username)
        print(f"Username '{valid_username}' is valid!")
    except ValueError as e:
        # Print error message if the username is invalid
        print(f"Error: {e}")



def create_username(user_list, username):

    if not username or len(username) < 3:
        return {"success": False, "message": "Username cannot be empty."}

    if len(username) < 3:
        return {"success": False, "message": "Username must be at least 3 characters long."}

    if len(username) > 20:
        return {"success": False, "message": "Username must not exceed 20 characters."}

    if not username.isalnum():
        return {"success": False, "message": "Username must only contain letters and numbers."}

    if username in user_list:
        return {"success": False, "message": f"Username '{username}' is already taken."}

    user_list.add(username)
    return {"success": True, "message": f"Username '{username}' has been successfully created!"}


