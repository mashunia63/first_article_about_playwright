from playwright.sync_api import Page
import config


class IndexPage:
    _BUTTON_GOOGLE_SEARCH = "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b"
    _LINK_ENGLISH_LANG = "//a[contains(text(), 'English')]"

    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    def press_link_english_lang(self, page: Page):
        page.locator(self._LINK_ENGLISH_LANG).click()

    def get_text_from_google_search_button (self,page:Page) -> None:
        return page.locator(self._BUTTON_GOOGLE_SEARCH).get_attribute('value')

