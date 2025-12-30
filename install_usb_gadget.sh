#!/bin/bash

check_root() {
    ROOTUID="0"
    if [ "$(id -u)" -ne "$ROOTUID" ] ; then
        echo "This script must be executed with root privileges."
        exit 1
    fi
}

check_root

ask_reboot() {
    while true; do
        read -p "Do you want to reboot? (Y/n) " yn </dev/tty
        case $yn in
            [Yy]* ) /sbin/reboot; break;;
            [Nn]* ) exit 0;;
            * ) echo "Please answer yes or no.";;
        esac
    done
}

install() {
    # Set required settings and modules
    echo "dtoverlay=dwc2" | tee -a /boot/firmware/config.txt
    echo "dwc2" | tee -a /etc/modules
    echo "libcomposite" | tee -a /etc/modules

    # Install the USB HID files
    sudo cp ./pi_zero_usb_media_remote /usr/bin/pi_zero_usb_media_remote
    sudo chmod +x /usr/bin/pi_zero_usb_media_remote

    # Set the USB HID file to run on startup
    sudo cp ./usb_media_remote.service /lib/systemd/system/usb_media_remote.service
    sudo systemctl daemon-reload
    sudo systemctl enable usb_media_remote.service
    sudo service usb_media_remote start
}

uninstall() {
    service usb_media_remote stop
    systemctl disable usb_media_remote.service
    systemctl daemon-reload
    rm /lib/systemd/system/usb_media_remote.service

    rm -rf /sys/kernel/config/usb_gadget/my_gadget/
    rm /usr/bin/pi_zero_usb_media_remote

    sed -i '/dtoverlay=dwc2/d' /boot/firmware/config.txt
    sed -i '/dwc2/d' /etc/modules
    sed -i '/libcomposite/d' /etc/modules
}

if [ -f "/usr/bin/pi_zero_usb_media_remote" ]; then
    echo "Looks like usb gadget already instaled"
    read -p "Do you want to uninstall it? (Y/n) " yn </dev/tty
    case $yn in
        [Yy]* )
            uninstall
            echo "Done uninstalling usb gadget. you should reboot now."    
            ask_reboot; break;;
        [Nn]* ) exit 0;;
        * ) echo "Please answer yes or no.";;
    esac
else
    install
    echo "Installed usb gadget, You should reboot now"
    ask_reboot
fi
