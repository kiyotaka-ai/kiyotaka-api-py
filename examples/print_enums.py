import tharamine

def main():
    enums = [tharamine.Exchange, tharamine.Type]

    for enum in enums:
        print(enum)
        for e in enum:
            print(e.name, '=', e.value)

if __name__ == '__main__':
    main()
