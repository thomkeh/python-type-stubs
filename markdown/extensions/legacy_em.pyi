from . import Extension as Extension
from ..inlinepatterns import EM_STRONG2_RE as EM_STRONG2_RE, EmStrongItem as EmStrongItem, STRONG_EM2_RE as STRONG_EM2_RE, UnderscoreProcessor as UnderscoreProcessor
from typing import Any

EMPHASIS_RE: str
STRONG_RE: str
STRONG_EM_RE: str

class LegacyUnderscoreProcessor(UnderscoreProcessor):
    PATTERNS: Any = ...

class LegacyEmExtension(Extension):
    def extendMarkdown(self, md: Any) -> None: ...

def makeExtension(**kwargs: Any): ...
