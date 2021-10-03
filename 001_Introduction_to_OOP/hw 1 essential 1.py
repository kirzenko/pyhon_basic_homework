# Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии, годе
# издания и  жанре. Создайте  несколько  разных  книг. Определите  для  него  операции проверки  на
# равенство и неравенство, методы __repr__ и __str__.

class BookDescription:   # почему равенство не выводится на экран?
    def __init__(self, author, name, year, publication, genre):
        self.author = author
        self.name = name
        self.year = year
        self.publication = publication
        self.genre = genre

    def __eq__(self, other):
        return 'Равенство книг: %s' % (self.author == other.author and self.name == other.name and self.year ==
                                      other.year and self.publication == other.publication and self.genre == other.genre)

    def __repr__(self):
        return 'Информация о книге: ' % {self.author, self.name, self.year, self.publication, self.genre}

    def __str__(self):
        return 'Информация о книге: %s, %s, %s, %s, %s' % (self.author, self.name, self.year, self.publication, self.genre)


def main():
    book_1 = BookDescription('J. London', 'The Call of the Wild', '1990', 'Penguin Random House', 'Adventure')
    print(book_1)
    book_2 = BookDescription('H. Lee', 'To Kill a Mockingbird', '1981', 'Hachette Livre', 'Classics')
    print(book_2)


if __name__ == '__main__':
    main()





