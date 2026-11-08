from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    HEADER = (By.XPATH, "//h1[text()='Лента заказов']")
    FIRST_ORDER_CARD = (By.XPATH, "(//a[contains(@class,'OrderHistory_link')])[1]")
    ORDER_NUMBERS = (
        By.XPATH,
        "//a[contains(@class,'OrderHistory_link')]//p[contains(@class,'text_type_digits-default')]",
    )
    TOTAL_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    IN_PROGRESS_LIST = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul")
