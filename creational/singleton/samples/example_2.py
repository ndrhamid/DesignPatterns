class ChashManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not ChashManager._instance:
            cls._instance = super(ChashManager, cls).__new__(cls, *args, *kwargs)
            cls._instance._initialize_cash()

        return cls._instance

    def _initialize_cash(self):
        self.cash = {}

    def set(self, key, value):
        self.cash[key] = value

    def get(self, key):
        return self.cash.get(key)

    def clear(self):
        self.cash.clear()
