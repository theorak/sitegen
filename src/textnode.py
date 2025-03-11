from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    ITALIC2 = "italic2"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextTypeDelimiters(Enum):    
    BOLD = "**",
    ITALIC = "*",
    ITALIC2 = "_",
    CODE = "`"
    PATTERN = r"(\*\*.*?\*\*|\*.*?\*|_.*?_|`.*?`)"

class TextNode():    
    def __init__(self, text: str, text_type: TextType, url:str = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, value):
        if not isinstance(value,TextNode):
            return False
        return self.text == value.text and self.text_type == value.text_type and self.url == value.url
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"