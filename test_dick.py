from selene import browser, be, have


browser.open('https://duckduckgo.com/')
browser.element('[id="searchbox_input"]').should(be.blank).type('Утка').press_enter()
browser.element('[data-testid="web-vertical"]').should(have.text('Утки'))