#!/bin/bash

sudo mkdir /usr/share/ppg
sudo cp ./API_key.json /usr/share/ppg/API_key.json
sudo cp ./ppg.py /usr/share/ppg/ppg
sudo chmod +x /usr/share/ppg/ppg
sudo ln -s /usr/share/ppg/ppg /usr/bin/ppg

echo "Install Complete"
echo "Usage : ppg [-e or -k or -j] [source_text]"
