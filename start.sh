#! /bin/sh

export LD_LIBRARY_PATH="/opt/pr/prbf2_1.7.4.0_server/mods/pr/bin/PRMurmur/libs"
export PYTHONPATH="/opt/pr/prbf2_1.7.4.0_server/mods/pr/bin/PRMurmur/python/Ice"

alias python=python2

#Check for updates
chmod -R 777 /opt/pr/prbf2_1.7.4.0_server
cd /opt/pr/prbf2_1.7.4.0_server/mods/pr/bin
chmod +x /opt/pr/prbf2_1.7.4.0_server/mods/pr/bin/prserverupdater-linux64
yes '' | ./prserverupdater-linux64

cd /opt/pr/proxy
python3 main.py &
#cd /opt/pr/prbf2_1.7.4.0_server/mods/pr/bin/PRMurmur/
#chmod +x prmurmurd.x64
#./prmurmurd.x64 &

#sleep 15
#chmod +x initialsetup.sh
#./initialsetup.sh &
#sleep 10
#chmod +x createchannel.sh
#./createchannel.sh &
#sleep 10
#chmod +x startmumo.sh
#./startmumo.sh &

cd /opt/pr/prbf2_1.7.4.0_server/
chmod +x start_pr.sh
./start_pr.sh
