valid_states = ("FL", "NY", "CA", "TX", "NC")

expected_salaries = {"NY": 90000, "CA": 70000, "FL": 80000, "NC": 50000, "TX": 60000}


def calculate_expected_salary(number_of_experience_years, user_information, number_of_education_years,
                              is_developer, is_designer, users_coding_languages, users_design_tools):
    try:
        expected_salary = expected_salaries[user_information["state"].upper()]
        number_of_education_years_as_an_integer = int(number_of_education_years)

        # "9" can be passed to int()
        # "nine" cannot be passed to int()
    except KeyError:
        return "*******************  INPUT ERROR: Please enter a valid State   ******************"
    except ValueError:
        return "*******************  INPUT ERROR: Please enter a valid number for years of learning experience   ******************"
    else:  # this else only gets executed if the exception is not raised/called

        new_expected_salary = 0
        if number_of_experience_years == 1:
            new_expected_salary = expected_salary - 5000
        elif number_of_experience_years == 2:
            new_expected_salary = expected_salary - 3000
        elif number_of_experience_years == 3:
            new_expected_salary = expected_salary + 1000
        elif number_of_experience_years == 4:
            new_expected_salary = expected_salary + 5000
        else:
            return "Please insert a valid option - 1, 2, 3, or 4."

        if is_developer:
            if len(users_coding_languages) < 3:
                new_expected_salary = new_expected_salary - 10000
                # return "Learn more languages: Deduct 10k from the expected salary. Keep Pushing!"
            elif len(users_coding_languages) > 3:
                new_expected_salary = new_expected_salary + 10000
            else:
                new_expected_salary = new_expected_salary + 5000
            if number_of_education_years_as_an_integer > 3:
                new_expected_salary = new_expected_salary + 5000
            else:
                new_expected_salary = new_expected_salary - 5000
            # return "Expect $" + str(new_expected_salary) + " for your level of experience."

        if is_designer:
            if len(users_design_tools) < 3:
                new_expected_salary = new_expected_salary - 10000
                # return "Learn more software: Deduct 10k from the expected salary. Keep Pushing!"
            elif len(users_design_tools) > 3:
                new_expected_salary = new_expected_salary + 10000
            else:
                new_expected_salary = new_expected_salary + 5000
            if number_of_education_years_as_an_integer > 3:
                new_expected_salary = new_expected_salary + 5000
            else:
                new_expected_salary = new_expected_salary - 5000

        result_message = ""
        # for state in users_info:
        for state in expected_salaries:
            salary = expected_salaries[state]
            result_message = result_message + "Your expected Salary living in " + state + " could have been " + str(salary) + ". " + "\n"
            # print("Your expected Salary living in " + state + " could have been " + str(salary))

        result_message = result_message + "Expect $" + str(new_expected_salary) + " for your level of experience." + "\n"
        # print("Expect $" + str(new_expected_salary) + " for your level of experience.")

        return result_message
