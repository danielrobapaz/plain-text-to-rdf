def get_list_safe(l: list, index: int, default: any = None):
    try:
        return l[index]
    except:
        return default