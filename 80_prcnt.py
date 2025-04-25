import psutil
from plyer import notification
import time


notified = False

while (True):
   battery = psutil.sensors_battery()
   percent = battery.percent
   charging_state = battery.power_plugged

   if charging_state and percent >= 80 and not notified:
      notification.notify(
         title = "WARNING",
         message = str(percent)+ "% REACHED",
         timeout = 5
      )
      notified = True

   elif not charging_state or percent <= 80:
      notified = False

   time.sleep(60)
