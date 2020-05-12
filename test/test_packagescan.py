from distutils.version import LooseVersion

from nicethings.packagescan import PackageScan


def test_processes_html_for_list_of_distribution_names(shared_datadir):
    html = (shared_datadir / "package.html").read_text()
    distributions = PackageScan.scan(html)
    assert distributions

    for distribution in distributions:
        assert "cryptography" in distribution.name.lower()


def test_distribution_info_contains_version_info(shared_datadir):
    html = (shared_datadir / "package.html").read_text()
    distributions = PackageScan.scan(html)

    for distribution in distributions:
        version = distribution.version
        assert version
        assert version > LooseVersion("0.0.0")


def test_all_distributions_are_parsed(shared_datadir):
    html = (shared_datadir / "package.html").read_text()

    from html.parser import HTMLParser

    class HrefCounter(HTMLParser):
        def __init__(self, *, convert_charrefs=True):
            super().__init__(convert_charrefs=convert_charrefs)
            self.hrefs = 0

        def handle_starttag(self, tag, attrs):
            if "a" != tag:
                return

            attrs_dict = dict(attrs)
            if "href" in attrs_dict:
                self.hrefs += 1

    href_counter = HrefCounter()
    href_counter.feed(html)

    distributions = PackageScan.scan(html)
    assert len(distributions) == href_counter.hrefs


def test_distribution_information_includes_links(shared_datadir):
    html = (shared_datadir / "package.html").read_text()
    distributions = PackageScan.scan(html)
    for distribution in distributions:
        import urllib.parse

        urllib.parse.urlparse(distribution.link)
