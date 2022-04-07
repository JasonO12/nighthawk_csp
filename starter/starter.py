import requests
from flask import Blueprint, render_template, request, url_for, redirect
from flask_login import login_required
from cruddy.query import *
from algorithm.image import image_data

from pathlib import \
    Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and
# -linux-11a072b58d5f

app_starter = Blueprint('starter', __name__,
                        url_prefix='/starter',
                        template_folder='templates/starter/',
                        static_folder='static',
                        static_url_path='static/assets')

# Flask-Login directs unauthorised users to this unauthorized_handler
# @login_manager.unauthorized_handler
# def unauthorized():
#     """Redirect unauthorized users to Login page."""
#     return redirect(url_for('starter.starter_login'))
#
#
# # if login url, show phones table only
# @app_starter.route('/login/', methods=["GET", "POST"])
# def starter_login():
#     # obtains form inputs and fulfills login requirements
#     if request.form:
#         email = request.form.get("email")
#         password = request.form.get("password")
#         if login(email, password):       # zero index [0] used as email is a tuple
#             return redirect(url_for('starter.greet'))
#
#     # if not logged in, show the login page
#     return render_template("s_login.html")
#
#
# @app_starter.route('/authorize/', methods=["GET", "POST"])
# def starter_authorize():
#     # check form inputs and creates user
#     if request.form:
#         # validation should be in HTML
#         user_name = request.form.get("user_name")
#         email = request.form.get("email")
#         password1 = request.form.get("password1")
#         password2 = request.form.get("password1")
#         phone = request.form.get("phone")
#         if authorize(user_name, email, password1, phone):    # zero index [0] used as user_name and email are type tuple
#             return redirect(url_for('starter.starter_login'))
#     # show the auth user page if the above fails for some reason
#     return render_template("s_authorize.html")


@app_starter.route('/greet', methods=['GET', 'POST'])
@login_required
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greet.html", name=name)
    # starting and empty input default
    return render_template("greet.html", name="World")


@app_starter.route('/binary/')
def binary():
    return render_template("binary.html")


@app_starter.route('/rgb/')
def rgb():
    path = Path(app_starter.root_path) / "static" / "img"
    return render_template('rgb.html', images=image_data(path))


@app_starter.route('/joke', methods=['GET', 'POST'])
def joke():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/joke"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/joke"
    response = requests.request("GET", url)
    return render_template("joke.html", joke=response.json())


@app_starter.route('/jokes', methods=['GET', 'POST'])
def jokes():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/jokes"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/jokes"

    response = requests.request("GET", url)
    return render_template("jokes.html", jokes=response.json())


@app_starter.route('/covid19', methods=['GET', 'POST'])
def covid19():
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
    headers = {
        'x-rapidapi-key': "dec069b877msh0d9d0827664078cp1a18fajsn2afac35ae063",
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    stats = response.json()

    """
    # uncomment this code to test from terminal
    world = response.json().get('world_total')
    countries = response.json().get('countries_stat')
    print(world['total_cases'])
    for country in countries:
        print(country["country_name"])
    """
    return render_template("covid19.html", stats=stats)

@app_starter.route('/life')
def life():
    return render_template("../frontend/templates/frontend/life.html")
