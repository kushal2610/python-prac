import time
max_tries = 5
attempt=0
wait_time = 1
while attempt< 5:
    print(attempt+1, wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempt +=1