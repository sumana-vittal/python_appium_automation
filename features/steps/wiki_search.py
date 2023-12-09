from behave import given, when, then


@given('Click to Skip onboarding')
def click_skip_ob(context):
    context.app.onboarding_page.click_skip_ob()


@when('Click search icon')
def click_search_icon(context):
    context.app.explore_page.click_search_icon()


@when('Search for Python (programming language)')
def input_search_text(context):
    context.app.search_page.input_search_text()


@then('Verify first result is Python (programming language)')
def verify_search_result(context):
    context.app.search_page.verify_search_result()
