data= {
    'PYTHON20201':'ALFRED',
    'PYTHON20202':'VICTOR',
    'PYTHON20203':'ELIJAH',
    'PYTHON20204':'DAVID E',
    'PYTHON20205':'DAVID P',
    'PYTHON20206':'MARYAM',
}
candidates= {
     'MARYAM':'cand1',
   'DAVID E' :'cand2',
}
election_time= ['open','closed']
while election_time== 'open':
    start= input('enter matric number ')
    if start in data:
        print('welcome')
        start1= input('select cand1 or cand2 ')
        if start1 in candidates:
            print('voted')
        else:
            print('invalid candidate ')

    else:
        print('please you are not allowed')
