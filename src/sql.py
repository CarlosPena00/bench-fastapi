import oracledb


def create_pool():
    pool = oracledb.SessionPool(
        "system/chcp@localhost:1521/xe",
        min=24,
        max=100,
        increment=10,
    )
    return pool
