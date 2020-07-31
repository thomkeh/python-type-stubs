from . import Extension as Extension
from ..preprocessors import Preprocessor as Preprocessor
from typing import Any

log: Any
META_RE: Any
META_MORE_RE: Any
BEGIN_RE: Any
END_RE: Any

class MetaExtension(Extension):
    md: Any = ...
    def extendMarkdown(self, md: Any) -> None: ...
    def reset(self) -> None: ...

class MetaPreprocessor(Preprocessor):
    def run(self, lines: Any): ...

def makeExtension(**kwargs: Any): ...
