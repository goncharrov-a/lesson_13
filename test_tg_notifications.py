import allure
import pytest


@allure.epic("Demo")
@allure.feature("Successful cases")
@allure.tag("positive", "smoke")
@pytest.mark.parametrize("a,b,expected", [
    (1, 1, 2),
    (2, 3, 5),
    (0, 5, 5),
    (-1, 1, 0),
    (10, 20, 30),
])
def test_sum_success(a: int, b: int, expected: int):
    with allure.step(f"Складываем {a} и {b}"):
        result = a + b

    with allure.step("Проверяем результат"):
        assert result == expected


@allure.epic("Demo")
@allure.feature("Failure cases")
@allure.tag("negative", "regression")
@pytest.mark.parametrize("a,b,expected", [
    (1, 1, 3),
    (2, 2, 5),
    (0, 0, 1),
    (-1, -1, -1),
    (10, 5, 20),
])
def test_sum_failure(a: int, b: int, expected: int):
    with allure.step(f"Складываем {a} и {b}"):
        result = a + b

    with allure.step("Проверяем заведомо неверное ожидание"):
        assert result == expected