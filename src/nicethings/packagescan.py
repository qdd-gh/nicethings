from typing import List

import attr


@attr.s(auto_attribs=True, frozen=True)
class Distribution:
    name: str = ""
    link: str = ""


class PackageScan:

    @classmethod
    def scan(cls, html: str) -> List[Distribution]:
        return [Distribution(name="cryptography", link="example.com")]
