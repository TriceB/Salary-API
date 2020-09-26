from flask import Flask, render_template, request
from calculate_api.utilities import calculator
import json

app = Flask(__name__)   # activate the Flask application / instantiate the Flask object


@app.route('/hello_world')
def hello_world():
    return '<h1><b>Hello, Tribe!</b></h1>'


@app.route('/')
def candidate_form():
    return render_template("index.html")


@app.route('/open-jobs')
def open_jobs():
    f = open("data.json", "r")  # open up the file in read mode
    data_contents = f.read()    # Read data from file and store in variable as raw text
    jobs_as_json = json.loads(data_contents)    # turn the raw text into a Python object

    result_message = ""
    for job in jobs_as_json:    # loop over the list of job dictionaries
        print(job)
        print(job["job_title"])
        print(job["location"])
        result_message = result_message + job["job_title"] + "\n"
        result_message = result_message.replace('\n', '<br/>')
    return render_template("result.html", message=result_message)


@app.route("/calculate_salary", methods=["POST"])
def calculate_salary():
    # capture the API request
    if request.method == "POST":
        f = open("candidates_db.txt", "a")
        profession = int(request.form['profession'])    # 1 = Developer, 2 = Designer
        f.write("Profession: " + str(profession) + "\n")
        number_of_experience_years = int(request.form['experience'])
        f.write("Years of Experience: " + str(number_of_experience_years) + "\n")

        languages = request.form['languages']
        users_coding_languages = languages.split(",")
        f.write("List of Coding Languages: " + str(users_coding_languages) + "\n")

        design_tools = request.form['designTools']
        users_design_tools = design_tools.split(",")
        f.write("List of Design Tools: " + str(design_tools) + "\n")

        dob = request.form['dob']
        f.write("Date of Birth: " + dob + "\n")
        full_name = request.form['fullName']
        f.write("Full Name: " + full_name + "\n")

        age = int(request.form['age'])
        f.write("Age: " + str(age) + "\n")

        country = request.form['country']
        f.write("Country: " + country + "\n")
        state = request.form['state']
        f.write("State: " + state + "\n")
        number_of_education_years = int(request.form['educationYears'])
        f.write("Years of Education: " + str(number_of_education_years) + "\n")
        f.close()

        is_developer = False
        is_designer = False
        if int(profession) == 1:
            is_developer = True
        else:
            is_designer = True

        users_info = {"dob": dob, "full_name": full_name, "age": age, "country": country, "state": state,
                      "is_active": True, "number_of_education_years": number_of_education_years}

        result_message = calculator.calculate_expected_salary(number_of_experience_years, users_info,
                                                              number_of_education_years, is_developer, is_designer,
                                                              users_coding_languages, users_design_tools)
        result_message = result_message.replace('\n', '<br/>')

        f = open("response.txt", "r")
        file_contents = f.read()
        final_message = result_message + "\n" + file_contents + "\n"
        f.close()
        # return API response
        return render_template("result.html", message=final_message)
    else:   # if a GET request is attempted
        return "Please submit a POST request"
