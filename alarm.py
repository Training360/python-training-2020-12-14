actual_time = int(input("Hány óra van?"))
print(actual_time)
req_alarm_time = int(input("Hány óra múlva szólaljon meg az ébresztő?"))
print(req_alarm_time)

req_alarm_time = (actual_time + req_alarm_time) % 24
print("Hour: " + str(req_alarm_time))
