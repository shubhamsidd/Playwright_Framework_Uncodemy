import pytest
from pages.vertical import verticals


@pytest.mark.smoke
def test_trading_options(page):
    vertical_page = verticals(page)
    vertical_page.trading_option_click()