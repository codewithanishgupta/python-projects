from plyer import notification
import time

def water_reminder(intervel_minutes):
    intervel_second = intervel_minutes *60
    print("Water Drinking Reminder Started")
    print(f"You will we notify evry {intervel_minutes} minutes \n")

    while True :
        time.sleep(intervel_second)

        notification.notify(
            title = "Drinking Water ",
            message = " time to drinking water and stay hydrated.",
            timeout = 10
        )

water_reminder(1)