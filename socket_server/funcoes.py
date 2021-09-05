import json

def pickle_to_dict(obj):
    obj_json = json.dumps(obj.__dict__,ensure_ascii=False)
    obj_dict = json.loads(obj_json)
    return obj_dict

def formata_tamanho(byte):
    if byte <= 1024:
        return f"{round(byte, 2)}.00 B"
    elif byte <= 1024**2:
        return f"{round(byte / 1024, 2)} KB"
    elif byte <= 1024**3:
        return f"{round(byte / (1024 * 1024), 2)} MB"
    else:
        return f"{round(byte / (1024 * 1024 * 1024), 2)} GB"