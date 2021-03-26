import sqlite3

conn = sqlite3.connect('main.db')
c = conn.cursor()


def loginSQL(pseudo, password):
    c.execute(f'SELECT user_id FROM user WHERE user.username = {pseudo} and user.password = {password}')
    if c.fetchall() == []:return None
    L = c.fetchall()
    conn.close()
    return L[0]

def signupSQL(pseudo, password):
    c.execute('SELECT user_id FROM user WHERE user.username = pseudo')
    if c.fetchall() != []:
        return 'None'
    c.execute('INSERT INTO user (username, password) (?, ?)', (pseudo, password))
    conn.commit()
    conn.close()
    return f'[new user] {pseudo}: {password}'