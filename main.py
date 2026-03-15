import json

from agents.indeed_agent import search_indeed
from utils.job_filter import is_relevant
from utils.telegram_sender import send_job


def load_seen_jobs():

    with open("database/jobs_seen.json", "r") as f:
        return json.load(f)


def save_seen_jobs(seen):

    with open("database/jobs_seen.json", "w") as f:
        json.dump(seen, f)


def run():

    jobs = search_indeed()

    seen_jobs = load_seen_jobs()

    print("Jobs Found:", len(jobs))

    for job in jobs:

        print("Checking:", job["title"])

        if job["link"] in seen_jobs:
            continue

        if is_relevant(job["title"]):

            print("Relevant job found:", job["title"])

            message = f"""
New Facilities Job 🚀

Title: {job['title']}
Link: {job['link']}
"""

            send_job(message)

            seen_jobs.append(job["link"])

    save_seen_jobs(seen_jobs)


run()