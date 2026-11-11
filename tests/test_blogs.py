import pytest
from pages.Blogs import Blogs

@pytest.mark.smoke
def test_blogs_categories(page):
    test_blogs = Blogs(page)
    test_blogs.catogories_click()

