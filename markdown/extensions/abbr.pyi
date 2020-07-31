from . import Extension as Extension
from ..inlinepatterns import InlineProcessor as InlineProcessor
from ..preprocessors import Preprocessor as Preprocessor
from ..util import AtomicString as AtomicString
from typing import Any

ABBR_REF_RE: Any

class AbbrExtension(Extension):
    def extendMarkdown(self, md: Any) -> None: ...

class AbbrPreprocessor(Preprocessor):
    def run(self, lines: Any): ...

class AbbrInlineProcessor(InlineProcessor):
    title: Any = ...
    def __init__(self, pattern: Any, title: Any) -> None: ...
    def handleMatch(self, m: Any, data: Any): ...

def makeExtension(**kwargs: Any): ...
