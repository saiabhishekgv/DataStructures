from datetime import date,datetime
import calendar

def meetup_day(year, month, day_of_the_week, which):
    day_index = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5,'Sunday':6}
    week_index = {'1st': 0, '2nd': 1, '3rd': 2, '4th': 3, '5th': 4, "last": 5}
    cal = calendar.monthcalendar(year=year,month=month)

    # Uncomment below section to print month calender
    '''
    print 'calender for month {0}, year {1} is : '.format(month, year)
    for i in cal :
        for j in i :
            if j == 0:
                print '    ',
            elif j<10:
                print j,'  ',
            else :
                print j,' ',
        print ''
    
    '''


    day = day_index[day_of_the_week]
    days = [w[day] for w in cal if w[day] > 0]
    if week_index[which]  != 5:
        d = days[week_index[which]]
        return date(year,month,d)

    else:
        for d in days:
            if d in range(13, 20):
                return date(year, month, d)
