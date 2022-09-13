#Examples of fake data generation:

import pandas as pd
import numpy as np
import random
from faker import Faker
from faker.config import AVAILABLE_LOCALES

# create some fake data
fake = Faker('en_GB')

# function to create a dataframe with fake values for our workers
def make_spe(num):
    
    # Depth
    depth_list = ['0', '1', '2', '3', '4','5']
    country_list = ['GB', 'DE', 'FR', 'NL', 'US','SG']
    percent_list = ['1', '0.80','0.70','0.25','0.75','0.50' ]
    nace_code_list = ['K', 'L','I', 'C', 'N']
    no_employee_list = ['1', '4', '6','10','20', 'NA']
    year_list = ['2019']
    

# assign items from list with different probabilities

    fake_spe = [{
                  'Depth': np.random.choice(depth_list, p=[0.30, 0.25, 0.25, 0.15, 0.05, 0.00]),
                  'T_Percent': np.random.choice(percent_list, p=[0.10, 0.60, 0.10, 0.10, 0.05, 0.05]), 
                  'D_Percent': np.random.choice(percent_list, p=[0.10, 0.60, 0.10, 0.10, 0.05, 0.05]), 
                  'Subsidiary_BvDID':str(np.random.choice(country_list, p=[0.60, 0.10, 0.10, 0.10, 0.05, 0.05])) + str(random.randrange(10000000, 99999999)),
                  'Postcode' : fake.postcode(),
                  'Shareholder': str(np.random.choice(country_list, p=[0.60, 0.10, 0.10, 0.10, 0.05, 0.05])) + str(random.randrange(10000000, 99999999)),
                  'NACE_code' : np.random.choice(nace_code_list),
                  'Number_of_employees_(last_vale)_(LY)': np.random.choice(no_employee_list, p=[0.50, 0.20, 0.10, 0.10, 0.00, 0.10]),
                  'Subsidiary_Country_ISO_Code' : np.random.choice(country_list, p=[0.60, 0.10, 0.10, 0.10, 0.05, 0.05]),
                  'Shareholder_Country_ISO_Code': np.random.choice(country_list, p=[0.60, 0.10, 0.10, 0.10, 0.05, 0.05]),
                  'Total_assents_th_GBP_(LY)_47': random.randrange(0, 50000),
                  'Operating_revenue_(Turnover)_th_GBP_(LY)': random.randrange(0, 30000),
                  'Year': np.random.choice(year_list),
                  'apex_UK' : 'GB'+ str(random.randrange(10000000, 99999999))
                  } for x in range(num)]
        
    return fake_spe

spe_df = pd.DataFrame(make_spe(num=20))
#worker_df.head()

#spe_df.to_csv('Fake_SPE_data.csv', index=False)

pd.DataFrame(spe_df)

import pandas as pd
import numpy as np
import random
from faker import Faker

# function to create widget data

def make_widget_data(num):
    
    fake_widgets = [{'Item Number':id(y),
                     'Step 1':np.random.gamma(shape=3, scale=1),
                     'Step 2':np.random.normal(5), 
                     'Step 3':np.random.exponential(4)} for y in range(num)]
    
    return fake_widgets

# empty list to store our widget dataframes in    
dfs_list = []

# now lets make some widget data for each worker
# iterate through the worker dataframe
for index, row in worker_df.iterrows():
    
    # not all workers work at the same rate - or the same number of hours
    # randomly select a number of widgets for them to create based on 'worker status'
    if row['Worker Status'] == 'Full Time':
        num_widgets = random.randrange(500, 1000)
    elif row['Worker Status'] == 'Part Time':
        num_widgets = random.randrange(100, 500)
    else:
        num_widgets = random.randrange(1, 1000)
    
    # make widgets for each worker
    tmp_widgets = pd.DataFrame(make_widget_data(num=num_widgets))
    
    # add worker id so we know who made the widget
    tmp_widgets['Worker ID'] = row['Worker ID']
    
    # make sure item number is unique by appending worker id
    tmp_widgets['Item Number'] = tmp_widgets['Item Number'].astype('str')+ '-' + tmp_widgets['Worker ID'].astype('str')
    
    # append to df list
    dfs_list.append(tmp_widgets)
    
# concatenate all the dfs 
widget_df = pd.concat(dfs_list)
print(widget_df.shape)
widget_df.head()

import random, csv
from datetime import timedelta, datetime
from faker import Faker
from faker.providers import person
from faker.providers import internet
from faker.providers import ssn
from faker.providers import address
from faker.providers import job
from faker.providers import date_time

fake = Faker()
fake.add_provider(person)
fake.add_provider(internet)
fake.add_provider(ssn)
fake.add_provider(address)
fake.add_provider(job)
fake.add_provider(date_time)

def first_name_and_gender():
    g = 'M' if random.randint(0,1) == 0 else 'F'
    n = fake.first_name_male() if g=='M' else fake.first_name_female()
    return {'gender':g,'first_name':n}

def birth_and_start_date():
    sd = fake.date_between(start_date="-20y", end_date="now")
    delta = timedelta(days=365*random.randint(18,40))
    bd = sd-delta

    return {'birth_date':bd.strftime('%m/%d/%Y'), 'start_date': sd.strftime('%m/%d/%Y')}

