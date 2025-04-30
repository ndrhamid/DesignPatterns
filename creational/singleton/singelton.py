class SingletonClass:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not SingletonClass._instance:
            cls._instance = super(SingletonClass, cls).__new__(cls, *args, **kwargs)

        return SingletonClass._instance