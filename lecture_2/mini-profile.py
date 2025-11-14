def generate_profile(age: int) -> str:
    if 0 < age < 12:
        return 'Child'
    elif 13 < age < 19:
        return 'Teenager'
    return 'Adult'


user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year
hobbies = []
hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
while hobby != 'stop':
    hobbies.append(hobby)
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
life_stage = generate_profile(current_age)
user_profile = {'name': user_name, 'age': current_age, 'stage': life_stage, 'hobbies':
    hobbies}

print(f'''
---
Profile Summary:
Name: {user_profile.get("name")}
Age: {user_profile.get("age")}
Life Stage: {user_profile.get("stage")}''')
if len(user_profile.get("hobbies")) == 0:
    print("You didn't mention any hobbies.", "---", sep='\n')
else:
    print(f'Favorite Hobbies ({len(user_profile.get("hobbies"))}):')
    for hobby in user_profile.get("hobbies"):
        print(f'- {hobby}')
    print("---")
