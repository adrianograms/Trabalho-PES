class singleton(type):
    instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super(singleton, cls).__call__(*args, **kwargs)

        return cls.instances[cls]
