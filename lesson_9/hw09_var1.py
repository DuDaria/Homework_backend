class Tag:
    def __init__(self, tag_name):
        self.tag_name = tag_name


class TagFactory:
    def create_tag(self, tag, format):
        tags = get_html(format)
        return tags(tag)


def get_html(format):
    if format == 'image':
        return _tag_image
    elif format == 'input':
        return _tag_input
    elif format == 'p':
        return _tag_p
    elif format == 'a':
        return _tag_a
    else:
        raise ValueError(format)

def _tag_image(tag):
    return (f"<{tag.tag_name}></{tag.tag_name}>")

def _tag_input(tag):
    return f"<{tag.tag_name}></{tag.tag_name}>"

def _tag_p(tag):
    return f"<{tag.tag_name}></{tag.tag_name}>"

def _tag_a(tag):
    return f"<{tag.tag_name}></{tag.tag_name}>"



if __name__ == "__main__":

    factory = TagFactory()

    elements = ['image', 'input', 'p', 'a']

    for el in elements:
        tag = Tag(el)
        print(factory.create_tag(tag, el))
