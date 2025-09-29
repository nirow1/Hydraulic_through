def check_path_for_special_chars(path: str) -> bool:
    try:
        path.encode("ascii")
        return False  # all good, no special chars
    except UnicodeEncodeError:
        return True  # special characters found