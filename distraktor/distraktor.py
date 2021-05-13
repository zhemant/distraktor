import yaml
import random
import threading
import time
import notification as notify


def reminder(messages):
    interval_water = 5
    while True:
        try:
            msg = random.choice(messages)
            notify.notification_send(title="drink water", message=msg)
            time.sleep(1)
        except KeyboardInterrupt:
            break


def main():
    config = yaml.load(open("data/data.yaml"), Loader=yaml.BaseLoader)
    water_messages = config["water_messages"]
    print(water_messages)
    reminder(water_messages)


if __name__ == "__main__":
    main()
