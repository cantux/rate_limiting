"""
We are building a cloud-based music player, like Spotify.
Let's start with the following functionality:

* `add_song (song_title [string])`
   - A song is given an incremental integer ID when it's added, starting with 1


* `play_song (song_id [integer], user_id [integer])`
   - Assume any user ID is valid, and that the given song ID will have been added


* `print_analytics_summary ()`
   - This is used for a report, created once per day for our company's Analytics department.
   - The summary should be sorted (descending) by the number of unique users who have played each song.
   - The summary should include the song titles, and the number of unique users, but the formatting does not matter.

For our MVP, consider performance as we will eventually support millions of songs and users.
However, let's not worry about thread safety or persistence for now - store data in memory.
"""


# song_ids = {}
# for i, s in enumerate(songs):
#     song_ids[i] = s

# song_plays = defaultdict(set)
# for frm, to in song_plays:
#     song_plays[frm].add(to)

# return [str(song_ids[k]) + " has been played by "  + str(len(v) + " unique users" for k, v in song_plays]

"""
We now want to allow users to see their most recently played songs.
Let's implement the following function:
* `last_three_played_song_titles (user_id [integer])`
   - Returns the titles of the last three unique played songs for the given user (ordered, most recent first)
Let's prioritize solving the problem for the last three played songs for now.
We can tackle extensibility at a later stage.
After running the new function with the plays from the previous example,

the summary should output as follows for user ID 1 (in order):

Hello, Goodbye
Stairway to Heaven
Bohemian Rhapsody
"""

from collections import defaultdict, deque

class Library:
    counter = 1
    def __init__(self):
        self.song_ids = {}
        self.song_plays = defaultdict(set)
        self.user_last_played_id_to_set_mp = defaultdict(set)
        self.user_last_played_id_to_deque_mp = defaultdict(deque)
        
    def last_three_played_song_titles(self, user_id):
        print("\n".join(
            [
                self.song_ids[song_id] for song_id in reversed(self.user_last_played_id_to_deque_mp[user_id])
            ]
            )
        )
        
    def play_song(self, song_id, user_id):
        ## note handle user don't exist
        if song_id not in self.user_last_played_id_to_set_mp[user_id]:
            if len(self.user_last_played_id_to_deque_mp[user_id]) == 3:
                removed_song_id = self.user_last_played_id_to_deque_mp[user_id].popleft()
                self.user_last_played_id_to_set_mp[user_id].remove(removed_song_id)
            self.user_last_played_id_to_deque_mp[user_id].append(song_id)
            self.user_last_played_id_to_set_mp[user_id].add(song_id)
        self.song_plays[song_id].add(user_id)
        
    def add_song(self, song_name):
        curr_song_id = Library.counter
        self.song_ids[curr_song_id] = song_name
        self.song_plays[curr_song_id] = set()
        Library.counter += 1

        
    def print_analytics_summary(self):
        id_len_sorted_lst = sorted( [
                    (
                        str(len(user_id_set)), str(self.song_ids[song_id])
                    ) for song_id, user_id_set in self.song_plays.items()
                ], reverse=True
            )
        print("\n".join([
                song_name + " has been played by " + user_id_set_length + " unique users" 
                    for user_id_set_length, song_name  in id_len_sorted_lst
            ]))


library = Library()
library.add_song("Hello, Goodbye")
library.add_song("Bohemian Rhapsody")
library.add_song("Stairway to Heaven")
library.add_song("Satisfaction")
library.add_song("Pinball Wizard")

# library.play_song(1, 9)
# library.play_song(2, 14)
# library.play_song(1, 2)
# library.play_song(1, 1)
# library.play_song(2, 1)
# library.play_song(3, 17)
# library.play_song(2, 1)
# library.play_song(3, 5)
# library.play_song(2, 1)
# library.play_song(2, 1)
# library.play_song(1, 7)
# library.play_song(4, 1)
# library.play_song(2, 1)
# library.play_song(1, 1)
# library.play_song(1, 1)
# library.play_song(3, 1)
# library.play_song(1, 1)

library.print_analytics_summary() # O(songname lg(songname))

library.play_song(2, 1) # bohemian
library.play_song(1, 1)
library.play_song(1, 1)
library.play_song(3, 1) # stairway
library.play_song(1, 1) # Hello  
library.last_three_played_song_titles(1)
"""
Expected output:
* "Hello, Goodbye" has been played by 4 unique users
* "Stairway to Heaven" has been played by 3 unique users
* "Bohemian Rhapsody" has been played by 2 unique users
* "Satisfaction" has been played by 1 unique user
* "Pinball Wizard" has been played by 0 unique users

You may look up syntax using a search engine or AI assistant, as long as you are sharing your screen.
"""

