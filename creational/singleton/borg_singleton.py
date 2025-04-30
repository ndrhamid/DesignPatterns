class BorgSingletonClass:
    share_state = {}

    def __new__(cls, *args, **kwargs):
