"""
Test goes here

"""
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import complex_query


def test_extract():
    data = extract()
    assert data == "data/drug-use-by-age.csv"


def test_load():
    data = load()
    assert data


def test_query():
    data = complex_query()
    assert data == "Success"


if __name__ == "__main__":
    test_extract()
    test_load()
    test_query()
