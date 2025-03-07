#!/data/data/com.termux/files/usr/bin/bash
echo "🔄 Fixing PulseAudio & ALSA Issues..."
pkill -9 pulseaudio
rm -rf /run/user/$(id -u)/pulse
rm -rf ~/.config/pulse
rm -rf ~/.pulse*
rm -rf /tmp/pulse-*
rm -rf ~/.pulse-cookie
mkdir -p ~/.config/pulse
echo -e "default-server = 127.0.0.1\nautospawn=yes\ndaemon-binary=/data/data/com.termux/files/usr/bin/pulseaudio" > ~/.config/pulse/client.conf
mkdir -p ~/.asoundrc
echo -e "pcm.!default {\n  type hw\n  card 0\n}\nctl.!default {\n  type hw\n  card 0\n}" > ~/.asoundrc
export PULSE_SERVER=127.0.0.1
pulseaudio --start --log-level=debug
pactl load-module module-null-sink sink_name=VirtualSink
pactl set-default-sink VirtualSink
pactl list sinks
echo "✅ PulseAudio & ALSA Fixed!"
