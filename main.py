from pytube import Search
import os
from loguru import logger
from time import sleep
import sys

logger.add('logfile.log', rotation='500 MB', compression='zip')

#Function for donwloading and managing the video files.
def file_downloader(ch_songs_dir):
    dir_list = os.listdir(ch_songs_dir)
    for music_name in dir_list:              #Loops through each folder in your songs directory.
        s_query = Search(music_name).results #Searchs yt for an corresponding video title.
        video = s_query[0]                   #Takes the 1st video 
        output_path = os.path.join(ch_songs_dir, music_name)
        chk_path = os.path.join(output_path, 'video.mp4')            
        if os.path.exists(chk_path) == False:
            try:
                logger.info(f'Downloading mv for {music_name}')
                #download the video at the highest available quality on the specified path, with the correct naming for CH
                video.streams.get_highest_resolution().download(output_path=output_path, filename='video.mp4')
                logger.success('Video downloaded!')
                sleep(1)
            except Exception as e:
                logger.error(e)
        else:
            logger.error(f'File already exists! at {chk_path}')
