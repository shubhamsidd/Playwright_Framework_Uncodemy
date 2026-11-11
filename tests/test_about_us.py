import pytest
from pages.About_us import aboutUs


@pytest.mark.smoke
def test_about_us(page):
    about_us_page = aboutUs(page)
    about_us_page.about_us_click()