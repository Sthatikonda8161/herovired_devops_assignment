import psutil
import time

limit_percentage = 80

print("Monitoring CPU")

print("Checking usage of the CPU")

while True:
  Current_CPU = psutil.cpu_percentage()
  if Current_CPU = limit_percentage:
      print("Alert..Alert! CPU exceeds limit percentage usage : {Current_CPU}")
    time.sleep(1)
