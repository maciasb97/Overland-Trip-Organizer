#import time
#import os.path
#import os
#from os import path
import random
#import psuti

#Presets
selection = 0
str1 = "REISleepingBag"
str2 = "REICampBlanket"
str3 = "REICampChair"
str4 = "SleepingPad"

#--------------------Objects--------------------
class Item:
    def __init__(self, name, worth, weight):
        self.name = name
        self.worth = worth
        self.weight = weight

class Truck:
    def __init__(self,CurbWeight, CurrentWeightOfItems, PayloadCapacity, TotalWeight, TotalWorth):
        self.curbWeight = CurbWeight
        self.currItemsWeight = CurrentWeightOfItems
        self.payloadCapacity = PayloadCapacity      
        self.totalWeight = TotalWeight
        self.totalWorth = TotalWorth
        self.items = []

#--------------------Functions/Methods--------------------
#Read items into a organized list
def read_file(filename):
    f = open(filename, "r")
    itemList = []
    for x in f:
        strlst = x.split()  #splits incoming line into temporary list to manage
        itemWeigh = int(strlst[2])
        itemWorth = int(strlst[1])
        itemList.append(Item(strlst[0], itemWeigh, itemWorth))
        
    return itemList

#Checks to see if item can fit in truck

def item_to_bag(item, bag):
    if bag.currItemsWeight + item.weight <= bag.payloadCapacity:
        bag.currItemsWeight = bag.currItemsWeight + item.weight
        bag.items.append(item)
    else:
        print("could not fit item in bag")


#------------------Algorithm 1 (Greedy)---------------------
#@profile
def greedy(lst, bag):
    lst.sort(key=lambda x: x.worth, reverse=True) #sort list by worth in decending order
   
    #check if item will fit    
    for x in range(len(lst)):
        item_to_bag(lst[x], bag)

    bag.totalWeight = bag.curbWeight + bag.currItemsWeight
    print("-----------------------------")
    print("Item List:")
    print("-----------------------------")
    for v in range(len(bag.items)):
        print(bag.items[v].name)
        bag.totalWorth = bag.totalWorth + bag.items[v].worth


#--------------------MAIN--------------------
#file error checking
filename = ""
if path.exists("ENTER INPUT DATA FILE LOCATION") == False:
    print("ERROR! Check file/code")
    exit()
else:
    if os.stat("ENTER INPUT DATA FILE LOCATION").st_size == 0:
        print("ERROR! Check file/code")
        exit()
    else:
        filename = "ENTER INPUT DATA FILE LOCATION"
mainlst = read_file(filename)

#group selection
print("Welcome to packing app!")
print("What group size will you be traveling with?")
print("1. Solo (1 Adult + Dog)")
print("2. Small (2 Adults + Dog)")
print("3. Medium (3 Adults)")
print("4. Large (4 Adults)")
print("------------------------------")
selection = 4
#random.randint(1, 4)
