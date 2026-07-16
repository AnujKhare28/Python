n = 0

def fun():
    global n
    if n == 4:
        return
    n += 1
    fun()
    print('Anuj Khare')

fun()