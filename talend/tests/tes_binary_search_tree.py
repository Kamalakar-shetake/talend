def test_bst_insert(bst, insert_elements):
    """Test case to validate insertion of data into BST"""
    root = None
    for element in insert_elements:
        root = bst.add(root, element)
    actual_output = []
    bst.inorder(root, actual_output)
    expected_output = [10,20,30,60,70]
    assert expected_output == actual_output


def test_bst_delete(bst, insert_elements, delete_elements):
    """Test case to validate deletion of data from BST"""
    root = None
    for element in insert_elements:
        root = bst.add(root, element)

    for element in delete_elements:
        root = bst.delete(root, element)
    actual_output = []
    bst.inorder(root, actual_output)
    expected_output = [10,20,60,70]
    assert expected_output == actual_output


def test_bst_inorder_traversal(bst, insert_elements):
    """Test case to validate inorder traversal in BST"""
    root = None
    for element in insert_elements:
        root = bst.add(root, element)
    actual_output = []
    bst.inorder(root, actual_output)
    expected_output = [10,20,30,60,70]
    assert expected_output == actual_output