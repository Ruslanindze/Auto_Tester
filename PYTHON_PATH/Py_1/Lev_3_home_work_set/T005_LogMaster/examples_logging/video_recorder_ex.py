#  -*- coding: utf-8 -*-                                                                                             #
# Python 3.x.x
#--------------------------------
# The script demonstrates desktop recording using ffmpeg.
# Is done recordind 2 (or 1 th) workers monitors, without any tests.
#--------------------------------
import time, os, signal, psutil
import subprocess as subp
from os.path import join

log_dir = r'd:\WORK_MC_21\Tester\Auto_Tester\PYTHON_PATH\Py_1\Lev_3_home_work_set\T005_LogMaster\examples_logging'  # path where create video
CORE_DIR = r'c:\FFmpeg\bin'  # path ffmpeg.exe
id_test = '001'
video_file = join(log_dir, 'video_' + id_test + '.flv') # name video file
FFMPEG_BIN = join(CORE_DIR, 'ffmpeg.exe')

command = [
    FFMPEG_BIN,
    '-y',                   # overwrite output files
    '-loglevel', 'error',
    '-f', 'gdigrab',
    # '-framerate', '12',   # default 30
    '-i', 'desktop',
    # '-t', '10',           # record or transcode "duration" seconds of audio/video
    '-s', '3000x1000',
    '-pix_fmt', 'yuv420p',
    '-c:v', 'libx264',
    '-profile:v', 'main',
    '-fs', '0.7M',          # set the limit file size in bytes
    video_file
]

# run record video with ffmpeg-commands
ffmpeg = subp.Popen(command, stdin=subp.PIPE, stdout=subp.PIPE, stderr=subp.PIPE)
time.sleep(6)

# close the video stream
ffmpeg.stdin.write("q".encode('utf-8'))
ffmpeg.stdin.close()