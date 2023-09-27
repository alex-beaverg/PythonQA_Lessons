# Homework 18 - (2023.09.26)
# Homework -> Alerts, Frames, Windows, Shadow DOM and HTML5 Elements
# Run configuration -> Current File
# Run: Shift + F10

import unittest

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChromeDriverSingleton(webdriver.Chrome):
    """Docstring: Class singleton ChromeWebDriver"""

    def __new__(cls):
        """Docstring: Special constructor for singleton class ChromeWebDriver"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(ChromeDriverSingleton, cls).__new__(cls)
        return cls.instance


class TestClass(unittest.TestCase):
    """Docstring: Test class"""

    def setUp(self) -> None:
        """Docstring: Setup method before every test"""
        self.setWebdriver()
        self.webdriverSetUp()
        self.pageUrls()
        self.setTestsParameters()

    def setWebdriver(self) -> None:
        """Docstring: Set webdriver setup method"""
        self.driver = ChromeDriverSingleton()

    def webdriverSetUp(self) -> None:
        """Docstring: Webdriver setup method"""
        self.timeout = 5
        self.driver.maximize_window()
        self.driver.implicitly_wait(self.timeout)

    def pageUrls(self) -> None:
        """Docstring: Page setup method"""
        self.page_url = 'https://the-internet.herokuapp.com/'
        self.page_url_canvas = 'https://canvas.apps.chrome/'
        self.page_url_video = 'https://www.w3schools.com/html/html5_video.asp'
        self.page_url_web_storage = 'https://mdn.github.io/dom-examples/web-storage/'

    def setTestsParameters(self) -> None:
        """Docstring: Method to set parameters to all tests"""
        self.setLocators()
        self.setVariables()

    def setLocators(self) -> None:
        """Docstring: Set locators method"""
        self.alerts_link_text = 'JavaScript Alerts'
        self.alert_css_selector = '#content>div>ul>li:nth-child(1)>button'
        self.confirm_css_selector = '#content>div>ul>li:nth-child(2)>button'
        self.prompt_css_selector = '#content>div>ul>li:nth-child(3)>button'
        self.result_id = 'result'
        self.frames_link_text = 'Frames'
        self.iframe_link_text = 'iFrame'
        self.iframe_id = 'mce_0_ifr'
        self.iframe_textarea_css_selector = '#tinymce>p'
        self.windows_link_text = 'Multiple Windows'
        self.new_window_link_text = 'Click Here'
        self.new_window_tag = 'h3'
        self.shadow_dom_link_text = 'Shadow DOM'
        self.shadow_dom_css_selector = '#content>my-paragraph:nth-child(5)'
        self.shadow_dom_content_css_selector = 'p>slot'
        self.canvas_shadow_dom1_id = 'drawing-app'
        self.canvas_shadow_dom2_css_selector = 'welcome-dialog'
        self.canvas_shadow_dom2_btn_css_selector = 'ea-button#get-started'
        self.drawing_canvas_css_selector = 'drawing-canvas'
        self.ink_engine_id = 'ink-canvas'
        self.video_id = 'video1'
        self.bg_color_id = 'bgcolor'

    def setVariables(self) -> None:
        """Docstring: Set variables method"""
        self.expected_alert_text = 'I am a JS Alert'
        self.expected_alert_result = 'You successfully clicked an alert'
        self.expected_confirm_text = 'I am a JS Confirm'
        self.expected_confirm_result = 'You clicked: Ok'
        self.expected_prompt_text = 'I am a JS prompt'
        self.text_to_prompt = 'Hello!'
        self.expected_prompt_result = 'You entered: Hello!'
        self.expected_iframe_text = 'Your content goes here.'
        self.expected_new_window_text = 'New Window'
        self.expected_shadow_dom_text = 'My default text'
        self.expected_duration = 10
        self.expected_source = 'https://www.w3schools.com/html/mov_bbb.mp4'

    def tearDown(self) -> None:
        """Docstring: Teardown method after every test"""
        self.driver.quit()

    def following_the_link(self, link_text: str) -> None:
        """Docstring: Method to follow the link"""
        self.driver.find_element(By.LINK_TEXT, link_text).click()

    def test_01_alert_simple(self) -> None:
        """Docstring: Test 01 (JS alert)"""
        self.driver.get(self.page_url)
        self.following_the_link(self.alerts_link_text)
        self.alert_button = self.driver.find_element(By.CSS_SELECTOR, self.alert_css_selector)
        self.alert_button.click()
        self.assertEqual(self.expected_alert_text, Alert(self.driver).text)
        Alert(self.driver).accept()
        self.alert_result_text = self.driver.find_element(By.ID, self.result_id).text
        self.assertEqual(self.expected_alert_result, self.alert_result_text)

    def test_02_alert_confirm(self) -> None:
        """Docstring: Test 02 (JS confirm alert)"""
        self.driver.get(self.page_url)
        self.following_the_link(self.alerts_link_text)
        self.confirm_button = self.driver.find_element(By.CSS_SELECTOR, self.confirm_css_selector)
        self.confirm_button.click()
        self.assertEqual(self.expected_confirm_text, Alert(self.driver).text)
        Alert(self.driver).accept()
        self.confirm_result_text = self.driver.find_element(By.ID, self.result_id).text
        self.assertEqual(self.expected_confirm_result, self.confirm_result_text)

    def test_03_alert_prompt(self) -> None:
        """Docstring: Test 03 (JS prompt alert)"""
        self.driver.get(self.page_url)
        self.following_the_link(self.alerts_link_text)
        self.prompt_button = self.driver.find_element(By.CSS_SELECTOR, self.prompt_css_selector)
        self.prompt_button.click()
        self.assertEqual(self.expected_prompt_text, Alert(self.driver).text)
        Alert(self.driver).send_keys(self.text_to_prompt)
        Alert(self.driver).accept()
        self.prompt_result_text = self.driver.find_element(By.ID, self.result_id).text
        self.assertEqual(self.expected_prompt_result, self.prompt_result_text)

    def test_04_frames(self) -> None:
        """Docstring: Test 04 (Frames)"""
        self.driver.get(self.page_url)
        self.following_the_link(self.frames_link_text)
        self.iframe_link = self.driver.find_element(By.LINK_TEXT, self.iframe_link_text)
        self.iframe_link.click()
        self.iframe_element = self.driver.find_element(By.ID, self.iframe_id)
        self.driver.switch_to.frame(self.iframe_element)
        self.iframe_text = self.driver.find_element(By.CSS_SELECTOR, self.iframe_textarea_css_selector).text
        self.assertEqual(self.expected_iframe_text, self.iframe_text)

    def test_05_windows(self) -> None:
        """Docstring: Test 05 (Windows)"""
        self.driver.get(self.page_url)
        self.following_the_link(self.windows_link_text)
        self.new_window_link = self.driver.find_element(By.LINK_TEXT, self.new_window_link_text)
        self.new_window_link.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.new_window_text = self.driver.find_element(By.TAG_NAME, self.new_window_tag).text
        self.assertEqual(self.expected_new_window_text, self.new_window_text)

    def test_06_shadow_dom(self) -> None:
        """Docstring: Test 06 (Shadow DOM)"""
        self.driver.get(self.page_url)
        self.following_the_link(self.shadow_dom_link_text)
        self.shadow_host = self.driver.find_element(By.CSS_SELECTOR, self.shadow_dom_css_selector)
        self.shadow_root = self.shadow_host.shadow_root
        self.shadow_dom_text = self.shadow_root.find_element(By.CSS_SELECTOR, self.shadow_dom_content_css_selector).text
        self.assertEqual(self.expected_shadow_dom_text, self.shadow_dom_text)

    def test_07_canvas(self) -> None:
        """Docstring: Test 07 (HTML5 Canvas) -> Pseudo test"""
        self.driver.get(self.page_url_canvas)
        self.shadow_host1 = self.driver.find_element(By.ID, self.canvas_shadow_dom1_id)
        self.shadow_root1 = self.shadow_host1.shadow_root
        self.shadow_host2 = self.shadow_root1.find_element(By.CSS_SELECTOR, self.canvas_shadow_dom2_css_selector)
        self.shadow_root2 = self.shadow_host2.shadow_root
        self.start_button = self.shadow_root2.find_element(By.CSS_SELECTOR, self.canvas_shadow_dom2_btn_css_selector)
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of(self.start_button))
        self.start_button.click()
        WebDriverWait(self.driver, self.timeout).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        WebDriverWait(self.driver, self.timeout)\
            .until(EC.visibility_of(self.shadow_root1
                                    .find_element(By.CSS_SELECTOR, self.drawing_canvas_css_selector).shadow_root
                                    .find_element(By.ID, self.ink_engine_id)))
        ActionChains(self.driver)\
            .move_by_offset(200, 200)\
            .click_and_hold().move_by_offset(500, 0).release()\
            .click_and_hold().move_by_offset(0, 200).release()\
            .click_and_hold().move_by_offset(-500, 0).release()\
            .click_and_hold().move_by_offset(0, -200).release()\
            .perform()
        self.assertTrue(True)

    def test_08_video(self) -> None:
        """Docstring: Test 08 (HTML5 Video)"""
        self.driver.get(self.page_url_video)
        self.video_player = self.driver.find_element(By.ID, self.video_id)
        self.duration = self.driver.execute_script("return arguments[0].duration", self.video_player)
        self.assertEqual(self.expected_duration, round(self.duration))
        self.source = self.driver.execute_script("return arguments[0].currentSrc", self.video_player)
        self.assertEqual(self.expected_source, self.source)

    def test_09_web_storage(self) -> None:
        """Docstring: Test 09 (HTML5 Web Storage)"""
        self.driver.get(self.page_url_web_storage)
        self.new_color = '000000'
        self.driver.execute_script("localStorage.bgcolor = '" + self.new_color + "'")
        self.driver.execute_script('location.reload()')
        self.input_color = self.driver.find_element(By.ID, self.bg_color_id)
        self.color = self.input_color.get_attribute('value')
        self.assertEqual(self.color, self.new_color)