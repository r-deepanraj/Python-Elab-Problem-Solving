# day=int(input())
# hour=int(input())
# min=int(input())
# sec=int(input())
# seconds=3600
# minutes=int(seconds)/(60*min)
# hour_to_sec=(((day*24)+(hour))*(seconds))
# # min_to_sec=(minutes*min)
# # div=int(seconds/min_to_sec)
# print((hour_to_sec+minutes)+(sec))

day=int(input())
hour=int(input())
min=int(input())
sec=int(input())
day_sum=day*24
total=(day_sum*3600)+(hour*3600)+(min*60)+(sec)
print(total)