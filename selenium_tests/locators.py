# Conduit URL

CON_URL = 'http://localhost:1667'

# Bejelentkezõ - Menû gombok:

sign_up_x = '//*[@id="app"]/nav/div/ul/li[3]/a'
sign_in_x = '//*[@id="app"]/nav/div/ul/li[2]/a'

# Sign in form:

si_email_x = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
si_password_x = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
sign_in_button_x = '//*[@id="app"]/div/div/div/div/form/button'

# Logged in - Menü gombok:

user_x = '//*[@id="app"]/nav/div/ul/li[4]/a'
new_article_x = '//a[@href="#/editor"]'
home_x = '//*[@id="app"]/nav/div/ul/li[1]/a'
log_out_x = "//a/i[@class='ion-android-exit']"

# editor mezõk:
title_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input'
about_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input'
article_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea'
tag_x = '//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input'
publish_button_x = '//*[@id="app"]/div/div/div/div/form/button'

# My posts elsõ post

first_post_x = '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div[1]/a/h1'

# Post gombok:

delete_button_x = '//*[@id="app"]/div/div[1]/div/div/span/button/span'
edit_button_x = "//a[@class='btn btn-sm btn-outline-secondary']"

# Registration popup:

reg_message_x = '/html/body/div[2]/div/div[2]'
reg_fail_message_x = '/html/body/div[2]/div/div[3]'
ok_button_x = '/html/body/div[2]/div/div[4]/div/button'


# Sign up mezõk:

username_x = '//*[@id="app"]/div/div/div/div/form/fieldset[1]/input'
email_x = '//*[@id="app"]/div/div/div/div/form/fieldset[2]/input'
password_x = '//*[@id="app"]/div/div/div/div/form/fieldset[3]/input'
sign_up_button_x = '//*[@id="app"]/div/div/div/div/form/button'
