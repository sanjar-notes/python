
for countrypair in pytz.country_names.items():
    print(countrypair[0], ':\b')  # printed the country

    # check if country has a time zone
    if countrypair[0] not in pytz.country_timezones:
        continue
    for ctz in pytz.country_timezones[countrypair[1]]:
        # print the timezone and the local time
        print(ctz, datetime.