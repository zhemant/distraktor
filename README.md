# Distraktor

This app's purpose is to distract you while working simply for keeping your sight good for as long as possible :).

This app will send notification on desktop about drinking water, move eyes from screen to reduce the stress, and whatever more you would like to add. The data is store in data/data.yaml. Under distraktor any type of data can be as long as it provides the values for the given keys.

# How to run?

Install wheel for dependent packages. `pip install wheel`

Install dependencies using requirements.txt `pip install -r requirements.txt`

To run the app, execute `python -m distraktor`.

# To run in docker

security-opt apparmor referenced from: https://github.com/mviereck/x11docker/issues/271 as an alternative to --privileged

docker run mount user dbus to container, as notify-py uses dbus to send notification, the notification are sent from container to host. This works only in linux as it has libnotify which is listening on dbus for notification's.

Follow the steps:

```
# build docker image
docker build -t distraktor:latest .

# start docker image(non detached)
docker run --rm -v "/run/user/1000/bus:/run/user/1000/bus" --env DBUS_SESSION_BUS_ADDRESS="$DBUS_SESSION_BUS_ADDRESS" --user $(id -u):$(id -g) --security-opt apparmor=unconfined  distraktor:latest
```
