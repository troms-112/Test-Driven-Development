def check_pwd(pwd: str) -> bool:
    if not (8 <= len(pwd) <= 20):
        return False
    return True