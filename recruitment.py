# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from
def get_skills():
    skills = ["Python" , "C++" , "Javascript"]
    return skills

#print(get_skills())

# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything

skills = get_skills()
def show_skills(skills):
    print("Skills:")
    for index, skill in enumerate(skills, 1): # 1 way to do numbrec list
        print(f"{index}. {skill}")
        
    # for skill in skills: # my way to do this 
    #     print(skills.index(skill) +1, end='.')
    #     print("",skill)
        
# show_skills(skills)

# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
def get_user_skills(skills):
    show_skills(skills)
    skill1 = int(input('Choose a skill from above by entering its number: '))
    skill2 = int(input('Choose another skill from above by entering its number: '))
    lst = [skills[skill1 - 1], skills[skill2 -1]]
    return lst

#print(get_user_skills(skills))


# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
cv = {}
def get_user_cv(skills):
    name = input('What is your name: ')
    age = int(input('What is your age: '))
    experience = int(input('What is your years experience: '))
    cv = {
        "name": name,
        "age": age,
        "experience": experience,
        "skills": get_user_skills(skills)
    }
    return cv


# This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):
    if (25 <= cv["age"] <= 40 and cv["experience"] > 3 and desired_skill in cv["skills"]):
        return True
    else:
        return False
    
# print(check_acceptance(get_user_cv(skills),"Python"))

def main():
    print("Welcome to the special recruitment program, please answer the following questions:")
    skills = get_skills()
    user_cv =get_user_cv(skills)
    if check_acceptance(user_cv, "Python") == True:
        print(f"You have been accepted, {user_cv['name'] } :)")
    else:
        print("You have been rejected :(")
        
    

if __name__ == "__main__":
    main()
