count_down = list(range(0,101))
active = True
while active:
    for number in count_down:
        start_count = count_down.pop()
        percent = 0
        if start_count == 75:
            percent = 25
            print(f"{start_count}, we are {percent}% there.")
        elif start_count == 50:
            percent = 50
            print(f"{start_count}, we are {percent}% there.")
        elif start_count == 25:
            percent = 75
            print(f"{start_count}, we are {percent}% there.")
        elif start_count == 0:
            percent = 100
            print(f"{start_count}, we are {percent}% there.")
    if start_count == 0:
        break