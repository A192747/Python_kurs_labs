# TODO Найдите количество книг, которое можно разместить на дискете
disk_size = 1.44 # MByte
lists_count = 100
lines_count = 50
symbols_count = 25
symbol_size = 4 # Byte

book_size = lists_count * lines_count * symbols_count * symbol_size
books_count = round((disk_size * 1024 * 1024) / book_size)
print("Количество книг, помещающихся на дискету:", books_count)
