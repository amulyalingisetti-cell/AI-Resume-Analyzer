import pandas as pd
import re

def extract_skills(resume_text):

    skills_df = pd.read_csv("data/skills.csv")

    resume_text = resume_text.lower()

    found_skills = []

    for skill in skills_df["Skill"]:

        # Special handling for one-letter skills like C
        if len(skill) == 1:
            pattern = r"(?<![a-zA-Z])" + re.escape(skill.lower()) + r"(?![a-zA-Z])"
        else:
            pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, resume_text):
            found_skills.append(skill)

    return found_skills