def make_album(artist, album_title, num_of_tracks = ''):
    album = {'artist': artist, 'album' : album_title}
    if num_of_tracks:
        album['number of tracks'] = int(num_of_tracks)
    return album


artist_1 = make_album('eminem', 'recovery', 12)
artist_2 = make_album('jay-z', 'blueprint')
artist_3 = make_album('morgan wallen', 'if i know me')

print(f"{artist_1} \n{artist_2} \n{artist_3}")


