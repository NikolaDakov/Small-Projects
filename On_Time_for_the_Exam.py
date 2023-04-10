hour_exam = int(input())
minute_exam = int(input())
hour_taker = int(input())
minute_taker = int(input())

exam_time_in_minutes = hour_exam * 60 + minute_exam
taker_time_in_minutes = hour_taker * 60 + minute_taker

time_diff = exam_time_in_minutes - taker_time_in_minutes

if time_diff > 30:
    print('Early')
elif time_diff < 0:
    print('Late')
else:
    print('On time')

hours = 0
minutes = abs(time_diff)
result = ''

if minutes >= 60:
    hours = minutes // 60
    minutes = minutes % 60

if hours > 0:
    result += f'{hours}:{minutes:02d} hours'
elif minutes > 0:
    result += f'{minutes} minutes'

if time_diff > 0:
    result += ' before the start'
elif time_diff < 0:
    result += ' after the start'

print(result)
