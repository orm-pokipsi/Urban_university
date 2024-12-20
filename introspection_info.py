def introspection_info(obj):
    obj_type = type(obj).__name__

    attributes = dir(obj)

    methods = [method for method in attributes if callable(getattr(obj, method))]

    module = 'main' if __name__ == '__main__' else obj.__class__.__module__

    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module}

    return info


number_info = introspection_info(42)
print(number_info)

string_info = introspection_info('Hello')
print(string_info)

list_info = introspection_info([1, 10, 4.0, 'World'])
print(list_info)
