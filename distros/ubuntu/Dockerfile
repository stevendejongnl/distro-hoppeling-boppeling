FROM ubuntu:latest

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    dbus-x11 \
    xserver-xorg-video-dummy \
    gnome-core \
    gnome-panel \
    gnome-terminal \
    gnome-shell \
    gnome-tweaks \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

CMD ["dbus-launch", "gnome-session"]

