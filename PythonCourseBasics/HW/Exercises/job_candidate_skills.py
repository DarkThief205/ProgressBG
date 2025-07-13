#--------------------------------------------Task:-------------------------------------------------#

# Required and candidate skills
job_skills = {'Python', 'Django', 'SQL', 'Git'}
candidate_skills = {'Python', 'Flask', 'Git', 'JavaScript'}

matched_skills = candidate_skills & job_skills
missing_skills = job_skills - candidate_skills
extra_skills = candidate_skills - job_skills

print("Matched Skills:", ", ".join(sorted(matched_skills)))
print("Missing Skills:", ", ".join(sorted(missing_skills)))
print("Extra Skills:", ", ".join(sorted(extra_skills)))
#--------------------------------------------------------------------------------------------------#