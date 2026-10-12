import importlib.util
import os
import unittest

script_path = os.path.join(os.path.dirname(__file__), "..", "scripts", "check-discovery-sort.py")
spec = importlib.util.spec_from_file_location("check_discovery_sort", script_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

DiscoverGridParser = module.DiscoverGridParser
extract_grid_slugs = module.extract_grid_slugs
expected_slugs = module.expected_slugs


class TestDiscoverySort(unittest.TestCase):
    def test_old_fixture_with_disc_empty(self):
        html = """
        <html><body>
        <div id="discover-grid" class="disc-grid">
            <a class="disc-card" href="/discover/tool-a/"><h2 class="disc-card-title">A</h2></a>
            <a class="disc-card" href="/discover/tool-b/"><h2 class="disc-card-title">B</h2></a>
        </div>
        <p class="disc-empty">Hiç araç bulunamadı.</p>
        <aside class="disc-cta">Bülten</aside>
        </body></html>
        """
        slugs = extract_grid_slugs(html, "")
        self.assertEqual(slugs, ["tool-a", "tool-b"])

    def test_new_fixture_with_catalog_sidebar(self):
        html = """
        <html><body>
        <div class="catalog-content">
            <div id="discover-grid" class="disc-grid">
                <a class="disc-card" href="/en/discover/tool-1/"><span>1</span></a>
                <a class="disc-card" href="/en/discover/tool-2/"><span>2</span></a>
            </div>
        </div>
        <aside class="catalog-sidebar">
            <h2>Haberdar olun</h2>
        </aside>
        </body></html>
        """
        slugs = extract_grid_slugs(html, "/en")
        self.assertEqual(slugs, ["tool-1", "tool-2"])

    def test_missing_grid_raises_value_error(self):
        html = "<html><body><div>No grid here</div></body></html>"
        with self.assertRaises(ValueError) as ctx:
            extract_grid_slugs(html, "")
        self.assertIn("discovery grid boundary not found", str(ctx.exception))

    def test_expected_slugs_sorts_by_date_and_stars(self):
        catalog = [
            {"slug": "c", "date": "2026-08-01", "stars": 100},
            {"slug": "a", "date": "2026-09-01", "stars": 50},
            {"slug": "b", "date": "2026-09-01", "stars": 200},
        ]
        self.assertEqual(expected_slugs(catalog), ["b", "a", "c"])


if __name__ == "__main__":
    unittest.main()
