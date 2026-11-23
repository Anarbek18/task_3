from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    BUN_INGREDIENT = (By.XPATH, "(//a[contains(@class,'BurgerIngredient_ingredient')])[1]")
    BUN_COUNTER = (
        By.XPATH,
        "(//a[contains(@class,'BurgerIngredient_ingredient')])[1]//p[contains(@class,'counter_counter__num')]",
    )
    CONSTRUCTOR_AREA = (By.XPATH, "//section[contains(@class,'BurgerConstructor_basket')]")

    INGREDIENT_DETAILS_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class,'Modal_modal__title_shadow')]")
