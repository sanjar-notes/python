# 8. Music Library
Created Tuesday 26 May 2020

![](pasted_image%205.png)

* There exists a circular relationship here, we'll deal with it.
* Our primary data is song tracks which we import in the program using albums.tsv. It contains names of all the fields in the for of a track list.

	artist_name, album_name, year_field, song_field

We have created the classes and the load_data function to get the data from albums.tsv

Approaches:

0. We'll make make the things we can't do hollow/incomplete for the time being.
1. We do it as or the given data. Our goal is to represent the objects in a stable way.
	1. We create an album object if not present in the global albums list(auxilary).
	2. Else we add the song to the album.
	3. ...
	4. We write a method to check if we've written the data correctly.



