# Conduit URL

CON_URL = 'http://localhost:1667'

# Bejelentkező - Menü gombok:

sign_up_x = '//a[@href="#/register"]'
sign_in_x = '//a[@href="#/login"]'

# Sign in form:

si_email_x = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
si_password_x = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
sign_in_button_x = '//*[@id="app"]/div/div/div/div/form/button'

# Logged in - Menü gombok:

user_x = '//*[@id="app"]/nav/div/ul/li[4]/a'
new_article_x = '//a[@href="#/editor"]'
home_x = '//*[@id="app"]/nav/div/ul/li[1]/a'
log_out_x = "//a/i[@class='ion-android-exit']"
settings_x = '//a[@href="#/settings"]'

# editor mezők:

title_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input'
about_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input'
article_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea'
tag_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input'
publish_button_x = '//*[@id="app"]/div/div/div/div/form/button'

# My posts első post title

first_post_x = '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div[1]/a/h1'

# Post gombok:

delete_button_x = '//*[@id="app"]/div/div[1]/div/div/span/button/span'
edit_button_x = "//a[@class='btn btn-sm btn-outline-secondary']"

# Registration popup:

reg_message_x = '/html/body/div[2]/div/div[2]'
reg_fail_message_x = '/html/body/div[2]/div/div[3]'
ok_button_x = '/html/body/div[2]/div/div[4]/div/button'

# Sign up mezők:

username_x = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
email_x = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
password_x = '//*[@id="app"]/div/div/div/div/form/fieldset[3]/input'
sign_up_button_x = '//*[@id="app"]/div/div/div/div/form/button'

# Settings oldal mezői:

new_username_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input'
new_email_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/input'
new_password_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[5]/input'
update_button_x = '//*[@id="app"]/div/div/div/div/form/fieldset/button'
update_success_x = '/html/body/div[2]/div/div[2]'
update_ok_button_x = '/html/body/div[2]/div/div[3]/div/button'

# Cookie policy

cookie_panel = 'cookie-policy-panel'
cookie_accept_btn = '//*[@id="cookie-policy-panel"]/div/div[2]/button[2]'
