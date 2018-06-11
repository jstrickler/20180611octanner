#!/usr/bin/env python

import os
import calendar
import webbrowser

tcal = calendar.TextCalendar()  # <1>
print(tcal.formatmonth(2012,1)) # <2>

print()

hcal = calendar.HTMLCalendar()   # <3>
formatted_month = hcal.formatmonth(2012,1)  # <4>

html_file_name = 'sample_calendar.html'

with open(html_file_name, 'w') as calendar_out:
    calendar_out.write(formatted_month)
    webbrowser.open("file://" + os.path.realpath(html_file_name))

