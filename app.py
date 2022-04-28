






#bugs collected from a field research
total_days = 10
day = 1
total_bugs_collected = 0

while day <+ total_days:
    print("day:",day)
    bugs_collected = int(input("Enter the number of the bugs collected on the day:"))
    total_bugs_collected += bugs_collected
    day += 1

print("Total number of bugs collected are: ",total_bugs_collected )