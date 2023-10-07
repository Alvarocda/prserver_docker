#! /bin/sh

if [ -z "$SERVER_IP" ]
then
    echo "Server IP not defined"
    exit 1
fi


if [ -z "$LICENCE" ]
then
    echo "Licence not defined"
    exit 1
fi

echo $SERVER_IP
echo $SERVER_PASSWORD
echo $SERVER_INTERNET
echo $SERVER_PORT
echo $SERVER_NAME
echo $VOIP_REMOTE_SERVER_IP
echo $LICENCE
echo $MAX_PLAYERS
echo $WELCOME_MESSAGE
echo $SPONSOR_TEXT
echo $SPONSOR_LOGO_URL
echo $COMMUNITY_LOGO_URL



# UPDATE SERVER NAME
sed -i '/sv.serverName "PR:BF2 Server"/c\sv.serverName "'$SERVER_NAME'"' mods/pr/settings/serversettings.con
sed -i '/sv.password ""/c\sv.password "'$SERVER_PASSWORD'"' mods/pr/settings/serversettings.con
sed -i '/sv.internet 0/c\sv.internet '$SERVER_INTERNET mods/pr/settings/serversettings.con
sed -i '/sv.serverIP ""/c\sv.serverIP "'$SERVER_IP'"' mods/pr/settings/serversettings.con
sed -i '/sv.serverPort ""/c\sv.serverPort "'$SERVER_PORT'"' mods/pr/settings/serversettings.con
sed -i '/sv.voipServerRemoteIP ""/c\sv.voipServerRemoteIP "'$VOIP_REMOTE_SERVER_IP'"' mods/pr/settings/serversettings.con
sed -i '/sv.welcomeMessage ""/c\sv.welcomeMessage "'$WELCOME_MESSAGE'"' mods/pr/settings/serversettings.con
sed -i '/sv.sponsorText ""/c\sv.sponsorText "'$SPONSOR_TEXT'"' mods/pr/settings/serversettings.con
sed -i '/sv.sponsorLogoURL ""/c\sv.sponsorLogoURL "'$SPONSOR_LOGO_URL'"' mods/pr/settings/serversettings.con
sed -i '/sv.communityLogoURL ""/c\sv.communityLogoURL "'$COMMUNITY_LOGO_URL'"' mods/pr/settings/serversettings.con
sed -i '/sv.maxPlayers 64/c\sv.maxPlayers '$MAX_PLAYERS mods/pr/settings/serversettings.con

sed -i '/sv_externalIP = ""/c\sv_externalIP = "'$SERVER_IP'"' mods/pr/python/game/realityconfig_admin.py

# Check if licece.key file exists, if not, create
LICENSE_FILE=/opt/pr/mods/pr/license.key
if [ -f "$LICENSE_FILE" ]; then
    echo "Licence file exists."
else 
    echo "License file does not exist. CREATING!"
    echo $LICENCE >> /opt/pr/mods/pr/license.key
fi

#Check for updates
cd mods/pr/bin/
yes '' | ./prserverupdater-linux64

cd /opt/pr


./start.sh