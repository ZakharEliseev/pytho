from argparse import ArgumentError


def div_safe(a, b):
    print('start for', [a, b])
    try:
        c = a / b
    #  except Exception:
    #     pass
    except TypeError as e:
        print('OOOPS', e)
    #   return None
    except ZeroDivisionError:
        print("please don't divide bt zero")
        return 0
    # except NameError:
    #    pass
    # except ArgumentError:
    #    pass
    # except (ValueError, NameError, EnvironmentError):
    #    pass
    # except Exception:
    #    pass
    else:
        print('- return c')
        return c
    finally:
        print('finally for', [a, b])

    print('leaving with', [a, b])


print(div_safe(1, 2))
print(div_safe(10, 2))
print(div_safe(10, 3))
print(div_safe(10, '2'))
print(div_safe(12, 4))
print(div_safe(1, 0))
print(div_safe('1', 0))
print(div_safe(123, 5))
