one_minute = 60
one_hour = 3600
one_day = 86400
one_week = 604800
duration = int(input("Введите продолжительность в секундах: "))
print("продолжительность = ", duration)
if duration < one_minute:
    print (duration, "сек")
elif duration >= one_minute and duration < one_hour:
    minute = duration // one_minute
    second = duration % one_minute
    print("продолжительность = ", minute, "минут", second, "секунд")
elif duration >= one_hour and duration < one_day:
    hour = duration // one_hour
    duration = duration % one_hour
    minute = duration // one_minute
    second = duration % one_minute
    print("продолжительность = ", hour, "час" ,minute, "минут", second, "секунд")
elif duration >= one_day and duration < one_week:
    day = duration // one_day
    duration = duration % one_day
    hour = duration // one_hour
    duration = duration % one_hour
    minute = duration // one_minute
    second = duration % one_minute
    print("продолжительность = ", day,"дн" , hour, "час", minute, "минут", second, "секунд")





