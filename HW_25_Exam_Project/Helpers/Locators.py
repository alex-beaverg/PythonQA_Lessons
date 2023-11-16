from selenium.webdriver.common.by import By


class BasePageLocators:
    """Class with locators for "Base" page"""
    PAGE_TITLE = (By.CSS_SELECTOR, '#region_2_default > div:nth-child(2) > h1')


class MainPageLocators:
    """Class with locators for "Main" page"""
    MAIN_PAGE_TITLE = (By.CSS_SELECTOR, '#__tab_Tabs_2421_ctl00')


class MainMenuElementLocators:
    """Class with locators for "Main Menu" element"""
    ONE_WINDOW = (By.CSS_SELECTOR, "#h_menu > ul > li:nth-child(1) > a")
    ABOUT = (By.CSS_SELECTOR, "#h_menu > ul > li:nth-child(2) > a")
    TEACHERS_ROOM = (By.CSS_SELECTOR, "#h_menu > ul > li:nth-child(3) > a")
    PUPILS = (By.CSS_SELECTOR, "#h_menu > ul > li:nth-child(4) > a")
    GRADUATES = (By.CSS_SELECTOR, "#h_menu > ul > li:nth-child(5) > a")


class OneWindowSubMenuElementLocators:
    """Class with locators for "Main" menu sub-item "One window" items element"""
    SCHEDULE = (By.CSS_SELECTOR, "#h_menu > ul > li:nth-child(1) > ul > li:nth-child(1) > a")
    PROCEDURES = (By.CSS_SELECTOR, "#h_menu > ul > li:nth-child(1) > ul > li:nth-child(2) > a")


class AboutSubMenuElementLocators:
    """Class with locators for "Main" menu sub-item "About" items element"""
    GOALS_AND_TASKS = (By.CSS_SELECTOR, "#h_menu > ul > li:nth-child(2) > ul > li:nth-child(1) > a")
    HISTORY_AND_TRADITIONS = (By.CSS_SELECTOR, "#h_menu > ul > li:nth-child(2) > ul > li:nth-child(2) > a")
