import argparse
from scenedetect import detect, ContentDetector
from tabulate import tabulate

def detect_scenes(input_video):
    # Get the scene list
    scene_list = detect(input_video, ContentDetector())
    
    # Prepare data for tabulation
    scene_table = [[i + 1, str(scene[0]), str(scene[1])] for i, scene in enumerate(scene_list)]
    
    # Display the scene list in a table format
    print(tabulate(scene_table, headers=["Scene #", "Start Time", "End Time"], tablefmt="grid"))

def main():
    parser = argparse.ArgumentParser(description="Detect scenes in a video and display them in tabulated format.")
    parser.add_argument("--input", default="output/openai2.mp4", help="Path to the input video file. Defaults to 'output/openai2.mp4'.")
    args = parser.parse_args()
    
    # Detect scenes and display the result
    detect_scenes(args.input)

if __name__ == "__main__":
    main()
