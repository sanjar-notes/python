class Tag(object): # everything is actually done using a tag, the basic building block

    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents  # a collection of other elements

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)

# This class is actually an example of IS A relationship.
# IS A and HAS A are not necessarily exclusive, they can be used together.
class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = '' # no closing tag


class Body(Tag):

    def __init__(self):
        super().__init__('body', '')
        self._body_contents = []
        # we assume the body is empty, for now.

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents) # a generic tag, not a special tag like body
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents: # each tag is a generic tag, and has a print method
            self.contents += str(tag) # as contents is a string, we need it to get all the list elements

        #print the content using the super(), to avoid infinite loop
        super().display(file=file)   # prints the content


class HtmlDoc(object):

    def __init__(self, titlename=None): #challenge
        self._doc_type = DocType()
        self._body = Body()
        ###########Challenge line below
        self._head = Head(title=titlename)
        # Composition does not imply that we should use only the constituents, we can have our own things too.

    def add_tag(self, name, contents): # we give it the same name - for regularity - i.e ploymorphism
        self._body.add_tag(name, contents) # body class has an add_tag method - delegated

    def display(self, file=None):  # everything is deligated - showing polymorphism
        print('<html>', file=file)

        # print the doc
        self._doc_type.display(file=file)

        # print the head tag
        self._head.display(file=file)

        # print the body
        self._body.display(file=file)

        print('<html>', file=file)

# ================> Challenge
# making a new header - to include the title tag
# for this we first need a Title Tag, IS A.

class Title(Tag):

    def __init__(self, contents):   # we only need the content
        if contents == None:
            contents = 'Untitled Page'
        super().__init__('title', contents) # creates the tag with name title

    # no need of display, Tags display is okay

# now make the head tag, composing of title
class Head(Tag):

    def __init__(self, title=None): # the head tag doesn't have content
        super().__init__('head', '')
        self._title_tag = Title(title) # title may be undefined

    # def add_title(self, titlename):
    #     new_title = Title(titlename)
    #     self._title_tag = new_title

    def display(self, file=None):
        self.contents = str(self._title_tag)
        super().display(file=file)


#========================>
if __name__ == '__main__':
        mypage = HtmlDoc()
        mypage.add_tag('h1', 'Main heading')
        mypage.add_tag('h2', 'sub-heading')
        mypage.add_tag('p', 'This is a paragraph, set to appear on the page')
        # mypage.display()
        with open('challenge.html', 'w') as output:
            mypage.display(file=output)
