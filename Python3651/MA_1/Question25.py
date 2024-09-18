days = int(input("Enter number of days: "))
hours = int(input("Enter number of hours: "))
minutes = int(input("Enter number of minutes: "))
seconds = int(input("Enter number of seconds: "))

total_seconds = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds
print(f"Total seconds: {total_seconds}")
'''
OUTPUT
Enter number of days: 12
Enter number of hours: 15
Enter number of minutes: 38
Enter number of seconds: 4
Total seconds: 1093084
'''