def birth_and_start_date_on_windows():
    bd = datetime(1960, 1, 1) + timedelta(seconds=random.randint(0,1261600000)) #40 year time delta
    earliest_start_date = bd + timedelta(seconds=random.randint(0,567720000)) #earliest start date is 18 years after birth
    latest_start_date = datetime.now()

    delta = latest_start_date-earliest_start_date
    delta_in_seconds = delta.days*24*60*60+delta.seconds
    random_second = random.randint(0,delta_in_seconds)
    return {'birth_date':bd.strftime('%m/%d/%Y'), 'start_date': (bd+timedelta(seconds=random_second)).strftime('%m/%d/%Y')}

def title_office_org():
    #generate a map of real office to fake office
    offices = ['New York','Austin','Seattle','Chicago']
    #codify the hierarchical structure
    allowed_orgs_per_office = {'New York':['Sales'],'Austin':['Devops','Platform','Product','Internal Tools'],'Chicago':['Devops'], 'Seattle':['Internal Tools','Product']}
    allowed_titles_per_org = {
        'Devops':['Engineer','Senior Engineer','Manager'],
        'Sales':['Associate'],
        'Platform':['Engineer'],
        'Product':['Manager','VP'],
        'Internal Tools':['Engineer','Senior Engineer','VP','Manager']
    }

    office = random.choice(offices)
    org = random.choice(allowed_orgs_per_office[office])
    title = random.choice(allowed_titles_per_org[org])
    return {'office':office, 'title':title,'org': org}

def salary_and_bonus():
    salary = round(random.randint(90000,120000)/1000)*1000
    bonus_ratio = random.uniform(0.15,0.2)
    bonus = round(salary*bonus_ratio/500)*500
    return {'salary':salary,'bonus':bonus}

def title_office_org_salary_bonus():
    position = title_office_org()
    title_and_salary_range = {'Engineer':[90,120],'Senior Engineer':[110,140],'Manager':[130,150],'Associate':[60,80],'VP':[150,250]}
    salary_range = title_and_salary_range[position['title']]

    salary = round(random.randint(1000*salary_range[0],1000*salary_range[1])/1000)*1000
    bonus_ratio = random.uniform(0.15,0.2)
    bonus = round(salary*bonus_ratio/500)*500
    position.update({'salary':salary,'bonus':bonus})
    return position

d = dict()
d['first_name_and_gender'] = first_name_and_gender
d['last_name'] = lambda: {'last_name':fake.last_name()}
d['personal_email'] = lambda: {'email':fake.email()}
d['ssn'] = lambda: {'ssn':fake.ssn()}
d['birth_and_start_date'] = birth_and_start_date
d['title_office_org_salary_bonus'] = title_office_org_salary_bonus
d['accrued_holidays'] = lambda: {'accrued_holiday':random.randint(0,20)}

numRows = 100
data=[]
#data = pd.DataFrame([])
for _ in range(numRows):
    deep_list = [list(d[k]().values()) for k in d.keys()]
   # data.keys(deep_list)
   # data.append(deep_list)
    #row = [item for sublist in deep_list for item in sublist]
    data.append(row)
   # print(deep_list)
columns = list(d.keys())
df = pd.DataFrame(data)
df
#columns
#d.keys()
#df.head()
#list(df.columns.values)
#df = df.append(data, True)

import random
from datetime import timedelta, datetime
from faker import Faker
from faker.providers import person
from faker.providers import internet
from faker.providers import ssn
from faker.providers import address
from faker.providers import job
from faker.providers import date_time

fake = Faker()
fake.add_provider(person)
fake.add_provider(internet)
fake.add_provider(ssn)
fake.add_provider(address)
fake.add_provider(job)
fake.add_provider(date_time)
numRows = 10

d = dict()
d['first_name'] = lambda: fake.first_name()
d['last_name'] = lambda: fake.last_name()
d['gender'] = lambda: 'M' if random.randint(0,1) == 0 else 'F'
d['personal_email'] = lambda: fake.email()
d['ssn'] = lambda: fake.ssn()
#Note that on windows you cannot currently use the date_time functionality in Faker due to a known bug.  Comment out the following two lines and uncomment the two lines below that.
#d['birth_date'] = lambda: fake.date_between_dates(date_start=datetime(1960, 1, 1), date_end=datetime(2000, 1, 1))
#d['start_date'] = lambda: fake.date_between_dates(date_start=datetime(1995, 1, 1), date_end=datetime(2019, 1, 1))
d['birth_date'] = lambda: (datetime(1960, 1, 1) + timedelta(seconds=1261600000)).strftime('%m/%d/%Y')
d['start_date'] = lambda: (datetime(1995, 1, 1) + timedelta(seconds=725420000)).strftime('%m/%d/%Y')
d['office'] = lambda: fake.city()
d['title'] = lambda: fake.job()
d['org'] = lambda: random.choice(['Engineer','Sales','Associate','Manager','VP'])
d['accrued_holidays'] = lambda: random.randint(0,20)
d['salary'] = lambda: round(random.randint(90000,120000)/1000)*1000
d['bonus'] = lambda: round(random.randint(0,5000)/500)*500

for _ in range(numRows):
    print([d[k]() for k in d.keys()])

