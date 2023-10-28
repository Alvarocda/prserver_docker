#! /bin/sh

#Check for updates
chmod -R 777 /opt/pr/prbf2_1.7.4.0_server
cd /opt/pr/prbf2_1.7.4.0_server/mods/pr/bin
chmod +x /opt/pr/prbf2_1.7.4.0_server/mods/pr/bin/prserverupdater-linux64
yes '' | ./prserverupdater-linux64

cd /opt/pr/proxy
python3 main.py &
cd /opt/pr/prbf2_1.7.4.0_server/
chmod +x start_pr.sh
./start_pr.sh