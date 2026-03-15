def is_relevant(title):

    title = title.lower()

    keywords = [
        "facility",
        "facilities",
        "fm"
    ]

    if any(k in title for k in keywords):
        return True

    return False