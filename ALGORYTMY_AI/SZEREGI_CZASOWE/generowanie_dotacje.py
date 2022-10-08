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
