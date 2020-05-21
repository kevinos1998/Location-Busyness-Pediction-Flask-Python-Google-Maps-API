import pickle
from datetime import datetime
from flask import render_template, request
from app import app
from app.forms import inputForm
import pandas as pd

clf = pickle.load(open('model.pkl','rb'))

# Current date time functions
def getCurrHour():
    return datetime.now().hour
def getCurrDay():
    return datetime.now().weekday()
def getCurrMonth():
    return datetime.now().month

# This function is executed on load of root and home page
# View function for root and home page
@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def home():
    # List of building Ids
    buildingIDs = range(1,49)
    # Array for predictions
    xP = []
    # Set the form for the page to the input form
    form = inputForm();
    # If its POST user user input data
    if request.method == "POST":
        hour = request.form["Hour"];
        day = request.form["Day"];
        month = request.form["Month"];
        form.Hour.data = hour
        form.Day.data = day
        form.Month.data = month
    # Else if GET then use current date and time
    else:
        hour = getCurrHour()
        day = getCurrDay()
        month = getCurrMonth()
    # Get predictions
    for x in buildingIDs:
        dfp = pd.DataFrame({"BuildingID": [x],
                            "dayOfWeek": [day],
                            "hour": [hour],
                            "month": [month]})
        xP.append(clf.predict(dfp)[0])
    # Render the home page template and pass form and predictions
    return render_template("home.html", form=form, data=xP)
