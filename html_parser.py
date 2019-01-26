from mySQL_connector import *
from newspaper import fulltext


if __name__ == '__main__':
    conn = create_cnx()
    c = create_cursor(conn)
    cc = create_cursor(conn)

    #c.execute("ALTER TABLE tweets_1 ADD COLUMN news_text text")
    c.execute("SELECT html, num FROM tweets_1")

    for item in c:
        html = item[0]
        num = item[1]

        try:
            news_text = fulltext(item[0])
            #print(news_text)
            cc.execute("UPDATE tweets_1 SET news_text = %s WHERE num = %s", (news_text, str(num)))
            conn.commit()
        
        except:
            pass
    
        if num % 10000 == 0:
            print(num)
    
    c.close()
    cc.close()
    conn.close()
