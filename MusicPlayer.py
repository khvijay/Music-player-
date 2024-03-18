class MusicPlayer:
    def __init__(self):
        self.playlist = []

    def add_song(self, song):
        self.playlist.append(song)

    def remove_song(self, song):
        if song in self.playlist:
            self.playlist.remove(song)
            print(f"{song} has been removed from the playlist.")
        else:
            print(f"{song} is not in the playlist.")

    def play(self):
        if self.playlist:
            print("Playing music:")
            for song in self.playlist:
                print(song)
        else:
            print("No songs in the playlist. Please add songs first.")

def main():
    player = MusicPlayer()
    while True:
        print("1. Add Song")
        print("2. Remove Song")
        print("3. Play")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            song = input("Enter the song name: ")
            player.add_song(song)
        elif choice == "2":
            song = input("Enter the song name to remove: ")
            player.remove_song(song)
        elif choice == "3":
            player.play()
        elif choice == "4":
            print("Thank you for using the Music Player. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
