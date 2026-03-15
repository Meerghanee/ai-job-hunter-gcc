def is_relevant(title):

    title = title.lower()

    keywords = [
        "facility",
        "facilities",
        "fm"
    ]

    roles = [
        "manager",
        "engineer",
        "head",
        "director",
        "chief"
    ]

    if any(k in title for k in keywords) and any(r in title for r in roles):
        return True

    return False