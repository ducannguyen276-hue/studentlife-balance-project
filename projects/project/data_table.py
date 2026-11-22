from datetime import datetime
import tkinter as tk

from data_management import (
    get_daily_log
)
def genertate_dataframe():
    datas = get_daily_log()

    data_frame ={"date":[],
                 "categories":[],
                 "activities":[]}

    for i in datas:
      # Parse your input date string
        date_obj = datetime.strptime(i[0], "%Y-%m-%d")

        # Format as "Sat, Nov 21"
        formatted_date = date_obj.strftime("%a, %b %d")  

        data_frame["date"] += [formatted_date]
        data_frame["categories"] += [i[1]]
        data_frame["activities"] += [i[2]]

    print(data_frame)

