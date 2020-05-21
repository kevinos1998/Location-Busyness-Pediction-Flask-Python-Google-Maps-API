from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
# Form to take user request input for prediction
# Fields default to current datetime
class inputForm(FlaskForm):
    Hour = SelectField(u'Hour', choices=[(0, '0-1'), (1, '1-2'), (2, '2-3'), (3, "3-4"),(4, "4-5"),(5, "5-6"),(6, "6-7"),(7, "7-8"),(8, "8-9"),(9, "9-10"),(10, "10-11"),(11, "11-12"),(12, "12-13"),(13, "13-14"),(14,"14-15"),(15, "15-16"),(16, "16-17"),(17, "17-18"),(18, "18-19"),(19, "19-20"),(20, "20-21"),(21, "22-23"),(22, "22-23"),(23, "23-24")],default=datetime.now().hour);
    Day = SelectField(u'Day', choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')],default=datetime.now().weekday());
    Month = SelectField(u'Month', choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'),(5, 'May'), (6, 'June'), (7, 'July'), (8, "August"),(9, "September"),(10, "October"),(11, "November"),(12, "December")],default=datetime.now().month);
    submit = SubmitField('Predict')
