from faker import Faker
from faker.providers import internet
from faker.providers import DynamicProvider
import datetime

import pandas as pd
from pandas.tseries.offsets import MonthEnd

import random

industry = DynamicProvider(
     provider_name="industry",
     elements=["fishing","construction","retail","travel"],
)

channel = DynamicProvider(
     provider_name="channel",
     elements=["online","phone","instore"],
)

region = DynamicProvider(
     provider_name="region",
     elements=["NSW","QLD","VIC","Den Haag"],
)

enddate=datetime.date(2022,2,28)



df=pd.DataFrame()

i=0
numpeeps=500

while i<=numpeeps:
    

    fake = Faker()

    fake.add_provider(internet)
    fake.add_provider(industry)
    fake.add_provider(channel)
    fake.add_provider(region)
    
    
    cursordate = datetime.date(2020,1,31)

    
    
    while cursordate<=enddate:
    
        record = {
            'busn_date':cursordate,
            'name':fake.name(),
            'ip':fake.ipv4_private(),
            'industry':fake.industry(),
            'region':fake.region(),
            'channel':fake.channel(),
            'address':fake.address(),
            'balance':random.randint(0, 1000000)
            }
    
        
        df=df.append(record, ignore_index=True)
        
        
        
        
        
        cursordate=(cursordate+MonthEnd(1)).date()


    i=i+1
    

df.to_csv('pretend_data.csv',index=False)    