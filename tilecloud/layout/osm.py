import re
from typing import Any, Match, Optional

from tilecloud import TileCoord
from tilecloud.layout.re_ import RETileLayout


class OSMTileLayout(RETileLayout):
    """
    OpenStreetMap tile layout.
    """

    PATTERN = r"[0-9]+/[0-9]+/[0-9]+"
    RE = re.compile(r"([0-9]+)/([0-9]+)/([0-9]+)\Z")

    def __init__(self) -> None:
        RETileLayout.__init__(self, self.PATTERN, self.RE)

    @staticmethod
    def filename(tilecoord: TileCoord, metadata: Optional[Any] = None) -> str:
        return f"{tilecoord.z}/{tilecoord.x}/{tilecoord.y}"

    @staticmethod
    def _tilecoord(match: Match[str]) -> TileCoord:
        return TileCoord(*map(int, match.groups()))
