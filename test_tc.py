def add_time(start, duration):

  start_list = start.split()
  start_time = start_list[0].split(":")
  #print("This is the start_time split: ", start_time)
  start_hour = start_time[0]
  start_minutes = start_time[1]
  
  
  duration_list = duration.split(":")
  
  duration_hour = duration_list[0]
  duration_minutes = duration_list[1]

  hour_add = int(start_hour) + int(duration_hour)
  minutes_add = int(start_minutes) + int(duration_minutes)

  

  #print(f"start hour: {start_hour} + start duration: {duration_hour} = {hour_add} \n start minutes: {start_minutes} + duration minutes: {duration_minutes} = {minutes_add}")

  
  
  #print(start_list, duration_list)
  #print (start, start_time, start_hour, start_minutes)
  #print (duration, duration_list)
  
  '''
  for i in start:
    start_list = start.split()
    print (start_list)

  for i in duration:
    duration_list = duration.split()
    print (duration_list)
  '''
  

    #return new_time