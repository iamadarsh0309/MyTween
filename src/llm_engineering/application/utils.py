def split_user_full_name(user_full_name: str) -> tuple[str, str]:
    first_name, last_name = user_full_name.strip().split(maxsplit=1)
    return first_name, last_name
