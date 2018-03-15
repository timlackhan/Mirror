#!/bin/bash
export DISPLAY=:0
xset dpms force off
raspistill -t 2000 -o image2.jpg -w 640 -h 480
python face_Reco.py
if_Error=$? 
echo $if_Error
echo $if_Error
echo $if_Error
sleep 3
if [ $if_Error -eq 1 ]
then
    xset dpms force on       
fi

