import time
from datetime import datetime
import psutil
import json

app_name = "AndroidEmulator.exe"
index = 1
status = 0
start_time = None
d_format = "%d-%m-%Y, %I:%M:%S %p"
log_path = "D:/Programs/Python/log.json"

try:
    read_file = open(log_path)
    json_data = read_file.read()
    if json_data == "":
        json_data = []
    else:
        json_data = json.loads(json_data)
    read_file.close()
except:
    json_data = []
    print("Failed to parse log file!\n")

print("Application Launched: " + str(datetime.now().strftime(d_format)))
print("Monitoring \"" + app_name + "\"\n")
print("-----------------------------------------------------------------------------------------------")

while True:
    try:
        if (app_name in (p.name() for p in psutil.process_iter())):
            if (status == 0):
                print(str(index) + ". STARTED")
                index += 1
                print("Timestamp: " + str(datetime.now().strftime(d_format)))
                status = 1
                start_time = time.time()
        else:
            if (status == 1):
                print("Session Summary:")
                obj = {
                    "start_time": start_time,
                    "stop_time": time.time()
                }
                print("Ended at " + str(datetime.now().strftime(d_format)) + ", Total Time => " + str(round(time.time() - start_time, 2)) + " seconds.")
                print("-----------------------------------------------------------------------------------------------")
                status = 0
                json_data.append(obj)
    except KeyboardInterrupt:
        write_file = open(log_path, "w")
        write_file.write(json.dumps(json_data))
        write_file.close()
        break
