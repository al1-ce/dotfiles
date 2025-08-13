#!/bin/bash
# rem-accel () {
#     xinput set-prop "$1" "libinput Accel Speed" -0.4
#     xinput set-prop "$1" "libinput Accel Profile Enabled" 1 0 0
# }

# rem-accel "pointer:Logitech ERGO M575" || echo "Missing ERGO M575"
# rem-accel "pointer:Logitech G304" || echo "Missing G304"

rem-accel () {
    xinput set-prop "$1" "libinput Accel Speed" -0.5
    # xinput set-prop "$1" "libinput Accel Profile Enabled" 1 0 0
}

rem-accel "pointer:Logitech ERGO M575" || echo "Missing ERGO M575"
# rem-accel "pointer:Logitech G304" || echo "Missing G304"

