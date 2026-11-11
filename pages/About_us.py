class aboutUs:
    def __init__(self, page):
        self.page = page
        self.about_us = page.locator('(//a[@href="https://www.tranktechnologies.com/about"])[1]')


    def about_us_click(self):
        self.about_us.click()
        self.page.wait_for_timeout(2000)  # Wait for 2 seconds to allow the page to load
        self.page.go_back()  # Navigate back to the previous page