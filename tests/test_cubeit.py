from playwright.sync_api import Page, expect

BASE_URL = "https://cubeit-playwrigh-test-ci.netlify.app//"

def test_cube(page: Page):
    page.goto(BASE_URL)
    
    field = page.get_by_placeholder('enter number...')
    field.fill('5')
    
    btn = page.get_by_role("button", name="Cube")
    btn.click()
    
    result = page.locator("css=p#result")
    
    expect(result).to_contain_text("125")
    


def test_empty_input(page: Page):
    page.goto(BASE_URL)
    
    field = page.get_by_placeholder('enter number...')
    field.fill('')
    
    btn = page.get_by_role("button", name="Cube")
    btn.click()
    
    result = page.locator("css=p#result")
    
    expect(result).to_have_text("Enter something!")