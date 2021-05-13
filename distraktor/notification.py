from notifypy import Notify, exceptions


def notification_send(title="Empty", message="No message", icon=""):
    notify = Notify()
    notify.title = title
    notify.message = message
    try:
        notify.icon = icon
        notify.send(block=False)
    except (exceptions.InvalidIconPath):
        pass
