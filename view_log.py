import json
from datetime import datetime
import time

d_format = "%d-%m-%Y, %I:%M:%S %p"
log_path = "D:/Programs/Python/log.json"

try:
    json_file = open(log_path, "r")
    json_data = json.loads(json_file.read())
    json_file.close()
except:
    print("Failed to open/parse file!")
    exit(0)

print("Index \tStart Time \t\t\tEnd Time \t\t\tTotal Time (s)")

index = 1
for entry in json_data:
    print(str(index) + ".\t" + time.strftime(d_format, time.localtime(entry["start_time"])) + "\t\t" + time.strftime(d_format, time.localtime(entry["stop_time"])) + "\t\t" + str(round(entry["stop_time"] - entry["start_time"], 2)))
    index += 1
