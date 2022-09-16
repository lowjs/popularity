from typing import List
import os

CASE_DIR = os.path.join(os.path.dirname(__file__), "cases")

test_cases = next(os.walk(CASE_DIR))[2]
print(len(test_cases))
for case in sorted(test_cases):
    with open(os.path.join(CASE_DIR, case), 'r') as f:
        num_rails = int(f.readline())
        print(num_rails)
        for _ in range(num_rails):
            print(f.readline(), end = "")
        
        f.readline() #OUTPUT
        total_station = int(f.readline())
        user_total_station = input()
        
        list1 = []
        list2 = []
        user_station = []
        user_ticket = []
        for _ in range(total_station):
            line = f.readline()
            station, ticket = line.strip().split(" , ")
            list1.append(station.replace(" ", ""))
            list2.append(ticket)
            
        for _ in range(total_station):
            line = input()
            station, ticket = line.strip().split(" , ")
            user_station.append(station.replace(" ", ""))
            user_ticket.append(ticket)     
        
        if int(user_total_station) != int(total_station):
            raise ValueError("Wrong Total Station!")
        if user_station != list1:
            raise ValueError("Wrong Station Output!")
        if user_ticket != list2:
            raise ValueError("Wrong Ticket Counts!")

print("EXIT", flush=True)