# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 07:41:16 2020

@author: S.Narain Ramaswamy
"""

class Event:
    def __init__(self,name,dob):
        self.__name = name
        self.__dob = dob
    def check_date(self):
        mon = {
            1:"January",
            2:"Febuary",
            3:"March",
            4:"April",
            5:"May",
            6:"June",
            7:"July",
            8:"August",
            9:"September",
            10:"October",
            11:"November",
            12:"December"
            }
        print(self.__dob)
        l = self.__dob.split('/')
        month =int (l[1])
        if month%2==0:
            print("You are offered with the Birthday bash on ",mon[month],l[0],"of this year")
            
        else:
            print("You are not offered with the Birthday bash")
            
        
name = input("Enter your name: ")
dob = input("Enter your Date of Birth: ")
e = Event(name, dob)   
e.check_date()         