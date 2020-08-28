students= {
    'PYTHON20201':0,
    'PYTHON20202':0,
    'PYTHON20203':0,
    'PYTHON20204':0,
    'PYTHON20205':0,
    'PYTHON20206':0,
    'PYTHON20207':0,
    'PYTHON20208':0,
    'ADMIN2020':0
}
candidates= {
    'MARYAM':0,
    'VICTOR':0
}
maryam= candidates['MARYAM']
victor= candidates['VICTOR']
election_time = 'open'
while election_time == 'open':
    voter_number= input('enter your election number')
    if voter_number in students:
        if students[voter_number]==0:
            vote= input(f'''
            CHOOSE A CANDIDATE
            M for MARYAM
            V for VICTOR
            ''')
            if vote=='M':
                print('vote was casted')
                maryam+= 1
                students[voter_number]=1
            elif vote=='V':
                print('vote was casted')
                victor+= 1
                students[voter_number]=1
            elif vote=='CLOSEELECTION':
                print(f'''
                Maryam {maryam} votes
                Victor {victor} votes
                ''')
                if maryam > victor:
                    print('maryam won the election')
                elif maryam==victor:
                    print('No one won')
                else:
                    print('Victor won the election')
            else:
                print('vote wasn\'t casted')
        else:
            print('you have voted')
    else:
        print('wrong Voter\'s number')
