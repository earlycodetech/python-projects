location = {
    #values are users
    'nigeria':{'lagos':10000000,'abuja':5000000,'rivers':6000000,'kano':9800000,'anambra':4600000,
    'edo':3200000,'oyo':1600900,'calabar':1200700,'ogun':2100500,'enugu':1300700},
    
    'united states':{'florida':11000000,'new york':5100000,'california':6100000,'maryland':9900000,
    'ohio':4700000,'iowa':3300000,'north carolina':1700900,'ilinois':1300700,'pensylvannia':2200500,
    'masachussete':1400700}
}

interest = {
    #values are in percentages
    'education':15,'technology':20,'fashion':25,'sports':25,'music':15
}
demography = {
    #values are in percentages
    'gender':{'male':55,'female':44.5,'unspecified':0.5},
    'age':{'18-24':35,'25-34':25,'35-44':18,'45-54':12,'55-64':8,'65+':2}
}

print('WELCOME TO FB AD MANAGER')
purpose = input('''
What do you aim to achieve?

Choose any of the following:
Traffic
Conversion
Awareness
Engagement
''')

budget = float(input('What is you budget: '))

country =  input('Select target country: ')
if country.lower()=='nigeria':
    keys = [] #an empty list to be populated with keys
    state = '' 
    
    while state != 'null':
        state = input('''
        Select state:
        Lagos
        Abuja
        Rivers
        Kano
        Anambra
        Edo
        Oyo
        Calabar
        Ogun
        Enugu
        ''')
        keys.append(state.lower())
elif country.lower()=='united states':
    keys = []
    state = ''
    
    while state != 'null':
        state = input('''
        Select state:
        Florida
        New York
        California
        Maryland
        Ohio
        Iowa
        North Carolina
        Ilinois
        Pensylvannia
        Masachussete
        ''')
        keys.append(state.lower())
else:
    print('Unsupported coverage')

#-------------------------------------
#location audience summary
country_level = location[country]
audience_loc = 0
keys.pop() #removes the last null value that was entered
for i in keys:
    audience_loc = audience_loc + country_level[i]
#-------------------------------------

#-------------------------------------
#audience based on location and budget
reach = budget/4
max_spend = audience_loc*4
print(f'''
Available audience: {audience_loc}
Reach (based on budget): {reach}
Maximum spend: {max_spend}
''')
