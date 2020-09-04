import datetime


def path_decor(path):
    def decorator(old_func):
        def new_func(*args, **kwargs):
            ret = old_func(*args, **kwargs)
            start_time = datetime.datetime.now()
            output_data = {'date_info': start_time,
                           'function name': old_func.__name__,
                           'arguments': args}
            with open(path, 'w', encoding='utf8') as file:
                file.write(str(output_data))
            return ret
        return new_func
    return decorator


@path_decor('log_test.txt')
def somefunction(someparam1, someparam2):
    pass


somefunction(1, 2)
