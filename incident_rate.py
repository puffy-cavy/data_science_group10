from isoweek import Week
import datetime
import pandas as pd
import gc


# print("date_to_week", datetime.date(2020, 4, 12).isocalendar()[1])
#state vaccination:https://github.com/owid/covid-19-data/blob/master/public/data/vaccinations/us_state_vaccinations.csv

state_name = "Pennsylvania"
incident_rate_list = []
weeks_list = [i for i in range(1, 105)]
for i in weeks_list:
    w = Week(2020, i)
    next_w = Week(2020, i+1)
    start_date = w.monday()
    end_date = next_w.monday()
    start_date_string = start_date.strftime("%m-%d-%Y")
    end_date_string = end_date.strftime("%m-%d-%Y")
    print("the starting day of week %s is %s" % (i, start_date_string))
    print("the end day of week %s is %s" % (i, end_date_string))
    try:
        start_df = pd.read_csv('COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports_us/{}.csv'.format(start_date_string))
        end_df = pd.read_csv('COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports_us/{}.csv'.format(end_date_string))
    except OSError:
        print("case file not found for week %s" % (i))
        incident_rate_list.append(None)
        continue
    start_rate = start_df.loc[start_df['Province_State'] == state_name]["Incident_Rate"].to_string(index=False).strip()
    end_rate = end_df.loc[end_df['Province_State'] == state_name]["Incident_Rate"].to_string(index=False).strip()
    rate_difference = float(end_rate) - float(start_rate)
    incident_rate_list.append(rate_difference)
    print("the increasing of incident rate of that day is:", rate_difference)
    del start_df
    del end_df
    gc.collect()

total_df = pd.DataFrame(columns=['weeks','incident_ratio'])
total_df['incident_ratio'] = incident_rate_list
total_df['weeks'] = weeks_list
file_path = "state_incidents/{}.csv".format(state_name)
total_df.to_csv(file_path, index=False)
del total_df
gc.collect()
