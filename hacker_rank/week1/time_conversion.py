#!/bin/python3
import datetime
import os

"""
    excercise:
        Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
        Note: 
        - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
        - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
    arg:
        - time in 12-hour AM/PM format
    output:
        - return a new string representing the input time in 24 hour format.
    steps:
        - get time in a in 12-hour AM/PM format
        If i can use datetime to extract time 
        - use datetime to convert str in real time
        - return the converted time in 24h
        else
        - extract time in hh,mm,ss
        - control case if 12AM or 12PM
        - convert time in 24h time
    notes:
        - 12:00:00AM diventa 00:00:00
        - 12:00:00PM rimane 12:00:00
    question:
        - can I use datetime to extract singole var ?
"""

def timeConversion(s):
    time_obj = datetime.datetime.strptime(s, "%I:%M:%S%p")
    return time_obj.time()


if __name__ == '__main__':
    s = input().strip()
    result = timeConversion(s)
    print(str(result))
