import yaml
import random
import os
import asyncio
import distraktor.notification as notify
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from durations import Duration


def reminder(title="", messages="", icon=""):
    try:
        msg = random.choice(messages)
        icon = random.choice(icon)
        notify.notification_send(title=title, message=msg, icon=icon)
    except KeyboardInterrupt:
        pass


def main():
    data = yaml.load(open("data/data.yaml"), Loader=yaml.BaseLoader)

    scheduler = AsyncIOScheduler()

    for item in data["distraktor"]:
        interval = Duration(item["interval"]).to_seconds()
        scheduler.add_job(
            reminder,
            trigger="interval",
            args=[item["name"], item["messages"], item["icons"]],
            seconds=interval,
        )

    scheduler.start()

    print("Press Ctrl+{0} to exit".format("Break" if os.name == "nt" else "C"))
    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        pass


if __name__ == "__main__":
    main()
