cd -
ckear
clear
pkg reinstall imagemagick -y
pkg reinstall ghostscript -y
magick convert -density 300 installed_packages.pdf -quality 100 installed_packages.png
magick installed_packages.pdf installed_packages.png
ckear
clear
ls -lh installed_packages.png
mkdir -p ~/.magick
echo '<?xml version="1.0" encoding="UTF-8"?>
<policymap>
  <policy domain="coder" rights="read|write"/>
  <policy domain="path" rights="read|write"/>
</policymap>' > ~/.magick/policy.xml
exit
cd -
clear
pkg uninstall imagemagick ghostscript -y
pkg install imagemagick ghostscript -y
ls -lh installed_packages.png
clear
which magick
which gs
mkdir -p ~/.magick
echo '<?xml version="1.0" encoding="UTF-8"?>
<policymap>
  <policy domain="coder" rights="read|write"/>
  <policy domain="path" rights="read|write"/>
</policymap>' > ~/.magick/policy.xml
exit
cd -
(   echo "### 🖥️ SYSTEM INFO ###";   uname -a;   echo -e "\n### 📦 INSTALLED PACKAGES ###";   dpkg --get-selections;   echo -e "\n### 📁 DIRECTORY STRUCTURE ###";   ls -lah $HOME;   echo -e "\n### 🔍 STORAGE INFO ###";   df -h;   echo -e "\n### 🔌 NETWORK INFO ###";   ifconfig;   echo -e "\n### ⚙️ RUNNING PROCESSES ###";   ps aux;   echo -e "\n### ⚠️ LAST ERRORS ###";   tail -n 50 $HOME/.bash_history; ) > termux_system_info.txt
clear
(   echo "### 🖥️ SYSTEM INFO ###";   uname -a;   echo -e "\n### 📦 INSTALLED PACKAGES ###";   dpkg --get-selections;   echo -e "\n### 📁 DIRECTORY STRUCTURE ###";   ls -lah $HOME;   echo -e "\n### 🔍 STORAGE INFO ###";   df -h;   echo -e "\n### 🔌 NETWORK INFO (Limited Output) ###";   ip a;   echo -e "\n### ⚙️ RUNNING PROCESSES ###";   ps aux;   echo -e "\n### ⚠️ LAST ERRORS ###";   tail -n 50 ~/.bash_history; ) > termux_system_info.txt
pkg install python fpdf -y
python3 -c "from fpdf import FPDF;
data = open('termux_system_info.txt').read().splitlines();
pdf = FPDF(); pdf.set_auto_page_break(auto=True, margin=15);
pdf.add_page(); pdf.set_font('Arial', '', 8);
for item in data: pdf.cell(0, 5, str(item), ln=True);
pdf.output('termux_system_info.pdf');"
clear
pkg update && pkg upgrade -y
pkg install python imagemagick ghostscript -y
pip install fpdf2
clear
(   echo "### 🖥️ SYSTEM INFO ###";   uname -a;   echo -e "\n### 📦 INSTALLED PACKAGES ###";   dpkg --get-selections;   echo -e "\n### 📁 DIRECTORY STRUCTURE ###";   ls -lah $HOME;   echo -e "\n### 🔍 STORAGE INFO ###";   df -h;   echo -e "\n### 🔌 NETWORK INFO (Limited Output) ###";   ip a;   echo -e "\n### ⚙️ RUNNING PROCESSES ###";   ps aux;   echo -e "\n### ⚠️ LAST ERRORS ###";   tail -n 50 ~/.bash_history; ) > termux_system_info.txt
python3 -c "from fpdf import FPDF;
data = open('termux_system_info.txt', encoding='utf-8').read().splitlines();
pdf = FPDF(); pdf.set_auto_page_break(auto=True, margin=15);
pdf.add_page(); pdf.set_font('Arial', '', 6);
for item in data: pdf.cell(0, 3, item.encode('latin-1', 'ignore').decode('latin-1'), ln=True);
pdf.output('termux_system_info.pdf');"
gs -dNOPAUSE -dBATCH -sDEVICE=png16m -r300 -sOutputFile=termux_system_info.png termux_system_info.pdf
mv termux_system_info.png /sdcard/
termux-share -a send -c 'image/png' /sdcard/termux_system_info.png
gs -dNOPAUSE -dBATCH -sDEVICE=png16m -r300 -sOutputFile=termux_system_info_%d.png termux_system_info.pdf
mv termux_system_info_*.png /sdcard/
clear
exite
exit
pkg update && pkg upgrade -y
ckear
clear
pkg install python python-pip git nano curl wget openssh termux-api imagemagick ghostscript ffmpeg sox jq -y
clear
pip install --upgrade pip
pip install fpdf requests flask numpy pandas openai pyttsx3 speechrecognition termcolor
clear
pip install --upgrade pip
pip install fpdf requests flask numpy pandas openai pyttsx3 speechrecognition termcolor
clear
pkg install python python-pip git nano curl wget openssh termux-api imagemagick ghostscript ffmpeg sox jq -y
pip install --upgrade pip
pip install fpdf requests flask numpy pandas openai pyttsx3 speechrecognition termcolor
clear
bash start_all.sh
clear
termux-setup-storage
termux-microphone-record -d
clear
termux-setup-storage
termux-microphone-record -d
clear
termux-setup-storage
exit
dpkg --remove termux-api
dpkg --purge termux-api
cd -
dpkg --remove termux-api
dpkg --purge termux-api
exit
pkg update && pkg upgrade -y
pkg install wget -y
wget https://f-droid.org/repo/com.termux.api_51.apk -O termux-api.apk
apt remove termux-api -y
apt purge termux-api -y
clear
pkg update && pkg upgrade -y
pkg install wget -y
wget https://f-droid.org/repo/com.termux.api_51.apk -O termux-api.apk
am start -a android.intent.action.VIEW -d file://$HOME/termux-api.apk -t application/vnd.android.package-archive
apt remove termux-api -y
apt purge termux-api -y
clear
pkg update && pkg upgrade -y
pkg install wget -y
wget https://f-droid.org/repo/com.termux.api_51.apk -O ~/storage/downloads/termux-api.apk
clear
termux-open ~/storage/downloads/termux-api.apk
apt remove termux-api -y
apt purge termux-api -y
clear
cd -
pkg update && pkg upgrade -y
pkg install wget -y
wget https://f-droid.org/repo/com.termux.api_51.apk -O ~/termux-api.apk
termux-open ~/termux-api.apk
apt remove termux-api -y
apt purge termux-api -y
clear
cd ~  # होम डायरेक्टरी में जाएं
rm -f termux-api.apk  # पुरानी फाइल हटाएं
pkg update && pkg upgrade -y
pkg install wget -y
wget https://f-droid.org/repo/com.termux.api_51.apk -O ~/termux-api.apk
ls -lh ~ | grep termux-api.apk
termux-open ~/termux-api.apk
termux-setup-storage
pkg install termux-api -y
clear
rm -rf $PREFIX/etc/apt/sources.list.d
mkdir -p $PREFIX/etc/apt/sources.list.d
echo "deb https://packages-cf.termux.dev/apt/termux-main stable main" > $PREFIX/etc/apt/sources.list
pkg update && pkg upgrade -y
pkg install termux-tools -y
termux-setup-storage
pkg install termux-api -y
termux-battery-status
clear
ls
source venv/bin/activate
python main.py
pulseaudio --start --exit-idle-time=-1
export PULSE_SERVER=127.0.0.1
pulseaudio --check
source venv/bin/activate
python main.py
cd ~
ls
clear
pwd
shopt -s extglob
mv !(Accountant-MJ) Accountant-MJ/
ls
./Accountant-MJ
exit
clear
ls
source venv/bin/activate
pip install -r requirements.txt
python main.py
clear
cd ~/Accountant-MJ
# अगर requirements.txt फाइल missing है, तो इसे create करें
cat > requirements.txt <<EOF
flask
termux-api
requests
speechrecognition
pyaudio
EOF

