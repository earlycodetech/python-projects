print('Welcome to the IQ test game\nBegin by telling me about yourself\n')
name = input('What is your name?\n')
age = int(input('What is your age?\n'))

results = []

print('Answer the following questions. Simply type a,b,c or d to select your answer')

qst = input('If you save N500 monthly, how much will you have in 6 months?\na. N1,000\nb. N2,000\nc. N3,000\nd. N4,000')
if qst.lower()=='c':
  print('Correct answer!')
  results.append(20)
else:
  print('Incorrect answer!')
  results.append(0)
qst = input('When you join 2 squares, it becomes a ?\na. Sqaure\nb. Rectangle\nc. Trapezium\nd. Rhombus')
if qst.lower()=='b':
  print('Correct answer!')
  results.append(20)
else:
  print('Incorrect answer!')
  results.append(0)
qst = input('The retina is to the eye, as a _____ is to camera?\na. Film\nb. Shutter\nc. Zoom\nd. Pixels')
if qst.lower()=='a':
  print('Correct answer!')
  results.append(20)
else:
  print('Incorrect answer!')
  results.append(0)
qst = input('So, what does ATM mean?\na. Automatic Teller Machine\nb. Automatic Transfer Machine\nc. Automatic Technical Machine\nd. Automatic Telegram Machine')
if qst.lower()=='a':
  print('Correct answer!')
  results.append(20)
else:
  print('Incorrect answer!')
  results.append(0)
qst = input('What would be your preference to quench a fire if you have all of the following: insecticide,sand,wine,perfume?\na. insecticide\nb. sand\nc. wine\nd. perfume')
if qst.lower()=='b':
  print('Correct answer!')
  results.append(20)
else:
  print('Incorrect answer!')
  results.append(0)

cumm_result = sum(results)
iq = (cumm_result/age)*100
print(f"""
Hey {name},your IQ is {iq}
""")
