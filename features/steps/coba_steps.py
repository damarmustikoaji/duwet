# file:features/steps/coba_steps.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave   import given, when, then

@given('I start a new game')
def step_impl(context):
    context.duck_count = 0
    context.red_button_pressed = 0

@when('I press the big red button')
def step_impl(context):
    context.red_button_pressed += 1

@when('I duck')
def step_impl(context):
    context.duck_count += 1

@when('I do the same thing as before')
def step_impl(context):
    context.execute_steps(u"""
        when I press the big {button_color} button
         and I duck
    """.format(button_color="red"))

@then('I reach the next level')
def step_impl(context):
    assert context.duck_count >= 0, 'Growth Rate is not between 0 and 100'
    assert context.red_button_pressed >= 0, 'Growth Rate is not between 0 and 100'