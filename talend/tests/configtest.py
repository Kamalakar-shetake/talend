import pytest
from src import binary_search_tree_operation


@pytest.fixture
def bst():
    yield binary_search_tree_operation


@pytest.fixture
def insert_elements():
    return [30,60,70,20,10]


@pytest.fixture
def delete_elements():
    return [30]

@pytest.fixture
def tuple_list():
    return [('tom', 24, 26),('tom', 15, 24),('tor', 2, 8),('sop', 43, 56)]