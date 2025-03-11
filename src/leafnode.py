from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag is None or self.tag == "":
            return f"{self.value}"
        elif self.value is None or self.value == "":
            return f"<{self.tag}{self.props_to_html()} />"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"