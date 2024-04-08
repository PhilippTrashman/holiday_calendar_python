import calendar
import json

def show_holiday_calendar(filepath: str, year_number: int):
    cal = calendar.Calendar()
    years = cal.yeardays2calendar(year_number, width=12)
    month_list = ["January", "February", "March", "April", "May", "Juni", "Juli", "August", "September", "October", "November", "December"]
    month_index = 0

    with open(filepath, 'r') as f:
        d = json.load(f)['feiertage']
        holidays = {}
        for item in d:
            holidays[item["Datum"].replace(".", "-")] = item["Feiertag"]
        f.close()

    for year in years:
        year_str = ""
        for month in year:
            month_str = month_list[month_index] + "\n"
            month_str += "Mo Tu We Th Fr Sa Su \n"
            for week in month:
                holiday_present = False
                week_list = []
                week_str = ""
                for day in week:
                    if day[0] == 0:
                        week_str += "   "
                    else:
                        week_str += f'{day[0]:2} '
                        week_list.append(f"{day[0]:02}-{month_index+1:02}-{year_number}")
                
                for date, holiday in holidays.items():
                    if date in week_list:
                        if holiday_present:
                            week_str += f', {holiday}'
                        else:
                            holiday_present = True
                            week_str += f' {holiday}'

                month_str += week_str + "\n"
            year_str += month_str + "\n"
            month_index += 1

    with open("holiday_calendar.txt", "w") as f:
        f.write(year_str)
        f.close()

                

if __name__ == "__main__":
    show_holiday_calendar("holidays.json", 2024)