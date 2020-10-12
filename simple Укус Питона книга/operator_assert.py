mylist = ['item']
assert len(
    mylist) >= 1  # assert - если требуется гарантировать, что в списке будет хотя бы один элемент, и вы-звать ошибку
mylist.pop()
mylist
assert len(mylist) >= 1
