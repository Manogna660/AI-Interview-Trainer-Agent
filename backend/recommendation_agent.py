def recommend(score):

    if score >= 8:

        return [

            "Advanced Machine Learning",

            "System Design",

            "Mock Interviews"

        ]

    elif score >=5:

        return [

            "Python Practice",

            "SQL",

            "Statistics"

        ]

    else:

        return [

            "Python Basics",

            "Data Structures",

            "Communication Skills"

        ]