import os

import pytest

if __name__ == '__main__':
    pytest.main(["-vs", "./login", "--alluredir=temp"])
    os.system("allure generate temp -o reports --clean")
