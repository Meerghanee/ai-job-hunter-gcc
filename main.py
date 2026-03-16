from agents.indeed_agent import search_indeed
from agents.naukri_agent import search_naukri
from utils.job_filter import is_relevant
from utils.telegram_sender import send_job


def run():

    jobs = []

    # LinkedIn + Indeed (via jobspy)
    jobs.extend(search_indeed())

    # Naukri Gulf scraper
    jobs.extend(search_naukri())

    print("Jobs Found:", len(jobs))

    for job in jobs:

        print("Checking:", job["title"])

        if is_relevant(job["title"]):

            print("Relevant job found:", job["title"])

            message = f"""
New Facilities Job 🚀

Title: {job['title']}
Link: {job['link']}
"""

            send_job(message)


run()