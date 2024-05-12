import math
import datetime

"""
孩子不懂事写的玩的
计算下旅途的行程 11/5/2024
"""
def calculate_rent():
    curDate = datetime.date.today()
    travelDate = datetime.date(2024,6,5)
    cycle = 14
    gradDate = datetime.date(2024,7,1)
    daysNow = gradDate - curDate
    daysFuture = gradDate - travelDate
    rentsNow = daysNow.days / cycle * 460
    rentsTravel = daysFuture.days / cycle * 460
    print(rentsNow, rentsTravel)


if __name__ == "__main__":
    calculate_rent()
