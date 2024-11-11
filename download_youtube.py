import argparse
import yt_dlp

def download_video(link, save_path):
    # yt-dlp options to download as MP4
    ydl_opts = {
        'format': 'mp4',  # specify mp4 format
        'outtmpl': save_path + '%(title)s.%(ext)s',  # output path and filename
    }
    
    try:
        # Download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        
        print('Video downloaded successfully as MP4!')
    except Exception as e:
        print("Error during download:", e)

def main():
    # setup the parser
    parser = argparse.ArgumentParser(description="Download a YouTube video as an MP4.")

    # argu,ents
    parser.add_argument("--input", default="https://youtu.be/_iETa2KDRuw?si=D2xgXWkt5bss9Mq-", help="URL of the YouTube video to download. Defaults to a sample link.")
    parser.add_argument("--output", default="output/", help="Path to save the downloaded video. Defaults to 'output/'.")

    # parse
    args = parser.parse_args()
    
    # Download the video
    download_video(args.input, args.output)

if __name__ == "__main__":
    main()
