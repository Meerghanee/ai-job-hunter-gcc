from jobspy import scrape_jobs

def search_indeed():

    roles = [
        "Facilities Manager",
        "Facilities Operations Manager",
        "Senior Facilities Engineer",
        "Chief Engineer",
        "Head of Facilities",
        "Duty Manager"
    ]

    # City-based search improves GCC job discovery
    locations = [
        "Dubai, UAE",
        "Abu Dhabi, UAE",
        "Doha, Qatar",
        "Riyadh, Saudi Arabia",
        "Jeddah, Saudi Arabia"
    ]

    job_list = []

    for role in roles:
        for loc in locations:

            jobs = scrape_jobs(
                site_name=["linkedin", "indeed"],
                search_term=role,
                location=loc,
                results_wanted=50,
                hours_old=168
            )

            for _, job in jobs.iterrows():

                job_list.append({
                    "title": job["title"],
                    "link": job["job_url"]
                })

    return job_list