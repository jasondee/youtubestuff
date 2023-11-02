import datetime
import os
from googleapiclient.discovery import build

# Set your YouTube Data API key
API_KEY = "AIzaSyBWm-TkHLNptHGcYS0zSTbbhEscfCP10qk"

def search_videos_by_keywords():
    # Create a YouTube API client
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    # Prompt the user for keywords
    keywords = input("Enter keywords for video search: ")

    # Calculate the date 3 months ago from today
    target_date = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y-%m-%dT%H:%M:%SZ')

    # Perform the video search
    search_response = youtube.search().list(
        q=keywords,
        type='video',
        part='snippet',
        maxResults=10,  # You can adjust the number of results as needed
        publishedAfter=target_date
    ).execute()

    # Display the search results with video ID
    for idx, search_result in enumerate(search_response.get('items', []), start=1):
        video_info = search_result['snippet']
        video_title = video_info['title']
        channel_name = video_info['channelTitle']
        video_id = search_result['id']['videoId']  # Extract the video ID
        
        print(f"Result {idx}:")
        print(f"Video Title: {video_title}")
        print(f"Channel Name: {channel_name}")
        print(f"Video ID: {video_id}")  # Display the video ID
        print(f"Publication Date: {target_date}")  # Use target_date for publication date
        print("\n")

    # Iterate through the search results and print video titles and channel names
    for search_result in search_response.get('items', []):
        video_title = search_result['snippet']['title']
        channel_name = search_result['snippet']['channelTitle']
        print(f"Video Title: {video_title}")
        print(f"Channel Name: {channel_name}")
        print("\n")
      
        print("\n")

if __name__ == "__main__":
    search_videos_by_keywords()