import logging

class CustomLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def log_message(self, message):
        if not message:
            raise ValueError("ლოგირების მესიჯი არ უნდა იყოს ცარიელი.")
        if not isinstance(message, str):
            raise TypeError("ლოგირების მესიჯი უნდა იყოს სტრიქონი.")
        if len(message.strip()) == 0:
            raise ValueError("ლოგირების მესიჯი არ უნდა შედგებოდეს მხოლოდ ცარიელი სიმბოლოებისგან.")
        self.logger.debug(message)

    def log_info(self, message):
        self.log_message(message)

    def log_warning(self, message):
        self.log_message(message)
        self.logger.warning(message)

    def log_error(self, message):
        self.log_message(message)
        self.logger.error(message)

    def log_exception(self, message, exception):
        self.log_message(f"{message}: {exception}")
        self.logger.exception(f"{message}: {exception}")

logger = CustomLogger("MyLogger")

try:
    logger.log_info("ეს არის ინფორმაციული შეტყობინება.")
    logger.log_warning("გაფრთხილება!")
    logger.log_error("შეცდომა მოხდა.")
    logger.log_message("")

except ValueError as e:
    logger.log_exception("ვალიდაციის შეცდომა", e)
except TypeError as e:
    logger.log_exception("ტიპის შეცდომა",e)
except Exception as e:
    logger.log_exception("მოულოდნელი შეცდომა", e)