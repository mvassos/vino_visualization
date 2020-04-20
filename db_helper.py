import _sqlite3 as sql
import pandas as pd

DB_NAME = 'data.db'
DATA_FILE = 'winemag-data-130k-v2.csv'
COLS = '''id, country, description, designation, points, price, province, region_1, region_2,
        taster_name, taster_twitter_handle, title, variety, winery'''

def create_db():
    conn = sql.connect(DB_NAME)
    c = conn.cursor()

    c.execute('''
                CREATE TABLE REVIEWS
                ([id] integer,
                [country] text,
                [description] text,
                [designation] text,
                [points] integer,
                [price] integer,
                [province] text,
                [region_1] text,
                [region_2] text,
                [taster_name] text,
                [taster_twitter_handle] text,
                [title] text,
                [variety] text,
                [winery] text)''')

    conn.commit()


def upload_data():
    conn = sql.connect(DB_NAME)
    c = conn.cursor()

    wine_data = pd.read_csv(DATA_FILE, encoding='utf-8')
    wine_data.to_sql('REVIEWS', conn, if_exists='replace')

    # df = pd.read_sql_query('SELECT * FROM REVIEWS;', conn)
    # print(df)


def get_all_data():
    conn = sql.connect(DB_NAME)
    c = conn.cursor()

    df = pd.read_sql_query('SELECT * FROM REVIEWS;', conn)
    return df


def get_price_points():
    conn = sql.connect(DB_NAME)
    c = conn.cursor()

    df = pd.read_sql_query('SELECT price, points FROM REVIEWS;', conn)
    return df


if __name__ == '__main__':
    pass
    # create_db()
    # upload_data()

