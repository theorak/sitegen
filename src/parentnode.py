from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict = None):        
        super().__init__(tag, None, children, props)
        if self.tag is None or self.tag == "":
            raise ValueError(self)
        if self.children is None or self.children == []:
            raise ValueError(self)

    def to_html(self):
        if self.tag is None or self.tag == "":
            raise ValueError(self)
        if self.children is None or self.children == []:
            raise ValueError(self)
        
        child_html = ""
        for child in self.children:
           child_html += child.to_html()
        return f"<{self.tag}>{child_html}</{self.tag}>"