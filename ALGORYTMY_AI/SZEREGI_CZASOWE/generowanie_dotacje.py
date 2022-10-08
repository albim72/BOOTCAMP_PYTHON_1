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

