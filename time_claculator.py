def add_time(start_time, duration, start_day=None):
    start_time_split = start_time.split()
    time, period = start_time_split[0], start_time_split[1]
    start_hours, start_minutes = map(int, time.split(':'))
    if period == "PM" and start_hours != 12:
        start_hours += 12

    
    duration_hours, duration_minutes = map(int, duration.split(':'))

    
    total_minutes = start_hours * 60 + start_minutes + duration_hours * 60 + duration_minutes


    days = total_minutes // (24 * 60)
    remaining_minutes = total_minutes % (24 * 60)

    
    result_hours = remaining_minutes // 60
    result_minutes = remaining_minutes % 60

    
    period = "AM" if result_hours < 12 else "PM"
    result_hours = result_hours % 12
    result_hours = result_hours if result_hours > 0 else 12

    
    result_time = f"{result_hours:02d}:{result_minutes:02d} {period}"

    
    if start_day:
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        start_day = start_day.capitalize()
        start_day_index = days_of_week.index(start_day)
        result_day_index = (start_day_index + days) % 7
        result_day = days_of_week[result_day_index]
        result_time += f", {result_day}"

    
    if days == 1:
        result_time += " (next day)"
    elif days > 1:
        result_time += f" ({days} days later)"

    return result_time


print(add_time("3:00 PM", "3:10")) 
print(add_time("11:30 AM", "2:32", "Monday"))  
print(add_time("11:43 AM", "00:20")) 
print(add_time("10:10 PM", "3:30"))  
print(add_time("11:43 PM", "24:20", "tueSday"))  
print(add_time("6:30 PM", "205:12"))  