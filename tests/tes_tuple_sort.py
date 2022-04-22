from src import tuple_sort

def test_tuple_sort(tuple_list):
    """Test case to validate insertion of data into BST"""
    actual_output = tuple_sort.get_output(tuple_list)

    expected_output = [('sop', 43, 56),('tom', 5, 24), ('tom', 24, 26) , ('tor', 2, 8)]
    assert expected_output == actual_output
