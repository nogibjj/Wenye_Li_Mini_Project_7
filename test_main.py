"""
Test goes here

"""
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import insert_row, update_row, delete_row, select_rows


def test_extract():
    data = extract()
    assert data == "data/drug-use-by-age.csv"


def test_load():
    data = load()
    assert data


def test_insert():
    data = insert_row()
    assert data == "Success"


def test_select():
    data = select_rows()
    assert data == "Success"


def test_update():
    data = update_row()
    assert data == "Success"


def test_delete():
    data = delete_row()
    assert data == "Success"


if __name__ == "__main__":
    test_extract()
    test_load()
    test_insert()
    test_select()
    test_update()
    test_delete()
