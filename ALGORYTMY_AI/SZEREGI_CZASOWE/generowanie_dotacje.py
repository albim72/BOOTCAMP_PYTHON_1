import pdb
import numpy as np
import pandas as pd

#status członkostwa
years = ['2016','2017','2018','2019','2020']
userStatus = ['bronze','silver','gold','inactive']

usersYears = np.random.choice(years,1000,p=[0.1,0.1,0.15,0.3,0.35])
userStats = np.random.choice(userStatus,1000,p=[0.5,0.3,0.1,0.1])

yearJoined = pd.DataFrame({'uearJoined':usersYears,
                           'userStats':userStats})

print(yearJoined.head())

#definicja e-mails
NUM_EMAILS_SENT_WEEKLY = 3

#rodzaj zachowania
def never_opens(period_rng):
    return []

def constant_open_rate(period_rng):
    n,p = NUM_EMAILS_SENT_WEEKLY, np.random.uniform(0,1)
    num_opened = np.random.binomial(n,p,len(period_rng))
    return num_opened

def open_rate_with_factor_change(period_rng,fac):
    if len(period_rng) < 1:
        return []

    times =  np.random.randint(0,len(period_rng),int(0.1*len(period_rng)))
    try:
        n, p = NUM_EMAILS_SENT_WEEKLY, np.random.uniform(0, 1)
        num_opened = np.zeros(len(period_rng))
        for pd in range(0,len(period_rng),2):
            num_opened[pd:(pd+2)] = np.random.binomial(n,p,2)
            p = max(min(1,p*fac),0)
    except:
        num_opened[pd] = np.random.binomial(n,p,1)
    for t in times:
        num_opened[t] = 0
    return num_opened

def increasing_open_rate(period_rng):
    return open_rate_with_factor_change(period_rng, np.random.uniform(1.01,1.30))

def decreasing_open_rate(period_rng):
    return open_rate_with_factor_change(period_rng, np.random.uniform(0.5,0.99))

def random_weekly_time_delta():
    days_of_week = [d for d in range(7)]
    hours_of_day = [h for h in range(11,23)]
    minute_of_hour = [m for m in range(60)]
    second_of_minute = [s for s in range(60)]

    return pd.Timedelta(str(np.random.choice(days_of_week)) + " days") + \
            pd.Timedelta(str(np.random.choice(hours_of_day)) + " hours") + \
            pd.Timedelta(str(np.random.choice(minute_of_hour)) + " minutes") + \
            pd.Timedelta(str(np.random.choice(second_of_minute)) + " seconds")


#zachowanie dotacji
def produce_donations(period_rng,user_behavior,num_emails,use_id,user_join_year):
    donation_amounts = np.array([0,25,50,75,100,250,500,1000,1500,2000])
    user_has = np.random.choice(donation_amounts)
    user_gives = num_emails/(NUM_EMAILS_SENT_WEEKLY*len(period_rng))*user_has
    user_gives_idx = np.where(user_gives >= donation_amounts)[0][-1]
    user_gives_idx = max(min(user_gives_idx,len(donation_amounts)-2),1)

    num_times_gave = np.random.poisson(2)*(2020-user_join_year)
    times = np.random.randint(0,len(period_rng),num_times_gave)

    donations = pd.DataFrame({'user':[],'amount':[],'timestamp':[]})
    for n in range(num_times_gave):
        donations = donations.append(pd.DataFrame({'user':[use_id],
                                                   'amount':[donation_amounts[user_gives_idx+np.random.binomial(1,.3)]],
                                                   'timestamp':[str(period_rng[times[n]].start_time + random_weekly_time_delta())]}))
    if donations.shape[0] > 0:
        donations = donations[donations.amount != 0]
    return donations
                    
