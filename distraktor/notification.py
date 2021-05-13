from notifypy import Notify, exceptions


def notification_send(title="Empty", message="No message"):
    notify = Notify()
    notify.title = title
    notify.message = message
    try:
        notify.icon = "data/drinking_water.png"
        notify.send(block=False)
    except (exceptions.InvalidIconPath):
        pass
