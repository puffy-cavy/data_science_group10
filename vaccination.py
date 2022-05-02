from isoweek import Week
import datetime
import pandas as pd
import gc
import math


# print("date_to_week", datetime.date(2021, 6, 1).isocalendar()[1])
# w = Week(2020, 100)
# print(w.friday())
#
# state vaccination:https://github.com/owid/covid-19-data/blob/master/public/data/vaccinations/us_state_vaccinations.csv
# variant data from: https://www.cdc.gov/museum/timeline/covid19.html:
# 2021/06/01 Delta - week 75 (week 74 on the form)
# 2021/11/26 Omicron - week

state_name = "Texas"
vaccination_list = []
weeks_list = [i for i in range(1, 105)]
df = pd.read_csv('state_vaccination.csv')
for i in weeks_list:
    w = Week(2020, i)
    start_date = w.friday().strftime("%Y-%m-%d")
    print("the starting day of week %s is %s" % (i, start_date))
    people_fully_vaccinated_per_hundred = df.loc[(df['location'] == state_name) & (df['date'] == start_date)]["total_vaccinations_per_hundred"].to_string(index=False).strip()
    try:
        float(people_fully_vaccinated_per_hundred)

    except ValueError:
        print("NOT found for the week %s, date is %s" % (i, start_date))
        vaccination_list.append(None)
        continue

    if math.isnan(float(people_fully_vaccinated_per_hundred)):
        print("Nan found for the week %s, date is %s" % (i, start_date))
        vaccination_list.append(None)
    else:
        print("vaccination data found for the week %s, date is %s, people_fully_vaccinated_per_hundred is %f" % (i, start_date, float(people_fully_vaccinated_per_hundred)))
        vaccination_list.append(people_fully_vaccinated_per_hundred)


total_df = pd.DataFrame(columns=['weeks','people_fully_vaccinated_per_hundred'])
file_path = "vaccination_data/{}.csv".format(state_name)
total_df['weeks'] = weeks_list
total_df['people_fully_vaccinated_per_hundred'] = vaccination_list
total_df.to_csv(file_path, index=False)

del total_df
gc.collect()
