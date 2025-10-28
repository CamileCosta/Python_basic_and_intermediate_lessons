liked_songs = {
    'Remind Me': 'Chase Atlantic',
    'Espresso': 'Sabrina Carpenter',
    'Heartbreak': 'Justin Bieber',
    'Angel': 'Massive Attack'
}

def write_liked_songs_to_file(liked_songs, file_name):
    with open(file_name, 'w') as file:
        file.write('Liked songs: \n')
        for key, value in liked_songs.items():
            file.write(f"{key}: {value}\n")


write_liked_songs_to_file(liked_songs, 'liked_songs.txt')