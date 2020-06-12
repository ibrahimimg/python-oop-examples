#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 22:01:58 2019

@author: ibrahim
"""
from inheritance import Animal

class Student:
    name="Student"
    reg="000"
    level="000"
    def __init__(self,name,reg,level):
        self.name=name
        self.reg=reg
        self.level=level

class Dog(Animal):
    def __init__(self,leg):
        super().set()
        self.leg=leg
    
    def talk(self):
        print ('huhuhuuuuu')
        print ()

class Rat(Dog):
    def __init__(self,leg,no):
        self.leg=leg
        self.no=no
        super().talk()

class Hello:
    def __init__(self,name):
        self.name=name
    def say(self):
        print ('Hello '+self.name)

#using constructor
#user defined
print("STUDENT")
st=Student('Abba','0001','300L')
print (st.name,st.reg,st.level)

abbah=Hello(name="Abba")
abbah.say()


print ("\nDOG USING Animal CLASS")  
d=Dog(4)
print ("NAME :",d.name,"\n","COLOR: ",d.color)
print ("Legs: ",d.leg)

print ("\nDOG USING Dog CLASS")  
d=Dog(4)
d.set("Sharto","Black")
print ("NAME :",d.name,"\n","COLOR: ",d.color)
print ("Legs: ",d.leg)