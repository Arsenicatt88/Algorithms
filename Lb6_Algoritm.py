# Создание дерева
def build_tree(values):
    if not values or values[0] is None:
        return None

    root = [values[0], None, None]
    queue = [root]
    head = 0
    i = 1

    while head < len(queue) and i < len(values):
        node = queue[head]
        head += 1

        if i < len(values) and values[i] is not None:
            node[1] = [values[i], None, None]
            queue.append(node[1])
        i += 1

        if i < len(values) and values[i] is not None:
            node[2] = [values[i], None, None]
            queue.append(node[2])
        i += 1

    return root

# A
def is_mirror(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False

    return (
        left[0] == right[0]
        and is_mirror(left[1], right[2])
        and is_mirror(left[2], right[1])
    )


def is_symmetric(root):
    if root is None:
        return True
    return is_mirror(root[1], root[2])


# B
def height(node):
    if node is None:
        return 0
    return 1 + max(height(node[1]), height(node[2]))


def diameter(root):
    if root is None:
        return 0

    left_height = height(root[1])
    right_height = height(root[2])

    through_root = left_height + right_height

    return max(
        through_root,
        diameter(root[1]),
        diameter(root[2])
    )


# D
def same_tree(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False

    return (
        a[0] == b[0]
        and same_tree(a[1], b[1])
        and same_tree(a[2], b[2])
    )


def is_subtree(root, sub_root):
    if sub_root is None:
        return True
    if root is None:
        return False

    if same_tree(root, sub_root):
        return True

    return is_subtree(root[1], sub_root) or is_subtree(root[2], sub_root)


# Вывод
if __name__ == "__main__":
    # A
    tree_a1 = build_tree([1, 2, 2, 3, 4, 4, 3])
    tree_a2 = build_tree([1, 2, 2, None, 3, None, 3])

    print("A1:", is_symmetric(tree_a1))  
    print("A2:", is_symmetric(tree_a2))  

    # B
    tree_b1 = build_tree([1, 2, 3, 4, 5])
    tree_b2 = build_tree([1, 2])

    print("B1:", diameter(tree_b1))  
    print("B2:", diameter(tree_b2))  

    # D
    root_d1 = build_tree([3, 4, 5, 1, 2])
    sub_d1 = build_tree([4, 1, 2])

    root_d2 = build_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    sub_d2 = build_tree([4, 1, 2])

    print("D1:", is_subtree(root_d1, sub_d1))  
    print("D2:", is_subtree(root_d2, sub_d2))  

#1) Дерево: каждый узел — это список из трёх элементов `[значение, левый_ребёнок, правый_ребёнок]`, а `None` означает, что ребёнка нет.

#2) Функция `build_tree` нужна только для тестов: она превращает компактную запись вида `[1,2,2,3,4,4,3]` в настоящее двоичное дерево, строя его по уровням с помощью очереди.

#3) В `build_tree` сначала создаётся корень, потом очередь `queue`, затем по индексу `i` поочерёдно добавляются левый и правый дети к текущему узлу; если значение `None`, ребёнок не создаётся.

#4) Функция `is_mirror` проверяет зеркальность двух поддеревьев: если оба узла `None`, это хорошо; если только один `None`, это плохо; иначе значения должны совпадать, а левый ребёнок одного сравнивается с правым ребёнком другого и наоборот.

#5) Функция `is_symmetric` для задачи A просто вызывает `is_mirror` для левого и правого поддеревьев корня, а если корень `None`, сразу возвращает `True`.

#6) Функция `height` для задачи B рекурсивно считает высоту дерева: для `None` возвращает `0`, иначе `1 + максимум из высот левого и правого ребёнка`.

#7) Функция `diameter` для задачи B считает диаметр: для каждого узла проверяется путь через него как `height(левый) + height(правый)`, затем результат сравнивается с диаметрами левого и правого поддеревьев, и берётся максимум.

#8) Функция `same_tree` для задачи D проверяет полное совпадение двух деревьев: оба `None` — `True`, один `None` — `False`, иначе значения должны совпадать и оба поддерева должны совпадать.

#9) Функция `is_subtree` для задачи D проверяет, есть ли в `root` поддерево, совпадающее с `subRoot`: если `sub_root` пустой, возвращается `True`; если `root` пустой, `False`; затем проверяется текущий узел через `same_tree` и рекурсивно левое и правое поддеревья.

