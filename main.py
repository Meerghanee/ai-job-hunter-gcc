from agents.indeed_agent import search_indeed
from agents.bayt_agent import search_bayt
from utils.job_filter import is_relevant
from utils.telegram_sender import send_job


def run():

    jobs = []

    jobs.extend(search_indeed())
    jobs.extend(search_bayt())

    print("Jobs Found:", len(jobs))

    for job in jobs:

        if is_relevant(job["title"]):

            print("Relevant job found:", job["title"])

            message = f"""
New Facilities Job 🚀

Title: {job['title']}
Link: {job['link']}
"""

            send_job(message)


run()