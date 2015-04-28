
# pip install pytest
# http://pytest.org/latest/

import os
import pytest


def test_1():
    result = True
    print("\nThis is test #1: "+str(result))
    assert result


def test_2():
    result = False
    print("\nThis is test #2: "+str(result))
    assert result


def test_3():
    result = True
    print("\nThis is test #3: "+str(result))
    assert result


def main():
    os.chdir(os.path.dirname(__file__))
    pytest.main(["-v", "-s", os.path.basename(__file__)])


if __name__ == "__main__":
    main()
