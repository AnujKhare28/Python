n = 0

def fun():
    global n
    if n == 4:
        return
    print('Anuj Khare')
    n += 1
    fun()

fun()