Scripts and utilities to take a bunch of DAV files and convert them using ffmpeg and organize them into folders based on timestamp.

### dav_to_mp4.py

Usage: python dav_to_mp4.py <source_folder> <dest_folder>

Takes all DAV files in source folder and writes them to destination folder, creating a folder structure like 2019/05/06/ for year/month/day/ . Currently, extracts 1 of every 15 frames and creates mp4 files of the resultant frames in the destination.




