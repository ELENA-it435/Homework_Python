import allure
from lesson_10.pages.calculator_page import CalculatorPage


@allure.title("Проверка сложения на онлайн-калькуляторе")
@allure.description(
    "Тест проверяет корректность вычисления 7 + 8 = 15 "
    "на странице калькулятора."
)
@allure.feature("Онлайн-калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc_result(driver):
    page = CalculatorPage(driver)

    with allure.step("Открываем страницу калькулятора"):
        page.open()

    with allure.step("Устанавливаем задержку 45"):
        page.set_delay("45")

    with allure.step("Вводим выражение 7 + 8 ="):
        for symbol in ["7", "+", "8", "="]:
            page.click_button(symbol)

    with allure.step("Ожидаем появления результата на экране"):
        page.wait_for_result("15")

    with allure.step("Проверяем, что результат равен 15"):
        result = page.get_result()
        assert result == "15", f"Ожидалось 15, получено {result}"
