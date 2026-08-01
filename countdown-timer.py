import time

timer = int(input("Enter the countdown time in seconds: "))

for i in reversed(range(0, timer)):
    seconds = i % 60
    minutes = (i // 60) % 60
    hours = (i//3600)%24
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    
    time.sleep(1)

print("time's up!")


