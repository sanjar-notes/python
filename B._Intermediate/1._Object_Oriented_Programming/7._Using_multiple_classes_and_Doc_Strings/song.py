def check_it(object_list, name):
    """Checks if the artist is present using artist_name"""
    for objecti in object_list:
        if objecti.name == name:
            return objecti
    return None

class Song(object):
    """
        Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the songs creator.
        duration (int): The duration of the song in seconds. May be zero.
    """
    def __init__(self, title, artist, duration=0):
        self.name = title
        self.artist = artist
        self.duration = duration

class Album(object):
    """ Class to represent an album, using its track list

    Attributes:
        name(str): The name of the album.
        year(int): The year album was released.
        artist: (Artist): The artist responsible for the album. If not specified,
        the artist will default to an artist with the same name "Various Artists"
        tracks (List[Song]): A list of the songs on the album.

    Methods:
        addSong: Used to add a new song to the album's track list.

    """
    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list

        Args:
            song (Song): A song to add.
            position (Operational[int]): If specified, the song will be added to that positions
            in the track list - inserting it between other songs if necessary.
            Otherwise, the song will be added to the end of the list.
        """
        # we add the OOP approach
        new_song = check_it(self.tracks, song.name)
        if new_song==None:
            if position is None:
                self.tracks.append(song)
            else:
                self.tracks.insert(position, song)
        # else  - do nothing

class Artist:
    """This is a basic class to store artist details.

    Attributes:
        name(str): name of the artist
        albums(List(Album)): A list of albums by this artist
            The list includes only those albums in this collections, it is
            not an exhaustive list if the artist's published albums.

    Methods:
        add_album: Use to add a new album to the artist's albums list
    """
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list.

        Args:
            album (Album): Album object to add to the list.
                If the album is already present, it will not be added again (although this is yet to be implemented).
        """
        self.albums.append(album)

def load_data0():
    store_artist = None
    store_album = None
    artist_list = []

    with open('albums.tsv', 'r') as albums:
        for line in albums:
            # line contains (artist, album, year, song)
            # we need to remove the tabs and newline
            artist_field, album_field, year_field, song_field = tuple(
                line.strip('\n').split('\t'))
            year_field = int(year_field)
            # print('{}:{}:{}:{}'.format(artist_field, album_field, year_field, song_field))

            if store_artist is None:
                store_artist = Artist(artist_field)
            elif store_artist.name != artist_field:
                # we've just read details from new artist
                # store current album in the current artists collection then create a new artist
                store_artist.add_album(store_album)
                artist_list.append(store_artist)
                store_artist = Artist(artist_field)
                store_album = None

            if store_album is None:
                store_album = Album(album_field, year_field, store_artist)
            elif store_album.name != album_field:
                # We've just read a new album for the current artist
                # store the current album in the artist's collection then create a new album object
                store_album.add_song(store_album)
                store_album = Album(album_field, year_field, store_artist)

            # create a new song object and add it to the current album's collection
            new_song = Song(song_field, store_artist)
            store_album.add_song(new_song)

            # After reading the last line of the text file, we will have an artist and album that haven't been stored - process them now
            if store_artist is not None:
                store_artist.add_album(store_album)
            artist_list.append(store_artist)

        return artist_list

