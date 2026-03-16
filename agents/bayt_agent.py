import requests
from bs4 import BeautifulSoup


def search_bayt():

    roles = [
        "facilities manager",
        "facilities engineer",
        "chief engineer"
    ]

    job_list = []

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for role in roles:

        query = f"site:bayt.com {role}"
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")

        results = soup.select("a")

        for r in results:

            link = r.get("href", "")

            if "bayt.com" in link and "/jobs/" in link:

                title = r.text.strip()

                if title:

                    job_list.append({
                        "title": title,
                        "link": link
                    })

    print("Bayt Jobs Found:", len(job_list))

    return job_list