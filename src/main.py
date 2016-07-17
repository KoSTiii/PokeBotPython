
from login_manager import LoginManager
import config

def main():
    print('hopla')

    lm = LoginManager(config.POKEGO_LOGINTYPE, config.POKEGO_USERNAME, config.POKEGO_PASSWORD)
    lm.login()


if __name__ == '__main__':
    main()