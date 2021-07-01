"""A video player class."""

import random
from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_video = None
        self._pause_video = None
        self._current_id = None

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        all_videos = self._video_library.get_all_videos()  # Fetch all the videos, based off above function
        all_videos.sort(key=lambda x: x.title)  # Use key with lambda to dictate sort to only go through video title
        print("Here's a list of all available videos:")

        for video in all_videos:  # Loop through txt file, reading each video line by line
            tagString = str(video.tags)  # Convert to string to allow stripping of brackets, apostrophes and commas
            tagString = tagString.strip("()")
            tagString = tagString.replace("'","")
            tagString = tagString.replace(",","")  
            print(f"{video.title} ({video.video_id}) [{tagString}]")


    def play_video(self, video_id):
        """Plays the respective video.
        
        Args:
            video_id: The video_id to be played.
        """

        video = self._video_library.get_video(video_id) # Fetch information of specific video from video_id
        if not video:
            print("Cannot play video: Video does not exist")
            return

        # self._current_video initialized in constructor
        if self._current_video != None:
            print(f"Stopping video: {self._current_video}")
            print(f"Playing video: {video.title}")
            self._current_video = video.title # current video title updated
            self._pause_video = None # paused video updated
            return

        
        print(f"Playing video: {video.title}")
        self._current_video = video.title
        self._current_id = video_id # current video id updated
        
    def stop_video(self):
        """Stops the current video."""
        current_video = self._current_video

        if current_video:
            print(f"Stopping video: {current_video}")
            self._current_video = None # No video is playing therefore current video is back to None.
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""

        all_videos = [] # empty list
        
        for video in self._video_library.get_all_videos():
            all_videos.append(video.title) # append to list

        # if random video is currently playing
        if self._current_video != None:
            print(f"Stopping video: {self._current_video}")
            self._current_video = random.choice(all_videos) # current random video updated
            print(f"Playing video: {self._current_video}")
            return

        self._current_video = random.choice(all_videos) # current random video updated
        print(f"Playing video: {self._current_video}")

    def pause_video(self):
        """Pauses the current video."""
        pause_video = self._current_video
        
        if not pause_video:
            print("Cannot pause video: No video is currently playing")
            return

        
        # self._pause_video initialized in constructor
        if self._pause_video != None:
            print(f"Video already paused: {pause_video}")
            self._pause_video = pause_video # paused video updated
            return

        
        print(f"Pausing video: {pause_video}")
        self._pause_video = pause_video 
        
    def continue_video(self):
        """Resumes playing the current video."""
        continue_video = self._current_video

        if not continue_video:
            print("Cannot continue video: No video is currently playing")
            return

        
        if not self._pause_video:
            print(f"Cannot continue video: Video is not paused")
            return

        
        print(f"Continuing video: {continue_video}")
        self._pause_video = None # update paused video to None since video is continued

    def show_playing(self):
        """Displays video currently playing."""
        show_playing_video = self._current_video
        if not show_playing_video:
            print("No video is currently playing")
            return

        # Obtaining video information from updated current video id
        video = self._video_library.get_video(self._current_id)
        tagString = str(video.tags)  
        tagString = tagString.strip("()")
        tagString = tagString.replace("'","")
        tagString = tagString.replace(",","")

        
        if self._pause_video != None:
            print(f"Currently playing: {video.title} ({video.video_id}) [{tagString}] - PAUSED")
            return
        
        print(f"Currently playing: {video.title} ({video.video_id}) [{tagString}]")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
