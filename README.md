# Introduction
This is a set of utilities to help with videos

## dowload a youtube video
the followig will allow you to dowload a video as an mp4

```bash
python download_youtube.py --input "https://youtu.be/_iETa2KDRuw?si=D2xgXWkt5bss9Mq-"
```

## detect scenes in a vidoe
the following will print a list of scenes in a video

```bash
python scene_detect.py --input output/openai2.mp4
```

## Pre-Requisities
You will need the following installed

### ffmpeg
this can be installed with the following command

```bash
brew install ffmpeg
```

### scendetect
you will need to install scenedetect as a package

```bash
pip install -r requirements.txt
```