def load_data1(source_file='albums.tsv'
               ):  # works - but assumes sorted w.r.t artist and album
    """This function loads the data from the tsv using the given functions

    We proceed as per the data.
    1. Create an artist with no album, do so only if the artist changes(variable needed). Else, don't do anything coz the album object is not ready.
    2. Create an album with artist set to artist from 1. Do so only if the album changes(variable needed). If it doesn't change. Link the album if it has chnaged, to the artist.
    3. Create a song with artist set to artist from 1. This is done for each step regardless of the 1 and 2.
    4. Link all of them properly. Artist and album link should be avoided here.

    A. We can see that there's no need to create the artist and the album object, but we do need to have a song object created each time.
    B. The memory issues, dangling pointers - Python uses references for Data structures, So expanding them won't be a problem.
    C. How objects are expanded(they are not here, we create no instance variables) - That's none of our business. Maybe everything's a reference, that's why it's so dynamic. Typical Pythonic way of doing things.

    Implementation:
        1. We need to have a working variable for keeping track of the artist and album changes and for usual manipulation.
        2. Song object will be created everytime, so it won't need any object like this.
        3. We will need to maintain an artists list - otherwise the objects will be eaten up by the garbage collector, they need to be a part of something alive. That's the artist list that we return eventually.
    """
    # dummy objects to support construction
    store_artist = None
    store_album = None
    artist_list = []

    with open('albums.tsv', 'r') as albums:
        for line in albums:
            # line contains (artist, album, year, song)
            # we need to remove the tabs and newline
            artist_field, album_field, year_field, song_field = tuple(
                line.strip('\n').split('\t'))
            year_field = int(year_field)
            # print('{}:{}:{}:{}'.format(artist_field, album_field, year_field, song_field))

            # create the artist
            if store_artist is None or store_artist.name != artist_field:  # we need to create a new artist in both cases - None checking is inevitable
                store_artist = Artist(artist_field)  # no album attached
                artist_list.append(store_artist)  # storing the artist
            # create the album
            if store_album == None or store_album.name != album_field:
                store_album = Album(album_field, year_field, store_artist)
                store_artist.add_album(store_album)

            # create a new song
            new_song = Song(song_field, store_artist,
                            -1)  # no need of duration

            # link all the things
            store_album.add_song(new_song)  # artist already added
            new_song.artist = store_artist
    return artist_list

def load_data2(source_file='albums.tsv'):
    """This function loads the data from the tsv using the given functions"""
    # dummy objects to support construction
    store_artist = None
    store_album = None
    artist_list = []

    with open('albums.tsv', 'r') as albums:
        for line in albums:
            # line contains (artist, album, year, song)
            # we need to remove the tabs and newline
            artist_field, album_field, year_field, song_field = tuple(
                line.strip('\n').split('\t'))
            year_field = int(year_field)
            # print('{}:{}:{}:{}'.format(artist_field, album_field, year_field, song_field))
            # create the artist

            # check if artists exists in the artist_list - but don't create an artist object
            store_artist = check_it(artist_list, artist_field)
            if store_artist == None:
                store_artist = Artist(artist_field)  # no album attached yet
                artist_list.append(store_artist)  # storing the artist
                store_album = None  # we are assuming that artists and albums have a one-one function
                # we could initialize it here, but it is covered in the code below
            store_album = check_it(store_artist.albums, album_field)
            if store_album == None:
                store_album = Album(album_field, year_field, store_artist)
                store_artist.add_album(store_album)

            new_song = Song(song_field, store_artist, -1)
            store_album.add_song(new_song)  # always added

            # make the song connections
            new_song.artist = store_artist
    return artist_list

def create_checkfile(artist_list, target):
    """Create a check file from the object data for comparison with the original file"""
    with open(target, 'w') as checkfile:
        for store_artist in artist_list:
            for store_album in store_artist.albums:
                for new_song in store_album.tracks:
                    # format same as the existing file
                    print('{0.name}\t{1.name}\t{1.year}\t{2.name}'.format(
                        store_artist, store_album, new_song),
                          file=checkfile)

def check_num():
    artist = ''
    nums = 0
    with open('albums.tsv') as source:
        for row in source.readlines():
            new_artist = row.strip('\n').split('\t')[0]
            if artist != new_artist:
                artist = new_artist
                nums += 1
    return nums

if __name__ == '__main__':
    # artists = load_data1()
    # create_checkfile(artists, 'checkfile1.tsv')
    artists = load_data2()
    create_checkfile(artists, 'checkfile2.tsv')
    # print('There are {} artists.'.format(len(artists)))
    # print(len(load_data0()),len(load_data1()), check_num())
