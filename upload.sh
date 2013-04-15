# Uploads Django and static files to the WebFaction server
scp -r static/* jmcohen@princetonpounce.com:/home/jmcohen/webapps/writetime_static/
scp -r django/* jmcohen@princetonpounce.com:/home/jmcohen/webapps/writetime/
ssh jmcohen@princetonpounce.com /home/jmcohen/webapps/sectionswap/apache2/bin/restart
