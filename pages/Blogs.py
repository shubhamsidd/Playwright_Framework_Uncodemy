class Blogs:
    def __init__(self, page):
        self.page = page
        self.blogs_link = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')

        # catogories
        cat_app_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/app-development/"])[2]')
        cat_AI = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/artificial-intelligence/"])[1]')
        cat_CM = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/content-marketing/"])[1]')
        cat_CRM = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/crm-development/"])[1]')
        cat_DM = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/digital-marketing/"])[1]')
        cat_ecomm = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ecommerce-development/"])[5]')
        cat_email_marketing = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/email-marketing/"])[1]')
        cat_graphic_design = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/graphic-design/"])[3]')
        cat_softwareIT = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/software-it-company/"])[1]')
        cat__software_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/software-development/"])[1]')
        cat_UI_UX = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ui-ux-design/"])[5]')
        cat_web_dev = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/web-development/"])[5]')

        self.cat_list = [cat_app_dev, cat_AI, cat_CM, cat_CRM, cat_DM, cat_ecomm, cat_email_marketing, cat_graphic_design,
                    cat_softwareIT, cat__software_dev, cat_UI_UX, cat_web_dev]
        
    def catogories_click(self):
        for cat in self.cat_list:
            self.blogs_link.click()
            self.page.wait_for_timeout(2000)
            cat.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()
            self.page.wait_for_timeout(2000)
            self.page.go_back()