# अब dependencies install करें
pip install -r requirements.txt
pkg update && pkg upgrade -y
pkg install pulseaudio
termux-audio-ctl volume 15
pulseaudio --start
export PULSE_SERVER=127.0.0.1
clear
pkg update && pkg upgrade -y
pkg install termux-api pulseaudio sox
pulseaudio --start --exit-idle-time=-1
termux-media-player play test.mp3
pkill pulseaudio
rm -rf ~/.config/pulse
clear
pulseaudio --start --exit-idle-time=-1
export PULSE_SERVER=127.0.0.1
pulseaudio --check
source venv/bin/activate
python main.py
clear
source venv/bin/activate
python main.py
clear
pwd
ls -a
cd ~
ls
exit
pkill pulseaudio
rm -rf ~/.config/pulse
pulseaudio --start --exit-idle-time=-1
export PULSE_SERVER=127.0.0.1
source venv/bin/activate
python main.py
clear
source venv/bin/activate
python main.py
clear
source venv/bin/activate
python main.py
clear
source venv/bin/activate
python main.py
clear
pkg update && pkg upgrade -y
pkg install termux-api pulseaudio sox alsa-utils
pulseaudio --kill
pulseaudio --start --exit-idle-time=-1
export PULSE_SERVER=127.0.0.1
mkdir -p ~/.config/alsa
touch ~/.config/alsa/asoundrc
echo "defaults.pcm.card 1" > ~/.config/alsa/asoundrc
aplay -l
rm -rf ~/.config/alsa
mkdir -p ~/.config/alsa
touch ~/.config/alsa/asoundrc
echo "defaults.pcm.card 0" > ~/.config/alsa/asoundrc
pulseaudio --kill
pulseaudio --start
source venv/bin/activate
python main.py
clear
pulseaudio --kill
rm -rf ~/.config/pulse
rm -rf ~/.config/alsa
rm -rf ~/.pulse
rm -rf ~/.asoundrc
mkdir -p ~/.config/alsa
touch ~/.config/alsa/asoundrc
pulseaudio --cleanup-shm
clear
ps aux | grep pulseaudio
rm -rf ~/.config/pulse ~/.config/alsa ~/.pulse ~/.asoundrc
mkdir -p ~/.config/alsa
touch ~/.config/alsa/asoundrc
echo "defaults.pcm.card 0" > ~/.config/alsa/asoundrc
pkg update && pkg upgrade -y
pkg install pulseaudio alsa-utils -y
clear
pulseaudio --start --exit-idle-time=-1
export PULSE_SERVER=127.0.0.1
aplay -l
termux-setup-storage
modprobe snd-dummy
clear
pulseaudio --kill
rm -rf ~/.config/pulse ~/.config/alsa ~/.pulse ~/.asoundrc
mkdir -p ~/.config/alsa
touch ~/.config/alsa/asoundrc
echo "defaults.pcm.card 1" > ~/.config/alsa/asoundrc
pulseaudio --start --exit-idle-time=-1
export PULSE_SERVER=127.0.0.1
pkg update && pkg upgrade -y
pkg install pulseaudio alsa-utils -y
pkg update && pkg upgrade -y
pkg install pulseaudio alsa-utils -y
clear
termux-setup-storage
mkdir -p ~/.termux
echo "allow-external-apps=true" > ~/.termux/termux.properties
pactl list sinks
pactl list sources
clear
pkg install termux-services -y
sv-enable pulseaudio
aplay -l
exit
pkg install pulseaudio alsa-utils termux-api -y
clear
nano config
clear
pulseaudio --start
sleep 2
pulseaudio --check
pactl list sinks
pactl list sources
pulseaudio --kill || true
rm -rf ~/.config/pulse ~/.pulse* ~/.cache/pulse
rm -rf /data/data/com.termux/files/home/.config/pulse
clear
pkg update && pkg upgrade -y
pkg install pulseaudio termux-api -y
clear
ls
nano config
nano confi
nano config
clear
export PULSE_SERVER=unix:/data/data/com.termux/files/usr/tmp/pulse-server
pulseaudio --start
sleep 2
pulseaudio --check
export PULSE_SERVER=unix:/data/data/com.termux/files/usr/tmp/pulse-server
pactl list sinks
pactl list sources
ls
rm -rf config
ls
clear
nano config.py
echo "alias touch='touch() { command touch \"\$@\" && chmod +x \"\$@\"; }'" >> ~/.bashrc
source ~/.bashrc
ls
ckear
clear
ls
chmod +x requirements.txt config.py chatbot.log
ls
chmod +x finance.log home_files.txt tax_api.log test.mp3
ls
chmod +x ocr.log voice.log main.log dmesg_logs.txt
ls
chmod +x termux-api.apk termux_logs.txt termux_processes.txt 
clear
ls
chmod -x termux_services.json termux_services.pdf termux_system_info.pdf termux_system_info.txt error_logs.txt README.md 
ls
chmod +x termux_system_info.txt termux_system_info.pdf large_files.txt installed_packages_fixed.pdf installed_packages.txt 
ls
clear
export PULSE_SERVER=unix:/data/data/com.termux/files/usr/tmp/pulse-server
pulseaudio --start
sleep 2
pulseaudio --check
export PULSE_SERVER=unix:/data/data/com.termux/files/usr/tmp/pulse-server
pactl list sinks
pactl list sources
ckear
clear
pkg update -y && pkg upgrade -y
pkg install pulseaudio -y
pulseaudio --start
export PULSE_SERVER=unix:/data/data/com.termux/files/usr/tmp/pulse-server
pactl list sinks
pactl list sources
echo 'pulseaudio --start' >> ~/.bashrc
source ~/.bashrc
pactl list sinks
pactl list sources
echo 'pulseaudio --start --log-target=syslog' >> ~/.bashrc
echo 'export PULSE_SERVER=127.0.0.1' >> ~/.bashrc
source ~/.bashrc
clear
termux-microphone-record -l
pkg update -y && pkg upgrade -y
pkg install pulseaudio -y
pkg install termux-api -y
pkg install sox -y
pkg install ffmpeg -y
pkg install python -y
clear
echo 'pulseaudio --start' >> ~/.bashrc
echo 'export PULSE_SERVER=unix:/data/data/com.termux/files/usr/tmp/pulse-server' >> ~/.bashrc
source ~/.bashrc
pactl info
pulseaudio --start
export PULSE_SERVER=unix:/data/data/com.termux/files/usr/tmp/pulse-server
pactl info
pactl list sources
pactl list sinks
clear
pulseaudio --kill
rm -rf ~/.config/pulse
rm -rf /data/data/com.termux/files/usr/tmp/pulse-server
pulseaudio --start --exit-idle-time=-1
export PULSE_SERVER=unix:/data/data/com.termux/files/usr/tmp/pulse-server
pactl info
pulseaudio --verbose
clear
pactl list sources
pactl list sinks
ckear
clear
pulseaudio --kill
rm -rf ~/.config/pulse
rm -rf /data/data/com.termux/files/usr/tmp/pulse-server
rm -rf /data/data/com.termux/files/usr/var/run/dbus
export DBUS_SESSION_BUS_ADDRESS=unix:path=/data/data/com.termux/files/usr/var/run/dbus
mkdir -p /data/data/com.termux/files/usr/var/run/dbus
dbus-daemon --session --address=$DBUS_SESSION_BUS_ADDRESS --fork
pulseaudio --start --exit-idle-time=-1 --log-target=stderr
export PULSE_SERVER=unix:/data/data/com.termux/files/usr/tmp/pulse-server
pactl info
echo 'export DBUS_SESSION_BUS_ADDRESS=unix:path=/data/data/com.termux/files/usr/var/run/dbus' >> ~/.bashrc
echo 'mkdir -p /data/data/com.termux/files/usr/var/run/dbus' >> ~/.bashrc
echo 'dbus-daemon --session --address=$DBUS_SESSION_BUS_ADDRESS --fork' >> ~/.bashrc
echo 'pulseaudio --start --exit-idle-time=-1' >> ~/.bashrc
echo 'export PULSE_SERVER=unix:/data/data/com.termux/files/usr/tmp/pulse-server' >> ~/.bashrc
source ~/.bashrc
clear
exit
ckear
clear
pulseaudio --kill
rm -rf ~/.config/pulse
rm -rf /data/data/com.termux/files/usr/tmp/pulse-server
rm -rf /data/data/com.termux/files/usr/var/run/dbus
export DBUS_SESSION_BUS_ADDRESS=unix:path=/data/data/com.termux/files/usr/var/run/dbus
mkdir -p /data/data/com.termux/files/usr/var/run/dbus
dbus-daemon --session --address=$DBUS_SESSION_BUS_ADDRESS --fork
clear
pkill -9 pulseaudio
pkill -9 dbus-daemon
rm -rf ~/.config/pulse
rm -rf /data/data/com.termux/files/usr/tmp/pulse-server
rm -rf /data/data/com.termux/files/usr/var/run/dbus
export DBUS_SESSION_BUS_ADDRESS=unix:path=/data/data/com.termux/files/usr/var/run/dbus
mkdir -p /data/data/com.termux/files/usr/var/run/dbus
dbus-daemon --session --address=$DBUS_SESSION_BUS_ADDRESS --fork
pulseaudio --start --exit-idle-time=-1 --log-target=stderr
export PULSE_SERVER=unix:/data/data/com.termux/files/usr/tmp/pulse-server
adb connect <phone-ip>:5555
adb devices
adb shell
pulseaudio --kill
pulseaudio --start --log-level=4 --log-target=stderr
dbus-daemon --session --print-address --verbose
clear
pkg update && pkg upgrade -y
pkg install android-tools
exit
cd -
$ ls -a ~/.config
.  ..  pulse
clear
exit
cd -
exit
cd -
ls
clear
ls -la
chmod +x .gitignore
ls
ls -la
chmod +x .env
ls -la
clear
cd ..
ls
ls -l
mv -v ~/adbfiles ~/Accountant-MJ/
mv -v ~/fix_pulseaudio.sh ~/Accountant-MJ/
ls -l
exit
ls
chmo +x nohup.out
chmod -x nohup.out
ls
clear
pkg update && pkg upgrade -y
pkg install python nodejs git termux-api openssh ffmpeg curl wget -y
clear
cd ~/Accountant-MJ  # अपनी Project Directory में जाएं
git init  # Repository को Git से Initialize करें
git remote add origin https://github.com/Meghraj077/Accountant-MJ.git  # GitHub Repo को जोड़ें
git branch -M main  # Main Branch सेट करें
git add .  # सभी Files को Staging में डालें
git commit -m "First Commit - Accountant-MJ Code Upload"  # Code को Commit करें
git push -u origin main  # GitHub पर Push करें
git remote add origin https://github.com/Meghraj077/Accountant-MJ.git
git add .
git commit -m "Set up Git identity"
git config --global user.name "Meghraj077"
git config --global user.email "meghrajjanghel0234@gmail.com"
git add .
git commit -m "Set up Git identity"
git config --global user.name "Meghraj"
git config --global user.email "your-email@example.com"
clear
git add .
git commit -m "Added all Accountant-MJ files"
git push -u origin main
nano .env
ls
pip install python-dotenv
clear
nano config.py
config.py
mkdir -p ~/.config/pulse
echo "autospawn = yes" > ~/.config/pulse/client.conf
echo "daemon-binary = /data/data/com.termux/files/usr/bin/pulseaudio" >> ~/.config/pulse/client.conf
echo "default-server = unix:/data/data/com.termux/files/usr/tmp/pulse-server" >> ~/.config/pulse/client.c>exit
exit
