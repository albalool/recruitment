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
    for skill in skills:
        print(skills.index(skill) +1, end='.')
        print("",skill)
#   for skill in enumerate(skills):
 #       print(skill)   
show_skills(skills)

# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
def get_user_skills(skills):
    show_skills(skills)
    skill1 = input('Choose skill: ')
    skill2 = input('Choose another skill: ')
    lst = [skill1, skill2]
    return lst

# print(get_user_skills(skills))


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
        "experince": experience,
        "skills": get_user_skills(skills)
    }
    return cv


# This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):
    if (25 >= cv["age"] <= 40 and cv["experince"] > 3 and desired_skill in cv["skills"]):
        return True
    
# print(check_acceptance(get_user_cv(skills),"Python"))

# def main():
#     print("Welcome to the special recruitment program, please answer the following questions:")
#     if check_acceptance(get_user_cv(skills),cv["skills"]) == True:
#         return print("You have been accepted")
    

# if __name__ == "__main__":
#     main()
