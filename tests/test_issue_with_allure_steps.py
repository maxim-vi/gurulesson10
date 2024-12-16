from selene import by, be, browser
from selene.support.shared.jquery_style import s
import allure


def test_issue_name():
    with allure.step("Открыть github"):
        browser.open("")

    with allure.step("Искать репозиторий"):
        s("[data-target='qbsearch-input.inputButtonText']").click()
        s("#query-builder-test").click().type("maxim-vi/gurulesson10").press_enter()

    with allure.step("Открыть репозиторий"):
        s(by.link_text("maxim-vi/gurulesson10")).click()

    with allure.step("Открыть вкладку Issues"):
        s("#issues-tab").click()

    with allure.step("Проверить Issue homework в названии"):
        s(by.partial_text("homework")).should(be.visible)
