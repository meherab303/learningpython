def make_album(artist_name, album_title, num_songs=None):
    
    album = {
        'artist': artist_name,
        'title': album_title,
    }
    if num_songs:
        album['num_songs'] = num_songs
    return album


album1 = make_album('Taylor Swift', '1989')
album2 = make_album('Ed Sheeran', 'Divide')
album3 = make_album('Adele', '30', num_songs=12)

print(album1)
print(album2)
print(album3)

def make_car(manufacturer, model, **kwargs):
   
    car = {
        'manufacturer': manufacturer,
        'model': model,
    }
   
    car.update(kwargs)
    return car


car = make_car('subaru', 'outback', color='blue', tow_package=True)


print(car)
