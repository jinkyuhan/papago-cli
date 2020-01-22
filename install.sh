#!/bin/bash

set -e

# make uninstall script
echo "#!/bin/bash" > ./uninstall.sh
echo "" >> ./uninstall.sh 
echo "sudo rm -f /usr/bin/ppg" >> ./uninstall.sh
echo "sudo rm -rf /usr/share/ppg" >> ./uninstall.sh
echo "echo \"Complete to uninstall papago-cli. You can download it again in https://github.com/jinkyuhan/papago-cli\"" >> ./uninstall.sh

chmod +x ./uninstall.sh


# install papago-cli
if [ ! -d /usr/share/ppg ]; then
	sudo mkdir /usr/share/ppg
	sudo cp ./API_key.json /usr/share/ppg/API_key.json
	sudo cp ./ppg.py /usr/share/ppg/ppg
	sudo chmod +x /usr/share/ppg/ppg
	sudo ln -s /usr/share/ppg/ppg /usr/bin/ppg

	echo "Install Complete"
	echo "Usage : ppg [-e or -k or -j] [source_text]"
else
	echo "papago-cli already exist. please delete it with 'uninstall.sh'"
fi


