import math

January = 1
February = 2
March = 3
April = 4
May = 5
June = 6
July = 7
August = 8
September = 9
October = 10
November = 11
December = 12

Tishrei = 1
Cheshvan = 2
Kislev = 3
Tevet = 4
Shevat = 5
Adar = 6
Nissan = 7
Iyyar = 8
Sivan = 9
Tamuz = 10
Av = 11
Elul = 12
Adar2 = 6.5

def leapYear(year):
  if int((235*year-234)%19) >11:
    return 13
  return 12

def leapYear2(year):
  if int((235*year-234)%19) >11:
    return True
  return False


def months_num(month, year_type):
  if month in [Tishrei, Shevat, Nissan, Sivan, Av]:
    return 30
  elif month == Cheshvan:
    return cheshvan1(year_type)
  elif month == Kislev:
    return kislev1(year_type)
  else:
    return 29

def gregLeap(year):
  if year % 400 == 0:
    return 366   
  if year % 100 == 0:
      return 365  
  if year % 4 == 0:
      return 366  
  return 365

def greg_months(year, month):
  if month in [January, March, May, July, August, October, December]:
    return 31
  elif month == February: 
    if gregLeap(year):
      return 29
    return 28
  else:
    return 30

def greg_months_num(month):
  if month in [January, March, May, July, August, October, December]:
    return 31
  elif month == February: 
    return 28
  else:
    return 30

def kislev1(year_type):
  if year_type == "shalem" or year_type == "kesidrah":
    return 30
  else:
    return 29

def cheshvan1(year_type):
  if year_type == "shalem":
    return 30
  else:
    return 29
 
 
 # this calculates the type of year using the four gates 
def yearLength(year):
  YearCycle = int(year/19)
  Year_rem = int(year % 19)
  num_months = YearCycle * 235
  for i in range(1, Year_rem):
    num_months += leapYear(i)
  parts = num_months*(29*(24*1080)+12*1080+793)+1080*24+5*1080+204
  total_days = parts/(24*1080)
  total_weeks = int(parts/(24*1080*7))
  parts_into_week = math.trunc(parts-((total_weeks)*24*1080*7))
  hours_into = parts_into_week/1080
  hours_past_day = hours_into % 24
  day_in_week = int(hours_into / 24)  
  list1 = [1, 4, 9, 12, 15, 7, 18, 2, 5, 10, 13, 16]
  list2 = [3, 6, 8, 11, 14, 17, 0]   
  if 7*24*1080+16*1080 <= parts_into_week:
    year_type = "chaser"
  elif 6*24*1080+20*1080+491 <= parts_into_week:
    year_type = "shalem"
  elif 6*1080*24+1080*9+204 <= parts_into_week:
    if Year_rem in list1:
      year_type = "shalem"
    elif Year_rem in list2:
      year_type = "chaser"
  elif 6*24*1080+408 <= parts_into_week:
    if Year_rem in [1, 4, 9, 12, 15]:
      year_type = "shalem"
    elif Year_rem in [7, 18, 2, 5, 10, 13, 16] or Year_rem in list2:
      year_type = "chaser"
  elif 5*1080*24+1080*18 <= parts_into_week:
    year_type = "chaser"
  elif 5*1080*24+1080*9+204 <= parts_into_week:
    year_type = "shalem"
  elif 4*1080*24+11*24+695 <= parts_into_week:
    if Year_rem in list1:
      year_type = "kesidrah"
    elif Year_rem in list2:
      year_type = "shalem"
  elif 3*1080*24 + 18*1080 <= parts_into_week:
    if Year_rem in list1:
      year_type = "kesidrah"
    elif Year_rem in list2:
      year_type = "chaser"
  elif 3*1080*24+9*1080+204 <= parts_into_week:
    year_type = "kesidrah"
  elif 2*1080*24+18*1080 <= parts_into_week:
    year_type = "kesidrah"
  elif 2*1080*24+15*1080+589 <= parts_into_week:
    if Year_rem in [1, 4, 9, 12, 15, 7, 18]:
      year_type = "kesidrah"
    elif Year_rem in [2, 5, 10, 13, 16] or Year_rem in list2:
      year_type = "shalem"
  elif 1*24*1080+20*1080+491 <= parts_into_week:
    year_type = "shalem"
  elif 1*24*1080+9*1080+204 <= parts_into_week:
    if Year_rem in list1:
      year_type = "shalem"
    elif Year_rem in list2:
      year_type = "chaser"
  else:
    year_type = "shalem" 
    
  return year_type, hours_past_day, parts_into_week, day_in_week, total_days

  
