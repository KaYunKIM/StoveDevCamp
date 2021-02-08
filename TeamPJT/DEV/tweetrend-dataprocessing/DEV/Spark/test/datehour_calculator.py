import time, datetime

current = 2010936
cur = datetime.datetime.now()


datehour = str(current)
collected_at = datetime.datetime(2021,int(datehour[:-6]),int(datehour[-6:-4]),int(datehour[-4:-2]),int(datehour[-2:]))
# print(type(collected_at), collected_at)

for i in range(100):
    one_minute_later = collected_at + datetime.timedelta(minutes=1)
    collected_at = one_minute_later
    print(one_minute_later)



# for i in range(5):
    # now = int(datetime.datetime.now().strftime("%M"))
    # print('now', now)
    # while True:
    #     nxt = int(datetime.datetime.now().strftime("%M"))
    #     if nxt > now: 
    #         break
    #     print('next', nxt, now)

    # print('next after', nxt, now)
    # datehour = int((datetime.datetime.now() - datetime.timedelta(hours=9, minutes=1)).strftime("%m%d%H%M"))
    # print('datehour', datehour)


# current = 2010936
# cur = datetime.datetime.now()

# print(type(cur), cur)

# datehour = str(current)
# new_date = datetime.datetime(2021,int(datehour[:-6]),int(datehour[-6:-4]),int(datehour[-4:-2]),int(datehour[-2:]))
# print(type(collected_at), collected_at)
# collected_at = datetime.datetime.now() - datetime.timedelta(hours=9, minutes=1)

datehour = 0
while int(datehour) < 2061907:
    now = datetime.datetime.now()
    search = str(now - datetime.timedelta(minutes=1))
    datehour = search[6:7]+search[8:10]+search[11:13]+search[14:16]
    try:
    #     casandra(datehour) -> mongo DB
        print(now, datehour)
    except:
        pass
    time.sleep(5)


# for i in range(5):
#     collected_at += datetime.timedelta(minutes=1)
#     datehour_time = str(collected_at + datetime.timedelta(hours=9))
#     print(collected_at)
#     print(datehour_time[6:7]+datehour_time[8:10]+datehour_time[11:13]+datehour_time[14:16])
#     print()