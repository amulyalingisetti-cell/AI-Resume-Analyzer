def generate_roadmap(missing_skills):
    roadmap = []

    if not missing_skills:
        return ["🎉 Excellent! Your resume already matches this role."]

    week = 1
    skill_plans = {
        "docker": "Learn Docker Basics + Containerize 1 app",
        "fastapi": "Build REST APIs using FastAPI",
        "mlflow": "Learn MLflow for Model Tracking",
        "tensorflow": "Learn TensorFlow + Build 1 DL model",
        "pytorch": "Learn PyTorch + Computer Vision Project",
        "power bi": "Learn Power BI + Create 2 Dashboards",
        "excel": "Learn Advanced Excel + Pivot Tables",
        "aws": "Learn AWS EC2, S3 + Deploy 1 project",
        "git": "Learn Git + GitHub Workflows"
    }

    for skill in missing_skills[:4]: # max 4 weeks
        skill_lower = skill.lower()
        task = skill_plans.get(skill_lower, f"Learn {skill.title()} + Build Mini Project")
        roadmap.append(f"Week {week}: {task}")
        week += 1

    return roadmap