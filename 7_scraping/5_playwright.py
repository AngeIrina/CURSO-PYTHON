import re # regular expression
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
  page.goto("https://playwright.dev/")

  # Esperar a que la página tenga el título 'Playwright'
  expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
  page.goto("https://playwright.dev/")

  # Hacer clic en el enlace "Get started"
  page.get_by_role("link", name="Get started").click()

  # Esperar a que la página tenga el título 'Get started'
  expect(page.get_by_role("heading", name="Installation")).to_be_visible()