# Создайте  класс  Editor,  который  содержит  методы  view_document  и  edit_document.  Пусть  метод
# edit_document выводит на экран информацию о том, что редактирование документов недоступно для
# бесплатной  версии.  Создайте  подкласс  ProEditor,  в  котором  данный  метод  будет  переопределён.
# Введите с клавиатуры лицензионный ключ и, если он корректный, создайте экземпляр класса ProEditor,
# иначе Editor. Вызовите методы просмотра и редактирования документов.

class Editor:
    def view_document(self):
        print('просмотр документа')

    def edit_document(self):
        print('редактирование документов недоступно для бесплатной  версии')


class ProEditor(Editor):
    def edit_document(self):
        print('вы можете редактировать документ')


def main():
    editor = Editor()
    proedit = ProEditor()

    editor.view_document()
    editor.edit_document()

    key = input('введите пароль для платной версии: ')
    if key == '1111':
        proedit.edit_document()
    else:
        print('пароль неверный')
        editor.edit_document()


if __name__ == '__main__':
    main()


'''class Editor:
    def book_operation(self, doc_1, view_document, edit_document):
        if view_document:
            return print(doc_1)


class ProEditor(Editor):
    def book_operation(self, doc_1, view_document, edit_document):
        if view_document:
            parent_class_editor = super()
            result = parent_class_editor.book_operation(doc_1, view_document, edit_document)
            return result
        elif edit_document:
            while True:
                key = input('Операция доступна в платной версии ProEditor, введите ключ:')
                if key == '1111':
                    return print('Редактирование документа', doc_1)


def main():

    editor = ProEditor()
    editor.book_operation('document', view_document=True, edit_document=False)
    editor.book_operation('document', edit_document=True, view_document=False)
    '''



