import requests
from bs4 import BeautifulSoup


def search_naukri():

    roles = [
        "facilities-manager",
        "facilities-engineer",
        "chief-engineer"
    ]

    job_list = []

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for role in roles:

        url = f"https://www.naukrigulf.com/{role}-jobs"

        try:

            response = requests.get(url, headers=headers, timeout=10)

            soup = BeautifulSoup(response.text, "html.parser")

            jobs = soup.select("a.info-position")

            for job in jobs[:20]:

                title = job.text.strip()
                link = job.get("href")

                if title and link:

                    job_list.append({
                        "title": title,
                        "link": link
                    })

        except Exception as e:

            print("Naukri scraper error:", e)

    print("Naukri Jobs Found:", len(job_list))

    return job_list