def height(node):
    return node['height'] if node else 0

def get_balance(node):
    if not node:
        return 0
    return height(node['left']) - height(node['right'])

def update_height(node):
    node['height'] = 1 + max(height(node['left']), height(node['right']))

def right_rotate(y):
    x = y['left']
    T2 = x['right']

    x['right'] = y
    y['left'] = T2

    update_height(y)
    update_height(x)

    return x

def left_rotate(x):
    y = x['right']
    T2 = y['left']

    y['left'] = x
    x['right'] = T2

    update_height(x)
    update_height(y)

    return y

def insert(node, key):
    if not node:
        return {'key': key, 'height': 1, 'left': None, 'right': None}
    
    if key < node['key']:
        node['left'] = insert(node['left'], key)
    elif key > node['key']:
        node['right'] = insert(node['right'], key)
    else:
        return node  # Дубликаты не добавляем

    update_height(node)
    balance = get_balance(node)

    # Left Left
    if balance > 1 and key < node['left']['key']:
        return right_rotate(node)

    # Right Right
    if balance < -1 and key > node['right']['key']:
        return left_rotate(node)

    # Left Right
    if balance > 1 and key > node['left']['key']:
        node['left'] = left_rotate(node['left'])
        return right_rotate(node)

    # Right Left
    if balance < -1 and key < node['right']['key']:
        node['right'] = right_rotate(node['right'])
        return left_rotate(node)

    return node

def min_value_node(node):
    current = node
    while current['left'] is not None:
        current = current['left']
    return current

def delete(node, key):
    if not node:
        return node

    if key < node['key']:
        node['left'] = delete(node['left'], key)
    elif key > node['key']:
        node['right'] = delete(node['right'], key)
    else:
        if node['left'] is None:
            return node['right']
        elif node['right'] is None:
            return node['left']

        temp = min_value_node(node['right'])
        node['key'] = temp['key']
        node['right'] = delete(node['right'], temp['key'])

    if not node:
        return node

    update_height(node)
    balance = get_balance(node)

    # Left Left
    if balance > 1 and get_balance(node['left']) >= 0:
        return right_rotate(node)

    # Left Right
    if balance > 1 and get_balance(node['left']) < 0:
        node['left'] = left_rotate(node['left'])
        return right_rotate(node)

    # Right Right
    if balance < -1 and get_balance(node['right']) <= 0:
        return left_rotate(node)

    # Right Left
    if balance < -1 and get_balance(node['right']) > 0:
        node['right'] = right_rotate(node['right'])
        return left_rotate(node)

    return node

def inorder_traversal(node, res=None):
    if res is None:
        res = []
    if node:
        inorder_traversal(node['left'], res)
        res.append(node['key'])
        inorder_traversal(node['right'], res)
    return res

def process_avl_test(operations):
    root = None
    for key in operations.get('insert', []):
        root = insert(root, key)
    for key in operations.get('delete', []):
        root = delete(root, key)
    return inorder_traversal(root)


# ТЕСТЫ
print(process_avl_test({'insert': [10, 20, 30, 40, 50, 25], 'delete': [40, 20]}))
print(process_avl_test({'insert': [5, 2, 8, 1, 3, 7, 9], 'delete': [2, 9]}))
print(process_avl_test({'insert': [1, 2, 3, 4, 5, 6, 7], 'delete': [4]}))