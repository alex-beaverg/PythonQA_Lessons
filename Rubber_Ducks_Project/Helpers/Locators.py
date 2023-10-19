from selenium.webdriver.common.by import By


class BasePageLocators:
    """Class with locators for Base Page"""
    PAGE_TITLE = (By.CSS_SELECTOR, 'h1.title')


class LoginPageLocators:
    """Class with locators for Login Page"""
    TITLE_OF_LOGIN_BOX = (By.CSS_SELECTOR, '#box-account-login .title')
    INPUT_LOGIN = (By.NAME, 'email')
    INPUT_PASSWORD = (By.NAME, 'password')
    BUTTON_LOGIN = (By.NAME, 'login')
    TEXT_AFTER_LOGIN = (By.CSS_SELECTOR, '.notice.success')


class MainMenuElementLocators:
    """Class with locators for Main Menu Element"""
    MAIN_MENU_ITEM_ELEMENT = (By.CSS_SELECTOR, '#site-menu .category-1 > a')


class RubberDucksPageLocators:
    """Class with locators for Rubber Ducks Page"""
    DUCK = (By.CLASS_NAME, 'name')
    BUTTON_SORT_BY_NAME = (By.CSS_SELECTOR, 'nav.filter>a:first-child')
    STICKER_SALE = (By.CSS_SELECTOR, 'div.sticker.sale')
