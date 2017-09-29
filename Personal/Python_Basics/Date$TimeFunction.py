##Date and Time Functions

#Time Method
import time
#returns time span of current time, time span is time lapsed in seconds between january 1st 1970 12 am and current time
print time.time()   #1504630416.88   #first time is module and second time is function
# 1504630416.88 this number is useful, you can pull out no of years , hours , days etc
print time.localtime(time.time())   #time.struct_time(tm_year=2017, tm_mon=9, tm_mday=5, tm_hour=11, tm_min=57, tm_sec=6, tm_wday=1, tm_yday=248, tm_isdst=1)
#monday has index 0

#ASCTIME function
print time.asctime()    #Tue Sep 05 11:59:14 2017

#MAKE TIME function
# used to find time span for some day which is passed or of the day which is going to happen latter
mytuple={1993,4,6,15,23,15,0,0,0}   #year1993,april,day6,15:23:15pm, 0 for don;t know which day of the week
#print mytuple
#print time.mktime(mytuple)  #should return 734089995.0
#???having issues
#print time.localtime(time.mktime(mytuple))

#SLEEP Function
#delays excutuin of the calling function or the script by a given number of seconds
time.sleep(7)
print "Hello world!"    #Hello World get displayed after 7 seconds

#Month Method
#requires calander module
import calendar
#takes two arguments, 1st year value and 2nd month value
print calendar.month(1965,3)
""""     March 1965
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
"""
#to see calender of the entire year
print calendar.calendar(1994,2,1,10)    #2 is max width for each date, 1 as each week occupy max one line,10 as charcter space between each coloumn
""""
                                      1994

      January                       February                       March
Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su
                1  2              1  2  3  4  5  6              1  2  3  4  5  6
 3  4  5  6  7  8  9           7  8  9 10 11 12 13           7  8  9 10 11 12 13
10 11 12 13 14 15 16          14 15 16 17 18 19 20          14 15 16 17 18 19 20
17 18 19 20 21 22 23          21 22 23 24 25 26 27          21 22 23 24 25 26 27
24 25 26 27 28 29 30          28                            28 29 30 31
31

       April                          May                           June
Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su
             1  2  3                             1                 1  2  3  4  5
 4  5  6  7  8  9 10           2  3  4  5  6  7  8           6  7  8  9 10 11 12
11 12 13 14 15 16 17           9 10 11 12 13 14 15          13 14 15 16 17 18 19
18 19 20 21 22 23 24          16 17 18 19 20 21 22          20 21 22 23 24 25 26
25 26 27 28 29 30             23 24 25 26 27 28 29          27 28 29 30
                              30 31

        July                         August                      September
Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su
             1  2  3           1  2  3  4  5  6  7                    1  2  3  4
 4  5  6  7  8  9 10           8  9 10 11 12 13 14           5  6  7  8  9 10 11
11 12 13 14 15 16 17          15 16 17 18 19 20 21          12 13 14 15 16 17 18
18 19 20 21 22 23 24          22 23 24 25 26 27 28          19 20 21 22 23 24 25
25 26 27 28 29 30 31          29 30 31                      26 27 28 29 30

      October                       November                      December
Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su
                1  2              1  2  3  4  5  6                    1  2  3  4
 3  4  5  6  7  8  9           7  8  9 10 11 12 13           5  6  7  8  9 10 11
10 11 12 13 14 15 16          14 15 16 17 18 19 20          12 13 14 15 16 17 18
17 18 19 20 21 22 23          21 22 23 24 25 26 27          19 20 21 22 23 24 25
24 25 26 27 28 29 30          28 29 30                      26 27 28 29 30 31
31
"""

#isleap method
#tell you if given year is a leap year or not
print calendar.isleap(2008)     #True
print calendar.isleap(2009)     #false


