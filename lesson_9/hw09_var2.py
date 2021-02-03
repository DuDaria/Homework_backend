
class Factory():
    def create_tag(self, tag_name):
        # параметризованный фабричный метод `create_tag`
        raise NotImplementedError()


class TagFactory(Factory):
    def create_tag(self, tag_name):
        if tag_name == 'image':
            return TagImage()
        elif tag_name == 'input':
            return TagInput()
        elif tag_name == 'p':
            return TagP()
        elif tag_name == 'a':
            return TagA()
        else:
            raise AttributeError("Ошибка атрибута")


class Tag():
    def get_html(self):
        raise NotImplementedError()


class TagImage(Tag):
    def get_html(self):
        print('<image></image>')


class TagInput(Tag):
    def get_html(self):
        print('<input></input>')


class TagP(Tag):
    def get_html(self):
        print('<p></p>')


class TagA(Tag):
    def get_html(self):
        print('<a></a>')


if __name__ == "__main__":

    factory = TagFactory()

    elements = ['image', 'input', 'p', 'a']

    for el in elements:
        factory.create_tag(el).get_html() 
        # print(factory.create_tag(el))
