mkdir -p ~/.config/pulse
echo "autospawn = yes" > ~/.config/pulse/client.conf
echo "daemon-binary = /data/data/com.termux/files/usr/bin/pulseaudio" >> ~/.config/pulse/client.conf
echo "default-server = unix:/data/data/com.termux/files/usr/tmp/pulse-server" >> ~/.config/pulse/client.conf
