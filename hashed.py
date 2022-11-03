if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(str(hash(tuple(integer_list))))