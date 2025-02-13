def check_pwd(pwd: str) -> bool:
    if not len(pwd) == 8:
        return False
    return True