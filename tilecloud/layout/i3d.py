import re
from typing import Dict, Match, Optional

from tilecloud import TileCoord
from tilecloud.layout.re_ import RETileLayout


class I3DTileLayout(RETileLayout):
    """
    I3D (FHNW/OpenWebGlobe) tile layout.
    """

    PATTERN = r"(?:[0-3]{2}/)*[0-3]{1,2}"
    RE = re.compile(PATTERN + r"\Z")

    def __init__(self) -> None:
        RETileLayout.__init__(self, self.PATTERN, self.RE)

    @staticmethod
    def filename(tilecoord: TileCoord, metadata: Optional[Dict[str, str]] = None) -> str:
        return "/".join(re.findall(r"[0-3]{1,2}", I3DTileLayout.quadcode_from_tilecoord(tilecoord)))

    @staticmethod
    def _tilecoord(match: Match[str]) -> TileCoord:
        return I3DTileLayout.tilecoord_from_quadcode(re.sub(r"/", "", match.group()))

    @staticmethod
    def quadcode_from_tilecoord(tilecoord: TileCoord) -> str:
        x, y = int(tilecoord.x), int(tilecoord.y)
        result = ""
        for _ in range(0, tilecoord.z):
            result += "0123"[(x & 1) + ((y & 1) << 1)]
            x >>= 1
            y >>= 1
        return result[::-1]

    @staticmethod
    def tilecoord_from_quadcode(quadcode: str) -> TileCoord:
        z, x, y = len(quadcode), 0, 0
        for i, c in enumerate(quadcode):
            mask = 1 << (z - i - 1)
            if c in ["1", "3"]:
                x |= mask
            if c in ["2", "3"]:
                y |= mask
        return TileCoord(z, x, y)
