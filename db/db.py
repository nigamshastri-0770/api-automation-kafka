import psycopg


class DB:

    def __init__(self):

        self.conn = psycopg.connect(
            host="localhost",
            dbname="events",
            user="postgres",
            password="admin"
        )

    def fetch_order(
            self,
            order_id
    ):

        with self.conn.cursor() as c:

            c.execute(
                """
                SELECT *
                FROM orders
                WHERE order_id=%s
                """,
                (order_id,)
            )

            return c.fetchone()