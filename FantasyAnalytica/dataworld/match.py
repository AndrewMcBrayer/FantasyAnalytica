from dataworld import league


cf_free = league.League(310279, 2016, 2015)
cf_free._sbData_get()
cf_free._sbData_parse_()
print(cf_free.sbData)

