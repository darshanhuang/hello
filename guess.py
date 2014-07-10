
number=23
ink=raw_input('Enter:')
if ink=='':
    print 'invalid input'
else:
    guess=int(ink)
    if number==guess:
        print 'right!'

    elif guess=='':
        print 'invalid input'
    elif number<guess:
        print 'low'
    else:
        print 'high'

print 'Done'
