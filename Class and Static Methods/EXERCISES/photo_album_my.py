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
        for idx, curr_photos_per_page in enumerate(self.photos):
            if len(curr_photos_per_page) < PhotoAlbum.PHOTOS_PER_PAGE:
                self.photos[idx].append(label)
                return (f"{label} photo added successfully on page "
                        f"{idx + 1} slot {len(self.photos[idx])}")

        return "No more free slots"

    def display(self):
        separator = '-' * 11
        result = separator
        result += '\n'
        for elements in self.photos:
            result += ' '.join(['[]' for el in elements]) + '\n' + separator + '\n'

        return result.strip()


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
