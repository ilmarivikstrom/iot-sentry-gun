#!/usr/bin/python
import sys
import os
cmd = '/usr/local/bin/mjpg_streamer -i "/usr/local/lib/input_uvc.so -d /dev/video0 -y YUYV -n" -o "/usr/local/lib/output_http.so -p 8090 -w /usr/locaww"'
os.system(cmd)
