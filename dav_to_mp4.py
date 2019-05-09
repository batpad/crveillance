import os
import sys
import glob
import subprocess

def parse_time(time_string):
    year = time_string[0:4]
    month = time_string[4:6]
    day = time_string[6:8]
    hour = time_string[8:12]
    return [year, month, day, hour]

def get_path(year, month, day):
    return os.path.join(year, month, day)

def call_ffmpeg(source, out):
    cmd = ['ffmpeg', '-i', source, '-vf', "select='not(mod(n,15))',setpts=N/FRAME_RATE/TB", out]
    subprocess.check_call(cmd)

if len(sys.argv) != 3:
    print('usage: python dav_to_mp4.py source_dir dest_dir')

source_dir = sys.argv[1]
dest_dir = sys.argv[2]

glob_path = os.path.join(source_dir, '*.dav')

for dav in glob.glob(glob_path):
    filename = os.path.basename(dav)
    filename_parts = filename.split('_')

    # filename should look like NVR_ch2_main_20190507000000_20190507010000.dav
    start_time = filename_parts[3]
    end_time = filename_parts[4].split('.')[0]
    
    year, month, day, hour = parse_time(start_time)
    dest_path = os.path.join(dest_dir, get_path(year, month, day))
    print(dest_path)
    dest_filename = '%s_%s.mp4' % (start_time, end_time)
    dest = os.path.join(dest_path, dest_filename)
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    # If destination mp4 exists, skip
    if os.path.exists(dest):
        continue

    call_ffmpeg(dav, dest)


