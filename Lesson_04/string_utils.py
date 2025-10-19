class StringUtils:
    def capitalize(self, string):
        if not string:
            return ""
        return string[0].upper() + string[1:]

    def trim(self, string):
        if string is None:
            return ""
        return string.strip()

    def to_list(self, string, delimiter=","):
        if not string:
            return []
        return string.split(delimiter)

    def contains(self, string, symbol):
        if not string or not symbol:
            return False
        return symbol in string
