#   Codewars 1: The Office I - Outed
def outed(meet, boss):
    average = (sum(meet.values()) + meet[boss])/ len(meet)
    if average <= 5:
        return "Get Out Now!"
    else:
        return "Nice Work Champ!"

#   Codewars 2: The Office II - Boredom Score

departments = {
    "accounts" : 1,
    "finance" : 2,
    "canteen" : 10,
    "regulation" : 3,
    "trading" : 6,
    "change" : 6,
    "IS" : 8,
    "retail" : 5,
    "cleaning" : 4,
    "pissing about" : 25
}

def boredom(staff):
    total_score = 0
    chosen_departments = staff.values()
    for department in chosen_departments:
        total_score += departments[department]
    if total_score <= 80:
        return "kill me now"
    elif 100 > total_score > 80:
        return "i can handle this"
    else:
        return "party time!!"
