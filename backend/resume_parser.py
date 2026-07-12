import re

def extract_skills(text):

    skills = [

        "Python",
        "Java",
        "C",
        "C++",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "Data Science",
        "Pandas",
        "NumPy",
        "TensorFlow",
        "Scikit-learn",
        "Power BI",
        "Excel",
        "Statistics"

    ]

    found=[]

    for skill in skills:

        if re.search(skill,text,re.IGNORECASE):

            found.append(skill)

    return found