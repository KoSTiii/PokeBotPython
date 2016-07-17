from login_manager import LoginManager
import config


print('hopla')

lm = LoginManager(config.POKEGO_LOGINTYPE, config.POKEGO_USERNAME, config.POKEGO_PASSWORD)
if lm.login():
    print('Success login')
else:
    print('Error loggin')

print('Token: ' + lm.get_access_token())