def heb_to_num(M, D, Y):
  year = 1
  days = 0
  previous_days = 0
  year_type = ""
  while year < Y+1:
    
    year_type, hours_past_day, parts_into_week, day_in_week, total_days = yearLength(year)
    
    
    if year_type == "kesidrah" and parts_into_week > (2*24*1080+9*1080+204):
      total_days += 2
    elif leapYear(Y-1) == 366 and parts_into_week > (24*1080+15*1080+589) and parts_into_week < 24*1080*2:
      total_days +=1
    else:
      if hours_past_day >= 18:
        total_days += 1
        day_in_week += 1
        if day_in_week in [1, 4, 6]:
          total_days += 1
      elif day_in_week in [1, 4, 6]:
        total_days += 1
    
    days += (total_days - previous_days)
    previous_days = total_days
    year += 1
  for i in range(1, M):
      days += months_num(i, year_type)
  if leapYear(Y) == 13:
    if M == 7:
      days += 1
    elif M > 7:
      days += 30
  days += D
  return days



def num_to_heb(days):
  days_off = days
  parts = days*(1080*24)-1080*24+5*1080+204
  num_months = int(parts/(29*(24*1080)+12*1080+793))
  
  parts_left = math.trunc(parts - num_months*(29*(24*1080)+12*1080+793))
  num_cycles = int(num_months/235)
  num_remains = num_months - (235*num_cycles)
  num_years_cycles = 19*num_cycles
  num_months_full_year = num_cycles * 235
  
  year = 1
  while num_remains > 13:
    num_remains -= leapYear(year)
    num_months_full_year += leapYear(year)
    year += 1
  
  if leapYear2(year) == False and num_remains == 13:
    num_remains -= 12
    num_months_full_year += 12
    year += 1
  
  Year = year + num_years_cycles  
  days_off -= ((num_months_full_year*(29*(24*1080)+12*1080+793)))/(1080*24)
  year_type, hours_past_day, parts_into_week, day_in_week, total_days = yearLength(Year)
  if leapYear2(Year):
    for i in range(1, num_remains+1):
      if i == 6:
        days_off -= 30
      if i == 7:
        days_off -= 29
      elif i > 7:
        days_off -= months_num(i-1, year_type)
      else:
        days_off -= months_num(i, year_type)
  else: 
    for i in range(1, num_remains+1):
      days_off -= months_num(i, year_type)
  Month = num_remains+1
  Day = days_off
  return Month, int(Day), Year


def num_to_eng(days):
  if days >= heb_to_num(4, 17, 3761):
    days -= heb_to_num(4, 17, 3761)
    Year = 1
    while days > 365:
      days -= gregLeap(Year)
      Year += 1
    Month = 1
    if gregLeap(Year) == 366:
      while (days > 31 and Month in [January, March, May, July, August, October, December]) or (days > 29 and Month == 2) or (days > 30 and Month in [February, April, June, September, November]):
        days -= greg_months(Year, Month)
        Month += 1
    else:
      while (days > 31 and Month in [January, March, May, July, August, October, December]) or (days > 28 and Month == 2) or (days > 30 and Month in [February, April, June, September, November]):
        days -= greg_months(Year, Month)
        Month += 1
    Day = days
  else:
    days -= heb_to_num(4, 17, 3761)
    Year = 1
    print(days)
    while days < -365:
      days += gregLeap(-Year)
      Year += 1  
    Year = -Year
    Month = 12
    if gregLeap(Year) == 366:
      while (days < -32 and Month in [January, March, May, July, August, October, December]) or (days < -30 and Month == February) or (days < -31 and Month in [February, April, June, September, November]):
        days += greg_months(Year, Month)
        print(days)
        Month -= 1   
    else:
      while (days < -32 and Month in [January, March, May, July, August, October, December]) or (days < -29 and Month == February) or (days < -31 and Month in [February, April, June, September, November]):
        days += greg_months(Year, Month)
        print(days)
        Month -= 1
        Day = greg_months(Year, Month)+days    
  return Month, int(Day)+1, Year    
      

def eng_to_num(M, D, Y):
  if Y > 0:
    daysTot = heb_to_num(4, 17, 3761)
    year = 1
    while year < Y:
      daysTot += gregLeap(year)
      year +=1
    for i in range(1, M):
      daysTot += greg_months(Y, i)
    daysTot += D
    
  else:
    start = heb_to_num(4, 17, 3761)
    daysTot = ((Y))*365.2425
    daysTot += start
    for i in range(M-1):
      daysTot += greg_months(-Y, i)
    daysTot += (D)
  return daysTot-1


def eng_to_heb(M,D,Y):
  num = eng_to_num(M, D, Y)
  return num_to_heb(num)

def heb_to_eng(M, D, Y):
  num = heb_to_num(M, D, Y)
  return num_to_eng(num)



# print(eng_to_heb(7, 2, 2020))
# print(heb_to_eng(Tamuz, 10, 5780))
# print(eng_to_num(1, 1, 2000))
# print(eng_to_num(2, 15, 2000))
