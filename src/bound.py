from time import perf_counter


def _slow_fibonacci(n):
    if n in {0, 1}:
        return n
    return _slow_fibonacci(n - 1) + _slow_fibonacci(n - 2)


def cpu_bound():
    # This function takes approx 1 second
    # Ryzen 5 5600x 6-core processor × 12
    st = perf_counter()
    _slow_fibonacci(34)
    _slow_fibonacci(30)
    end = perf_counter()
    return end - st


def _sleep_sql(pool):
    wait_time = 1  # seconds
    with pool.acquire() as conn:
        with conn.cursor() as cursor:
            response = cursor.callproc(
                "DBMS_SESSION.SLEEP", parameters=[wait_time]
            )
    return response


def io_bound(pool):
    st = perf_counter()
    _sleep_sql(pool)
    end = perf_counter()
    return end - st
