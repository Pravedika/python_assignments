class InvalidPasswordError(Exception):
    pass

def validate_password(password):
    try:
        if len(password) < 8:
            raise InvalidPasswordError(
                "Password must contain at least 8 characters"
            )
        print("Password is valid")
    except InvalidPasswordError as e:
        print("Error:", e)

validate_password("python123")
validate_password("abc")
