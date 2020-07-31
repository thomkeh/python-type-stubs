from . import Extension as Extension
from ..inlinepatterns import InlineProcessor as InlineProcessor
from typing import Any

def build_url(label: Any, base: Any, end: Any): ...

class WikiLinkExtension(Extension):
    config: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...
    md: Any = ...
    def extendMarkdown(self, md: Any) -> None: ...

class WikiLinksInlineProcessor(InlineProcessor):
    config: Any = ...
    def __init__(self, pattern: Any, config: Any) -> None: ...
    def handleMatch(self, m: Any, data: Any): ...

def makeExtension(**kwargs: Any): ...
