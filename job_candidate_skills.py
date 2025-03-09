req_skills = {'Python', 'Django', 'SQL', 'Git'}
candidate_skills = {'Python', 'Flask', 'Git', 'JavaScript'}

match_skills = req_skills.intersection(candidate_skills)
miss_skills = req_skills.difference(candidate_skills)
extra_skills = candidate_skills.difference(req_skills)
print (f'Matched Skills: {", ".join(match_skills)}')
print (f'Missing Skills: {", ".join(miss_skills)}')
print (f'Extra Skills: {", ".join(extra_skills)}')