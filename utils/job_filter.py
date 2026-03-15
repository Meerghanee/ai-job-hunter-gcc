def is_relevant(title):

    title = title.lower()

    keywords = [
        "facility",
        "facilities",
        "fm"
    ]

    # if job title contains facilities-related word
    for word in keywords:
        if word in title:
            return True

    return False