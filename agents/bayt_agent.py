import requests
from bs4 import BeautifulSoup


def search_bayt():

    roles = [
        "facilities manager",
        "facilities engineer",
        "chief engineer"
    ]

    job_list = []

    for role in roles:

        url = f"https://www.bayt.com/en/international/jobs/{role.replace(' ', '-')}-jobs/"

        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        jobs = soup.select("h2 a")

        for job in jobs[:20]:

            title = job.text.strip()
            link = "https://www.bayt.com" + job["href"]

            job_list.append({
                "title": title,
                "link": link
            })

    return job_list