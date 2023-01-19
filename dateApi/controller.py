from flask import request, Blueprint, views
from datetime import datetime, timedelta

date_api = Blueprint("test", __name__, url_prefix="/question")


class AddDaysAPI(views.MethodView):
    """
    API to return answer based on add_days question
    """
    def get(self):
        days_to_add = int(request.args.get('days'))
        current_date = datetime.now()
        new_date = current_date + timedelta(days=days_to_add)
        return {"new_date": new_date}


class AddWeeksAPI(views.MethodView):
    """
    API to return answer based on add_weeks question
    """
    def get(self):
        weeks_to_add = int(request.args.get('weeks'))
        current_date = datetime.now()
        new_date = current_date + timedelta(weeks=weeks_to_add)
        return {"new_date": new_date}


class SubtractDaysAPI(views.MethodView):
    """
    API to return answer based on subtract_weeks question
    """
    def get(self):
        days_to_subtract = int(request.args.get('days'))
        subtract_from = request.args.get('date')
        new_date = datetime.strptime(subtract_from, '%m/%d/%y') - timedelta(days=days_to_subtract)
        return {"new_date": new_date}





date_api.add_url_rule("/add_days", view_func=AddDaysAPI.as_view("date_add_api"))
date_api.add_url_rule("/add_weeks", view_func=AddWeeksAPI.as_view("week_add_api"))
date_api.add_url_rule("/subtract_days", view_func=SubtractDaysAPI.as_view("date_subtract_api"))