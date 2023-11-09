#!/bin/bash

#TODO: replace with hosted version


# onefile
wget https://github.com/DireLines/runpod-python/raw/pyinstaller/runpod-pyinstaller
chmod +x runpod-pyinstaller
mv runpod-pyinstaller /usr/local/bin


#folder
wget https://github.com/DireLines/runpod-python/raw/pyinstaller/runpod-pyinstaller.zip
unzip runpod-pyinstaller.zip
mv runpod-pyinstaller/lib /usr/local/lib
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
chmod +x runpod-pyinstaller/runpod-pyinstaller
mv runpod-pyinstaller/runpod-pyinstaller /usr/local/bin
