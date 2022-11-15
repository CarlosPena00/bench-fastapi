import oracledb


def create_pool():
    pool = oracledb.SessionPool(
        "system/chcp@localhost:1521/xe",
        min=8,
        max=64,
        increment=4,
    )
    return pool
