import pytest
from selene.support.shared import browser
from selene import have, be


@pytest.fixture()
def configure_size_window_browser():
    browser.config.window_width = 300
    browser.config.window_height = 700


def test_positive(configure_size_window_browser):
    browser.open('https://google.com')
    browser.element('[name=q]').should(be.blank).type('selene').press_enter()
    browser.element('[id=search]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_negative():
    browser.open('https://google.com')
    browser.element('[name=q]').should(be.blank).type('selene').press_enter()
    browser.element('[id=search]').should(have.no.text('Selene: User-oriented Web UI browser tests in Python'))

