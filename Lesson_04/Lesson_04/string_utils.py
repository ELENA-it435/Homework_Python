class StringUtils:
    def capitalize(self, string: str) -> str:
        if not string:
            return ""
        return string.capitalize()

    def trim(self, string: str) -> str:
        if not string:
            return ""
        whitespace = " "
        while string.startswith(whitespace):
            string = string.removeprefix(whitespace)
        return string

    def contains(self, string: str, symbol: str) -> bool:
        if not string or not symbol:
            return False
        try:
            return string.index(symbol) > -1
        except ValueError:
            return False

    def delete_symbol(self, string: str, symbol: str) -> str:
        if not string or not symbol:
            return string or ""
        if self.contains(string, symbol):
            string = string.replace(symbol, "")
        return string
