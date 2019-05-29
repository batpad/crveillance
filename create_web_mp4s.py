import os
import sys
import glob
import subprocess
from utils import parse_time, get_path

def call_ffmpeg(source, out):
    cmd = ['ffmpeg', '-i', source, '-crf', '20', '-vf', 'scale=720:-2', out]
    subprocess.check_call(cmd)

if len(sys.argv) != 3:
    print('usage: python dav_to_mp4.py source_dir dest_dir')

source_dir = sys.argv[1]
dest_dir = sys.argv[2]

glob_path = os.path.join(source_dir, '**/*.mp4')

for vid in glob.glob(glob_path, recursive=True):
    filename = os.path.basename(vid)
    filename_parts = filename.split('_')

    # filename should look like NVR_ch2_main_20190507000000_20190507010000.dav
    start_time = filename_parts[0]
    end_time = filename_parts[1].split('.')[0]
    
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
    #print(vid, dest)
    call_ffmpeg(vid, dest)


