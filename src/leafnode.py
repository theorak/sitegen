from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None):
        super().__init__(tag, value, None, props)
        if self.value is None or self.value == "":
            raise ValueError(self)

    def to_html(self):
        if self.value is None or self.value == "":
            raise ValueError(self)
        elif self.tag is None or self.tag == "":
            return f"{self.value}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"