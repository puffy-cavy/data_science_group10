import pandas as pd
import datetime
import csv



state_name = "New York"

policy_df = pd.read_csv('policies.csv')
# print(policy_df[["State", "Closed K-12 public schools"]])


#califonia first time close
curdate = policy_df.loc[policy_df['State'] == state_name]["Closed other non-essential businesses"].to_string(index=False).strip()
cur = curdate.split('/')
cur[0],cur[2] = cur[2],cur[0]
cur[1],cur[2] = cur[2],cur[1]
inputdate = '-'.join(cur)
bus_close = datetime.datetime.strptime(inputdate, '%Y-%m-%d')


bus_close = bus_close.isocalendar()[1]       # 索引为[1]，就可以求出一年的第多少周


#califonia first time reopen
curdate = policy_df.loc[policy_df['State'] == state_name]["Reopened other non-essential retail"].to_string(index=False).strip()
cur = curdate.split('/')
cur[0],cur[2] = cur[2],cur[0]
cur[1],cur[2] = cur[2],cur[1]
inputdate = '-'.join(cur)
my_dt = datetime.datetime.strptime(inputdate, '%Y-%m-%d')

reopen = my_dt.isocalendar()[1]
start_to_open01 = reopen


#Closed restaurants
#califonia first time reopen
curdate = policy_df.loc[policy_df['State'] == state_name]["Closed restaurants"].to_string(index=False).strip()
cur = curdate.split('/')
cur[0],cur[2] = cur[2],cur[0]
cur[1],cur[2] = cur[2],cur[1]
inputdate = '-'.join(cur)
my_dt = datetime.datetime.strptime(inputdate, '%Y-%m-%d')

close_rest = my_dt.isocalendar()[1]

#Reopened restaurants
curdate = policy_df.loc[policy_df['State'] == state_name]["Reopened restaurants"].to_string(index=False).strip()
cur = curdate.split('/')
cur[0],cur[2] = cur[2],cur[0]
cur[1],cur[2] = cur[2],cur[1]
inputdate = '-'.join(cur)
my_dt = datetime.datetime.strptime(inputdate, '%Y-%m-%d')
reopen_rest = my_dt.isocalendar()[1]



#state_df = pd.DataFrame(columns=['weeks','mask','restaurant','non-essential business','bars','movie theater','incident ratio'])


curdate = policy_df.loc[policy_df['State'] == state_name]["Closed bars"].to_string(index=False).strip()
cur = curdate.split('/')
cur[0],cur[2] = cur[2],cur[0]
cur[1],cur[2] = cur[2],cur[1]
inputdate = '-'.join(cur)
bar_dt = datetime.datetime.strptime(inputdate, '%Y-%m-%d')
close_bar = bar_dt.isocalendar()[1]
if cur[0] > '2020':
    close_bar+=52



curdate = policy_df.loc[policy_df['State'] == state_name]["Reopened bars"].to_string(index=False).strip()
cur = curdate.split('/')
cur[0],cur[2] = cur[2],cur[0]
cur[1],cur[2] = cur[2],cur[1]
inputdate = '-'.join(cur)
reopen_bar = datetime.datetime.strptime(inputdate, '%Y-%m-%d')
bar_reopen = reopen_bar.isocalendar()[1]
if cur[0] > '2020':
    bar_reopen+=52








curdate = policy_df.loc[policy_df['State'] == state_name]["Closed movie theaters"].to_string(index=False).strip()
cur = curdate.split('/')
cur[0],cur[2] = cur[2],cur[0]
cur[1],cur[2] = cur[2],cur[1]
inputdate = '-'.join(cur)
movie = datetime.datetime.strptime(inputdate, '%Y-%m-%d')
movie_close = movie.isocalendar()[1]
if cur[0] > '2020':
    movie_close += 52

curdate = policy_df.loc[policy_df['State'] == state_name]["Reopened movie theaters"].to_string(index=False).strip()
cur = curdate.split('/')
cur[0],cur[2] = cur[2],cur[0]
cur[1],cur[2] = cur[2],cur[1]
inputdate = '-'.join(cur)
movieend = datetime.datetime.strptime(inputdate, '%Y-%m-%d')
movie_reopen = movieend.isocalendar()[1]
if cur[0] > '2020':
    movie_reopen += 52

policy_df = pd.read_csv('mask_policy.csv')

curdate = policy_df.loc[policy_df['State'] == state_name]["Public face mask mandate start"].to_string(index=False).strip()
cur = curdate.split('/')
cur[0],cur[2] = cur[2],cur[0]
cur[1],cur[2] = cur[2],cur[1]
inputdate = '-'.join(cur)
mask_dt = datetime.datetime.strptime(inputdate, '%Y-%m-%d')
mask_start = mask_dt.isocalendar()[1]
if cur[0] > '2020':
    mask_start+=52


curdate = policy_df.loc[policy_df['State'] == state_name]["Face mask mandate end"].to_string(index=False).strip()
cur = curdate.split('/')
cur[0],cur[2] = cur[2],cur[0]
cur[1],cur[2] = cur[2],cur[1]
inputdate = '-'.join(cur)
mask_dt_end = datetime.datetime.strptime(inputdate, '%Y-%m-%d')
mask_end = mask_dt_end.isocalendar()[1]
if cur[0] > '2020':
    mask_end+=52




def create_csv():
    path = "NYC.csv"
    with open(path,'w') as f:
        csv_write = csv.writer(f)
        csv_head = ['weeks','mask','restaurant','non-essential business','bars','movie theater']
        csv_write.writerow(csv_head)

def write_csv(row):
    path  = "NYC.csv"
    with open(path,'a+') as f:
        csv_write = csv.writer(f)
        data_row = row
        csv_write.writerow(data_row)

row = [0,0,0,0,0,0]
create_csv()
write_csv(row)

for i in range(1,105):
    row[0] = i
    if i>=bus_close:
        row[3] = 1
    if i>=start_to_open01:
        row[3] = 0
    if i>= close_rest:
        row[2] = 1
    if i>= reopen_rest:
        row[2] = 0

    if i>= mask_start:
        row[1] = 1
    if i>= mask_end:
        row[1] = 0
    if i >= close_bar:
        row[4] = 1
    if i >= bar_reopen:
        row[4] = 0
    if i >= movie_close:
        row[5] = 1
    if i >= movie_reopen:
        row[5] = 0

    write_csv(row)





