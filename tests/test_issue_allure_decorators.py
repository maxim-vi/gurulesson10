import allure
from allure_commons.types import Severity
from gurulesson10.allure_steps.allure_steps_for_test import open_browser, search_repository, open_repository, open_issue_tab, \
    check_homework_issue


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "mtitov")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_issue_name():
    open_browser()
    search_repository()
    open_repository()
    open_issue_tab()
    check_homework_issue()


