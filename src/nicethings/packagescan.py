from distutils.version import LooseVersion
from html.parser import HTMLParser
from typing import List

import attr


@attr.s(auto_attribs=True)
class Distribution:
    name: str = ""
    link: str = ""
    version: LooseVersion = None


class PackageHtmlParser(HTMLParser):
    def __init__(self, *, convert_charrefs=True):
        super().__init__(convert_charrefs=convert_charrefs)
        self.current_link = ""
        self.distributions = []

    def handle_starttag(self, tag, attrs):

        if "a" != tag:
            return

        attrs_dict = dict(attrs)
        self.current_link = attrs_dict["href"]

    def handle_data(self, data):
        if not self.current_link:
            return

        name = data.split("-")[0]
        version = data.replace(name + "-", "")
        version = LooseVersion(version)
        dist = Distribution(name=data, link=self.current_link, version=version)
        self.distributions.append(dist)
        self.current_link = ""


class PackageScan:
    @classmethod
    def scan(cls, html: str) -> List[Distribution]:
        parser = PackageHtmlParser()
        parser.feed(html)
        return parser.distributions
