print("Using matcher.py")
import pandas as pd

def match_jobs(skills):

    jobs = pd.read_csv("data/job_roles.csv")

    results = []

    user_skills = set(skill.lower() for skill in skills)

    for _, row in jobs.iterrows():

        required_skills = [s.strip() for s in row["Skills"].split(",")]

        required_lower = [s.lower() for s in required_skills]

        # matched skills ni original case lo return cheddam
        matched = [req for req, req_low in zip(required_skills, required_lower) if req_low in user_skills]

        missing = [s for s in required_skills if s.lower() not in user_skills]

        score = (len(matched) / len(required_skills)) * 100 if required_skills else 0

        results.append({
            "Role": row["Role"],
            "Score": round(score),
            "Matched": matched,
            "Missing": missing
        })

    results.sort(key=lambda x: x["Score"], reverse=True)

    print(results)
    return results