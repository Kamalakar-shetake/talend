class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None


def add(root, data):
    '''

    :param root:
    :param data:
    :return: node value
    '''
    try:
        if root is None:
            return Node(data)
        if data < root.info:
            root.left = add(root.left, data)
        else:
            root.right = add(root.right, data)
        return root
    except Exception as e:
        print("Error in node inserction function..{}".format(e))

def delete(root, data):
    '''

    :param root:
    :param data:
    :return:
    '''
    try:
        if root is None:
            return root

        if data < root.info:
            root.left = delete(root.left, data)
            return root
        elif data > root.info:
            root.right = delete(root.right, data)
            return root
        if root.left is None and root.right is None:
            return None

        if root.left is None:
            temp = root.right
            root.right = None
            return temp
        elif root.right is None:
            temp = root.left
            root.left = None
            return temp

        parent = root

        succ = root.right

        while succ.left is not None:
            parent = succ
            succ = succ.left

        if parent != root:
            parent.left = succ.right
        else:
            parent.right = succ.right

        root.info = succ.info

        return root
    except Exception as e:
        print("Error in node deletion method..{}".format(e))

def inorder(root, arr):
    '''
    :param root:
    :return:
    '''
    try:
        if root:
            inorder(root.left, arr)
            arr.append(root.info)
            inorder(root.right, arr)
    except Exception as e:
        print("Error in inorder method")

def main():
    root = None
    while True:
        print("\nChoose from operations below:-\n")
        print(
            "1) To INSERT an element in Binary Search Tree, press 1 then press Enter"
        )
        print(
            "2) To DELETE an element from Binary Search Tree, press 2 then press Enter"
        )
        print(
            "any other number ) To terminate, press any number or letter then press Enter.\n")

        operation = input("Select an operation to perform: ")

        if operation != "1" and operation != "2":
            break
        else:
            while True:
                try:
                    user_input = input("Enter an integer : ")
                    user_input = eval(user_input)
                except ValueError:
                    print(
                        "The value entered is not a valid integer, please enter the value again.\n"
                    )
                    continue
                break

            if operation == "1":
                # Insert into BST
                root = add(root, user_input)
            elif operation == "2":
                # Delete from BST
                root = delete(root, user_input)

            arr = []
            inorder(root, arr)
            print("\nCurrent inorder for Tree:-")
            print(arr)


if __name__ == '__main__':
    main()
