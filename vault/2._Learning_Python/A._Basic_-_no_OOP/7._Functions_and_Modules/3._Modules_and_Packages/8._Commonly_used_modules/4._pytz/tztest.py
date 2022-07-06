import pytz # for localization
import datetime # for getting the date and time
# get the current local time for a place
# tz_display = pytz.timezone('Europe/Moscow')
# print(type(tz_display))

# local_time = datetime.datetime.now(tz=tz_display)
# print(local_time)

# #1 timezones, fully independent
# for i in pytz.all_timezones:
#     print(i)

# #2 country_names: codes and full names(country names)
# for i in pytz.country_names.items():
#     print(i[0],':', i[1])


# #3 print timezone and country name, using both country_names and timezones
# for country in pytz.country_names.items():
#     # country names
#     print(country[1],':')

#     # check if a timezone exists in the country
#     if country[0] in pytz.country_timezones:
#         # print the zones
#         if len(pytz.country_timezones[country[0]])>1:
#             for zone in enumerate(pytz.country_timezones(country[0])):
#                 print('\t {:>2}. {}'.format(zone[0]+1, zone[1]))
#         else:
#             print(pytz.country_timezones(country[0])[0])
#     else:
#         print('No time zones $$$')
