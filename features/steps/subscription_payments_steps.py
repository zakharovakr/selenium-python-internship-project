from behave import given, when, then
from time import sleep

@given('Open main page')
def verify_open_main_page(context):
    context.app.main_page.open()
    # couldn't get rid of this 'sleep' - the page reloads in Firefox, couldn't figure out any better waits
    sleep(5)

@given('Log in')
def verify_log_in(context):
    context.app.signin_page.login()

@when('Click on Main menu')
def click_main_menu(context):
    context.app.main_page.open_main_menu_mobile()

@when('Click on User Icon')
def click_user_icon_mobile(context):
    context.app.main_page.click_user_icon_mobile()

@when('Click on settings option')
def verify_open_settings(context):
    context.app.main_page.open_settings()


@when('Click on Subscription & payments option')
def open_subscription(context):
    context.app.settings_page.open_subscription_payments()

@then('Verify the subscription page opens')
def verify_subsription_page(context):
    context.app.subscription_page.verify_partial_url('/subscription')

@then('Verify title “Subscription & payments” is visible')
def verify_subscription_title(context):
    context.app.subscription_page.verify_title()

@then('Verify “back” and “upgrade plan” buttons are available')
def verify_buttons(context):
    context.app.subscription_page.verify_btns()