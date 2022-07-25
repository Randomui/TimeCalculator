def add_time(start,add,day=None):
  time, period = start.split() 
  hour, minutes = map(int,time.split(':')) # converting everything to int 
  addH, addM = map(int,add.split(':'))
  midday = ('PM','AM') 
  new_day = '' 
  later = ''
  
  carry, minutes = divmod(minutes + addM,60) # 'carry' is 1 (minutes >= 60) or 0 (minutes <= 59)
  hour += carry 
  cycles, hour = divmod(hour + addH,12) # 'cycles' is # of 12-hours (half days) that 'hour' exceeds 
  
 
  period = abs(midday.index(period)-(cycles % 2)) # period is an index in midday
  passed = (period + cycles) // 2  # 'passed' describes the number of days passed 
  
  if hour == 0: # basically an edge case created from my modulus calculations
    hour = 12

  if minutes < 10: # standardizing time format, 12:1 -> 12:01
    minutes = f'0{minutes}'

  
  if day:
      week = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
      new_day = f', {week[(week.index(day.capitalize()) + passed) % 7]}' 
  
 
  if passed == 1:
      later = ' (next day)'
  elif passed != 0:
      later = f' ({passed} days later)'
      
  return f'{hour}:{minutes} {midday[period]}{new_day}{later}'
