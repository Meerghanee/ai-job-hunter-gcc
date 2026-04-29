from agents.indeed_agent import search_indeed
from agents.naukri_agent import search_naukri
from utils.job_filter import is_relevant
from utils.telegram_sender import send_job

# 🔴 CONTROL SWITCH
SEND_ALERTS = False   # False = STOP | True = START


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

            # 🚫 STOP / START control
            if SEND_ALERTS:
                send_job(message)


run()
