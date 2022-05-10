from selenium import webdriver
import pytest


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser = maximize_window()
    yield browser
    browser.quit()

@pytest.fixture(scope="session")
def browser_session():
    browser = webdriver.Chrome()
    browser = maximize_window()
    yield browser
    browser.quit()
    
    
    

    