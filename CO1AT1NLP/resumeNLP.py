import re

resume = """
Name: Kavya K
Email: kavya@gmail.com
Mobile: 9876543210
Skills: Python, SQL, Machine Learning, NLP
Experience: 3 years
"""

# Extract Name
name = re.search(r"Name:\s*(.*)", resume)
if name:
    name = name.group(1)

# Extract Email
email = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', resume)

# Extract Mobile Number
mobile = re.findall(r'\b[6-9]\d{9}\b', resume)

# Detect Skills
skills = ["Python", "Java", "SQL", "Machine Learning", "NLP"]
found_skills = []

for skill in skills:
    if re.search(skill, resume, re.IGNORECASE):
        found_skills.append(skill)

# Extract Experience
experience = re.search(r'(\d+)\s+years', resume)
if experience:
    years = int(experience.group(1))
else:
    years = 0

# Structured Summary
print("------ Candidate Profile ------")
print("Name :", name)
print("Email :", email)
print("Mobile :", mobile)
print("Skills :", found_skills)
print("Experience :", years, "years")

# Eligibility Check
print("\nEligibility Status")

if years >= 2 and "Python" in found_skills:
    print("Candidate Shortlisted")
else:
    print("Candidate Not Eligible")
