export PATH=$HOME/.mytools:$PATH
export PATH=$HOME/mytools:$PATH
cd ~/Accountant-MJ
export PATH=$HOME/Accountant-MJ:$PATH
export PULSE_SERVER=127.0.0.1
export PULSE_SERVER=127.0.0.1
alias touch='touch() { command touch "$@" && chmod +x "$@"; }'
pulseaudio --start
pulseaudio --start --log-target=syslog
export PULSE_SERVER=127.0.0.1
pulseaudio --start
export PULSE_SERVER=unix:/data/data/com.termux/files/usr/tmp/pulse-server
export DBUS_SESSION_BUS_ADDRESS=unix:path=/data/data/com.termux/files/usr/var/run/dbus
mkdir -p /data/data/com.termux/files/usr/var/run/dbus
dbus-daemon --session --address=$DBUS_SESSION_BUS_ADDRESS --fork
pulseaudio --start --exit-idle-time=-1
export PULSE_SERVER=unix:/data/data/com.termux/files/usr/tmp/pulse-server
