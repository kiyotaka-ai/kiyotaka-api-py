import kiyotaka

def main():
    enums = [kiyotaka.Exchange, kiyotaka.Type]

    for enum in enums:
        print(enum)
        for e in enum:
            print(e.name, '=', e.value)

if __name__ == '__main__':
    main()
