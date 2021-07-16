"""Special handler for dev."""
from typing import Optional

from .sections import AwesomeVersionCompareHandlerSections


class AwesomeVersionCompareHandlerDevRc(AwesomeVersionCompareHandlerSections):
    """AwesomeVersionCompareHandlerDevRc class."""

    def handler(self) -> Optional[bool]:
        """Compare handler."""
        a_last = self.version_a.string.split(".")[-1]
        b_last = self.version_b.string.split(".")[-1]
        if (not a_last.startswith("dev") and b_last.startswith("dev")) or (
            not a_last.startswith("rc") and b_last.startswith("rc")
        ):
            self.version_b._version = self.version_b.string.replace(f".{b_last}", "")
            if self.version_a.string == self.version_b.string:
                return True
            if self._compare_base_sections(self.version_a, self.version_b) is None:
                return True
