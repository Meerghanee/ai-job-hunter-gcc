import requests
from bs4 import BeautifulSoup


def search_bayt():

    roles = [
        "facilities-manager",
        "facilities-engineer",
        "chief-engineer"
    ]

    job_list = []

    for role in roles:

        url = f"https://www.bayt.com/en/international/jobs/{role}-jobs/"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")

        jobs = soup.select("a[data-js='job-title']")

        for job in jobs[:20]:

            title = job.text.strip()
            link = "https://www.bayt.com" + job["href"]

            job_list.append({
                "title": title,
                "link": link
            })

    return job_list