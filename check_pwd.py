SYMBOLS = set("~`!@#$%^&*()_+-=")
def check_pwd(pwd: str) -> bool:
    if not (8 <= len(pwd) <= 20):
        return False
    lower_case = upper_case = digit = symbol = False
    for char in pwd:
        if char.islower():
            lower_case = True
        elif char.isupper():
            upper_case = True
        elif char.isdigit():
            digit = True
        elif char in SYMBOLS:
            symbol = True
    return lower_case and upper_case and digit and symbol