from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label):
        for idx, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.PHOTOS_PER_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {idx + 1} slot {len(page)}."

        return "No more free slots"

    def display(self):
        separator = '-' * 11
        result = separator + '\n'
        for page in self.photos:
            result += ' '.join('[]' for _ in page) + '\n'
            result += separator + '\n'
        return result.strip()


# album = PhotoAlbum(2)
album = PhotoAlbum(5)

print(album.photos)

print(album.add_photo("photo1"))
print(album.photos)

print(album.add_photo("photo2"))
print(album.photos)

print(album.add_photo("photo3"))
print(album.photos)

print(album.add_photo("photo4"))
print(album.photos)

print(album.add_photo("photo5"))
print(album.photos)

print(album.add_photo("photo6"))
print(album.photos)

print('-------------------------')

print(album.add_photo("photo7"))
print(album.photos)

print(album.add_photo("photo8"))
print(album.photos)

print(album.add_photo("photo9"))
print(album.photos)

print(album.display())
