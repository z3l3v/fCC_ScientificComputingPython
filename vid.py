import webbrowser

def open_youtube_video(video_id):
    base_url = "https://www.youtube.com/watch?v="
    video_url = base_url + video_id
    webbrowser.open(video_url)

if __name__ == "__main__":
    video_id = input("Enter the YouTube video ID (e.g., 'dQw4w9WgXcQ'): ")
    open_youtube_video(video_id)