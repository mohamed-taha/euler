import calendar
def calendar_solution():
    sundays = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            month_calendar = calendar.monthcalendar(year, month)
            if month_calendar[0][calendar.SUNDAY] == 1:
                sundays += 1
    return sundays

print calendar_solution()
