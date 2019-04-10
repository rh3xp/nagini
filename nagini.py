import itertools


def get_user_input():
    for i in itertools.count():
        try:
            yield i, input('In [%d]: ' % i)
        except KeyboardInterrupt:
            pass
        except EOFError:
            break


def main():

    for i, user_input in get_user_input():
        pass

if __name__ == '__main__':
    main()
