class verticals:
    def __init__(self, page):
        self.page = page
        self.vertical = page.locator('(//a[text()="Verticals"])[1]')

         # Verticals_Navigation
        self.vertical_tab = self.page.locator('(//a[text()="Verticals"])[1]')

    
        # Trading
        self.vertical_trading = self.page.locator('//strong[text()="Trading"]')
        self.vertical_stock   = self.page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.algo_trading     = self.page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.paper_trading    = self.page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.cus_trading      = self.page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.cfd_trading      = self.page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.web_trading      = self.page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
        self.app_trading      = self.page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')

        self.trading_list = [self.vertical_stock, self.algo_trading, self.paper_trading, self.cus_trading, self.cfd_trading, self.web_trading, self.app_trading]

    def trading_option_click(self):
        for option in self.trading_list:
            self.vertical_tab.hover()
            self.page.wait_for_timeout(1000)  # Wait for 1 second to ensure the hover effect is applied
            self.vertical_trading.hover()
            self.page.wait_for_timeout(2000)  # Wait for 1 second to ensure
            option.click()
            self.page.wait_for_timeout(2000)  # Wait for 2 seconds to allow the page to load
            self.page.go_back()