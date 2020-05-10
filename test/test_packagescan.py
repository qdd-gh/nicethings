from nicethings.packagescan import PackageScan


def test_processes_html_for_list_of_distribution_names(shared_datadir):
    html = (shared_datadir / "package.html").read_text()
    distributions = PackageScan.scan(html)
    assert distributions

    for distribution in distributions:
        assert "cryptography" in distribution.name.lower()
