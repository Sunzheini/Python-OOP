class Validator:
    @staticmethod
    def vali_string(string: str, message: str):
        if string.strip() == '':
            raise ValueError(message)

    @staticmethod
    def vali_num(number: float, message: str):
        if number <= 0:
            raise ValueError(message)

    @staticmethod
    def vali_range(number, start, end, message):
        if number < start or number > end:
            raise ValueError(message)
