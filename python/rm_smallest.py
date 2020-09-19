import sys

def rm_smallest(d):
    if len(d) > 0:
        current_min = sys.maxsize
        min_key = ""

        for i in d:
            if d[i] < current_min:
                current_min = d[i]
                min_key = i

        d.pop(min_key)

    return d

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()
