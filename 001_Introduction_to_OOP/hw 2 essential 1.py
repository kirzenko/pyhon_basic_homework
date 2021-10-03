# Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле –  список отзывов. Сделайте
# так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.
class Comment:
    def __init__(self, comment, book):
        self.comment = comment
        self.book = book

    def __str__(self):
        return 'комментарий %s к книге: %s' % (self.comment, self.book)


comment_1 = Comment('My favorite book of this author', 'The Call of the Wild')
comment_2 = Comment('Too boring', 'To Kill a Mockingbird')


class BookDescription:
    def __init__(self, author, name, year, publication, genre, comment):
        self.author = author
        self.name = name
        self.year = year
        self.publication = publication
        self.genre = genre
        self.comment = comment

    def __repr__(self):
        return 'Информация о книге: ' % {self.author, self.name, self.year,
                                         self.publication, self.genre, self.comment}

    def __str__(self):
        return 'Информация о книге: %s, %s, %s, %s, %s, %s' % (self.author, self.name,
                                                               self.year, self.publication, self.genre, self.comment)


def main():
    book_1 = BookDescription('J. London', 'The Call of the Wild', '1990', 'Penguin Random House', 'Adventure', comment_1)
    print(book_1)
    book_2 = BookDescription('H. Lee', 'To Kill a Mockingbird', '1981', 'Hachette Livre', 'Classics', comment_2)
    print(book_2)


if __name__ == '__main__':
    main()









