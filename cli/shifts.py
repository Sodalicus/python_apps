#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 Paweł Krzemiński 
#
# Distributed under terms of the MIT license.

"""


"""
#from calendar import *

#cal = Calendar()

P = [0,3,3,3,3,3,0,\
    0,0,2,2,2,2,2,\
    0,0,1,1,1,1,1]

A = [0,0,'N','N',0,0,'D',\
     'D','D',0,0,'N','N',0,\
     0,0,'D','D',0,0,'N',\
     'N','N',0,0,'D','D',0]

MONTHS = [31,28,31,30,31,30,31,31,30,31,30,31]

p = []
a0 = []
for x in A:
    a0.append([x, ''])

a = []

while len(p) < 366:
    p += P
while len(a) < 366:
    a += a0


b = []
c = []
d = []
for x in a:
    if x[0] == 0:
        b.append(['N',''])
        c.append([0,''])
        d.append(['D',''])
    elif x[0] == 'N':
        b.append([0,''])
        c.append(['D',''])
        d.append([0,''])
    elif x[0] == 'D':
        b.append([0,''])
        c.append(['N',''])
        d.append([0,''])


def compare2(shift):
    results = [x for x in range(0, 366)]
    for day in range(0, 366):
        if day == 0:
            results[day] = [shift[day][0], "1st"]
            continue

        if p[day] == 0:
            results[day] = [shift[day][0], "OFF"]
            continue

        if p[day] == 1:
            if shift[day-1][0] == "N":
                results[day] = [shift[day][0], "1hR"]
                continue

        if shift[day][0] == 0:
            results[day] = [shift[day][0], "OFF"]
            continue

        elif shift[day][0] == "D":
            if p[day-1] == 3:
                results[day] = [shift[day][0], "1hR"]
                continue
            elif p[day] == 3:
                results[day] = [shift[day][0], "OFF"]
                continue
            elif p[day] == 2:
                results[day] = [shift[day][0], "5hP"]
                continue
            elif p[day] == 1:
                results[day] = [shift[day][0], "9hR"]
                continue

        elif shift[day][0] == "N":
            if p[day] == 3:
                results[day] = [shift[day][0], "9hN"]
                continue
            elif p[day] == 2:
                results[day] = [shift[day][0], "5hW"]
                continue
            elif p[day] == 1:
                results[day] = [shift[day][0], "OFF"]
                continue
        print(p[day], shift[day][0])
        results[day] = [shift[day][0], 44]

    return results


results_a = compare2(a)
results_b = compare2(b)
results_c = compare2(c)
results_d = compare2(d)


def show_month(shift, start, end):
    print()
    i = 1
    if type(shift[0]) == type([]):
        for day in range(start, end):
            print("{:>3}|".format(shift[day][0]), end='')
        print()
        #for day in range(start, end):
        #    print(i, day, shift[day], end='')
        #    i+=1
        #print()
    else:
        for day in range(start, end):
            print("{:>3}|".format(shift[day]), end='')
        print()

def show_conflict(shift, start, end):
    print()
    for day in range(start, end):
        print("{:>3}|".format(shift[day][1]),end='')
    print()

def show_month_comp(shift, month):
    start = sum([x for x in MONTHS[0:month-1]])
    print("start:", start)

    end = sum([x for x in MONTHS[0:month]])
    print("end:", end)

    for day in range(1, end-start+1):
        print("{:3}|".format(day), end='')
    print()
    show_month(p, start, end)
    show_month(shift, start, end)
    show_conflict(shift, start, end)


#show_month_comp(result_c, 3)
shifts = {'a': results_a, 'b': results_b, 'c':results_c, 'd': results_d}

choice = None
shift = None
month = None
while shift not in shifts.keys():
    shift = input(("Podaj literę zmiany: ")).lower()
while month not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'):
    month = input("Podaj numer miesiąca: ")
month = int(month)
print()
print("Miesiąc: ", month)
show_month_comp(shifts[shift], month)


