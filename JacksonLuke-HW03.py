# Luke Jackson
# UWYO COSC 1010
# Submission Date 11/5/24
# HW 03
# Lab Section:14
# Sources, people worked with, help given to:
# your
# comments
# here




def determine_leap(MM, DD, YYYY):
    if YYYY % 4 == 0 and YYYY % 100 != 0:
        Months_dict["Febuary"] = 29
        Total_days == 366
        leap = True

    elif YYYY % 4 == 0 and YYYY % 400 == 0:
        Months_dict["Febuary"] = 29
        Total_days == 366
        leap = True

    if MM == 2 and DD == 29 and leap != True:
        Error = True
        return Error
    
def determine_t_days(MM, DD):
    month_determ = MM - 1
    mono = month_determ
    in_range = list(Months_dict.keys())[ : mono]
    if month_determ > 0 and mono > 0:
        for key in Months_dict.keys():
            mon = sum(Months_dict[key] for key in in_range)
    elif mono == 0:
        mon = Months_dict["January"]
    elif month_determ == 0:
        mon = 0
    total_days = mon + DD
    return total_days

def determine_DweekD(D, YY, M):
    y = YY -1
    day = (36 + y +(y/4) - (y/100) + (y/400))%7
    if M == 2:
        day = int(day)
        day = day -1
    else:
        day = round(day)
    day_counter = day
    total_day_counter = 0
    while True:
        day_counter += 1
        total_day_counter += 1
        # print("added")
        if day_counter == 7:
            day_counter = -1
        if total_day_counter == D:
            break
    day_of_week = Days_week[day_counter]
    return day_of_week

while True:
    Months_dict = {"January":31, "Febuary":28, "March":31, "April":30, "May":31, "June":30, "July":31, "August":31, "September":30, "October":31, "November":30, "December":31}
    Days_week = ["Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    DG_list = []
    DG_list1 = []
    Total_days = 365
    

    date_given = input("Type exit to stop\n Give a date in MM/DD/YYYY: ")
    if date_given.lower() == "exit":
        break
    DG_list1 = date_given.split("/")
    while len(DG_list) != 3:
        DG_list.append(int(DG_list1[0]))
        del DG_list1[0]
    if DG_list[0] > 12 or DG_list[0] <= 0:
        print(f"{date_given} Invalid Date")
        continue
    if DG_list[1] > 31 or DG_list[1] <= 0:
        print(f"{date_given} Invalid Date")
        continue

    
    determine_leap(DG_list[0], DG_list[1], DG_list[2])
    if determine_leap == True:
        print(f"{date_given} Invalid Date")
        continue

    determine_t_days(DG_list[0], DG_list[1])
    determine_DweekD(determine_t_days(DG_list[0], DG_list[1]), DG_list[2], DG_list[0])
    print(f"{date_given} {determine_DweekD(determine_t_days(DG_list[0], DG_list[1]), DG_list[2], DG_list[0])}")
    continue


