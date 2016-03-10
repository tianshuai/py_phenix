def force_int(value, default=1):
    try:
        return int(value)
    except:
        return default
