import os
import time
from pytube import *

class youtube_download:
    
    ### The Start ###
    def __init__(self):
        print("**********************************************")
        print("*  * * *         **    **         *****      *")
        print("*  *    *        * *  * *        *           *")
        print("*  *     *       *  **  *       *            *")
        print("*  *     *       *      *       *   ****     *")
        print("*  *    *        *      *        *    *      *")
        print("*  * * *         *      *         ****       *")
        print("**********************************************")
        print("               Yossef W. Eldeeb               ")

        print("\nUse to download videos or audios from YouTube\n")

        self.first_choose()

    ### Video Downloaded Message ###
    def finish(self):
        print("\nDownload done!")
        
    ####  First Choose #####    
    def first_choose(self):
        print("\n \nChoose the type:- \n")
        print("1) Video")
        print("2) Audio")
        print("3) Exit!")

        self.choose_type()
        
    def choose_type(self):
        while True:
            ans_type = input("\n: ")
            try:
                ans_type = int(ans_type)
                if ans_type == 1:
                    self.print_choose_video()
                elif ans_type == 2:
                    self.print_choose_audio()
                elif ans_type == 3:
                    exit()
                else:
                    print("Choose number between 1 , 2 and 3!")
            except ValueError:
                print("Please, Enter A Valid number!")
    ####  Choose Video #####
    def print_choose_video(self):
        print("\n___________________________________________________\n")
        print("\n \nChoose download single video or Playlist:- \n")
        print("1) Single Video")
        print("2) Playlist")
        print("3) Back")
        print("4) Exit!")

        self.choose_video()

    def choose_video(self):
        while True:
            ans_video = input("\n: ")
            try:
                ans_video = int(ans_video)
                if ans_video == 1:
                    self.print_choose_quality_video()
                elif ans_video == 2:
                    self.print_choose_quality_playlist()
                elif ans_video == 3:
                    print("\n___________________________________________________\n")
                    self.first_choose()
                    break
                elif ans_video == 4:
                    exit()
                else:
                    print("Choose number between 1 , 2 3, 4!")
            except ValueError:
                print("Please, Enter a Valid number!")
    ### Choose Video Quality ###
    def print_choose_quality_video(self):
        print("\n___________________________________________________\n")
        print("\n \nChoose the quality :- \n")
        print("1) High Quality")
        print("2) Low Quality")
        print("3) Back")
        print("4) Exit!")

        self.choose_quality_video()
    def choose_quality_video(self):
        while True:
            ans_video_quality = input("\n: ")
            try:
                ans_video_quality = int(ans_video_quality)
                if ans_video_quality == 1:
                    self.download_video_high()
                    self.print_choose_quality_video()
                elif ans_video_quality == 2:
                    self.download_video_low()
                    self.print_choose_quality_video()
                elif ans_video_quality == 3:
                    self.print_choose_video()
                    break
                elif ans_video_quality == 4:
                    exit()
                else:
                    print("Choose number between 1 , 2 3, 4!")
            except ValueError:
                print("Please, Enter a Valid number!")
    ### Choose Playlist video Quality ###
    def print_choose_quality_playlist(self):
        print("\n___________________________________________________\n")
        print("\n \nChoose the quality :- \n")
        print("1) High Quality")
        print("2) Low Quality")
        print("3) Back")
        print("4) Exit!")

        self.choose_quality_playlist()
    def choose_quality_playlist(self):
        while True:
            ans_playlist_quality = input("\n: ")
            try:
                ans_playlist_quality = int(ans_playlist_quality)
                if ans_playlist_quality == 1:
                    self.download_playlist_high()
                    self.print_choose_quality_playlist()
                elif ans_playlist_quality == 2:
                    self.download_playlist_low()
                    self.print_choose_quality_playlist()
                elif ans_playlist_quality == 3:
                    self.print_choose_video()
                    break
                elif ans_playlist_quality == 4:
                    exit()
                else:
                    print("Choose number between 1 , 2 3, 4!")
            except ValueError:
                print("Please, Enter a Valid number!")
    ### download video high quality ###
    def download_video_high(self):
        
        lvtube = input("Enter link the Video: ")
        try:
            vtube = YouTube(lvtube)
            print("\nDownloading, just wait!")
            vtube.streams.get_highest_resolution().download()
            vtube.register_on_complete_callback(self.finish())
            print("\nThe Download Dir: \n\"",os.getcwd(),"\"\n")
            time.sleep(5)
        except exceptions.RegexMatchError:
            print('\nEnter A Valid URL!')

        except exceptions.ExtractError:
            print('\nEnter A Valid URL!')

        except exceptions.VideoUnavailable:
            print('\nThe following video is unavailable')
    ### download video low quality ###
    def download_video_low(self):
        lvtube = input("Enter link the Video: ")
        try:
            vtube = YouTube(lvtube)
            print("\nDownloading, just wait!")
            vtube.streams.get_lowest_resolution().download()
            vtube.register_on_complete_callback(self.finish())
            print("\nThe Download Dir: \n\"",os.getcwd(),"\"\n")
            time.sleep(5)
        except exceptions.RegexMatchError:
            print('\nEnter A Valid URL!')

        except exceptions.ExtractError:
            print('\nEnter A Valid URL!')

        except exceptions.VideoUnavailable:
            print('\nThe following video is unavailable')
    ### download playlist video high quality ###
    def download_playlist_high(self):
        lptube = input("Enter link the Playlist: ")
        try:
            ptube = Playlist(lptube)
            num = len(ptube.video_urls)
            print("\n Number of videos in the playlist: ",num)
            x = 0
            
            for video in ptube.videos:
                x = x +1
                print("\nVideo number: ",x)
                print("Downloading, just wait!")
                video.streams.get_highest_resolution().download()
            if num == 0:
                print("The Playlist is empty")
            else:
                print("\nPlaylist downloaded")
                print("\nThe Download Dir: \n\"",os.getcwd(),"\"\n")
                time.sleep(5)
        except exceptions.RegexMatchError:
            print('\nEnter A Valid URL!')

        except exceptions.ExtractError:
            print('\nEnter A Valid URL!')

        except exceptions.VideoUnavailable:
            print('\nThe following video is unavailable')
        except KeyError:
            print('\nEnter A Valid URL!')
    ### download playlist video low quality ###
    def download_playlist_low(self):
        lptube = input("Enter link the Playlist: ")
        try:
            ptube = Playlist(lptube)
            num = len(ptube.video_urls)
            print("\n Number of videos in the playlist: ",num)
            x = 0
            for video in ptube.videos:
                x = x +1
                print("\nVideo number: ",x)
                print("Downloading, just wait!")
                video.streams.get_lowest_resolution().download()
            if num == 0:
                print("The Playlist is empty")
            else:
                print("\nPlaylist downloaded")
                print("\nThe Download Dir: \n\"",os.getcwd(),"\"\n")
        except exceptions.RegexMatchError:
            print('\nEnter A Valid URL!')

        except exceptions.ExtractError:
            print('\nEnter A Valid URL!')

        except exceptions.VideoUnavailable:
            print('\nThe following video is unavailable')
        except KeyError:
            print('\nEnter A Valid URL!')
    ####  Choose Audio #####
    def print_choose_audio(self):
        print("\n___________________________________________________\n")
        print("\n \nChoose download single audio or Playlist:- \n")
        print("1) Single Audio")
        print("2) Playlist")
        print("3) Back")
        print("4) Exit!")

        self.choose_audio()

    def choose_audio(self):
        while True:
            ans_audio = input("\n: ")
            try:
                ans_audio = int(ans_audio)
                if ans_audio == 1:
                    self.download_audio()
                    self.print_choose_audio()
                elif ans_audio == 2:
                    self.download_playlist_audio()
                    self.print_choose_audio()
                elif ans_audio == 3:
                    self.first_choose()
                    break
                elif ans_audio == 4:
                    exit()
                else:
                    print("Choose number between 1 , 2 3, 4!")
            except ValueError:
                print("Please, Enter a Valid number!")        
    def download_audio(self):
        latube = input("Enter link the Audio: ")
        try:
            atube = YouTube(latube)
            print("\nDownloading, just wait!")
            atube.streams.get_by_itag(251).download()
            atube.register_on_complete_callback(self.finish())
            print("\nThe Download Dir: \n\"",os.getcwd(),"\"\n")
            time.sleep(5)
        except exceptions.RegexMatchError:
            print('\nEnter A Valid URL!')

        except exceptions.ExtractError:
            print('\nEnter A Valid URL!')

        except exceptions.VideoUnavailable:
            print('\nThe following video is unavailable')
    def download_playlist_audio(self):
        laptube = input("Enter link the Playlist: ")
        try:
            aptube = Playlist(laptube)
            num = len(aptube.video_urls)
            print("\n Number of Audios in the playlist: ",num)
            x = 0
            for video in aptube.videos:
                x = x +1
                print("\nAudio number: ",x)
                print("Downloading, just wait!")
                video.streams.get_by_itag(251).download()
            if num == 0:
                print("The Playlist is empty")
            else:
                print("\nPlaylist downloaded")
                print("\nThe Download Dir: \n\"",os.getcwd(),"\"\n")
        except exceptions.RegexMatchError:
            print('\nEnter A Valid URL!')

        except exceptions.ExtractError:
            print('\nEnter A Valid URL!')

        except exceptions.VideoUnavailable:
            print('\nThe following video is unavailable')
        except KeyError:
            print('\nEnter A Valid URL!')


Youtube = youtube_download()
