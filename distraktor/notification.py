from notifypy import Notify, exceptions


def notification_send():
    notif = Notify()
    notif.title = "water break"
    notif.message = "drink water"
    try:
        notif.icon = "ico"
        notif.send(block=False)
    except (exceptions.InvalidIconPath):
        pass
