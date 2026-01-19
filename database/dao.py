from database.DB_connect import DBConnect
from model.gene import Gene

class DAO:

    @staticmethod
    def query_esempio():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM gene """

        cursor.execute(query)

        for row in cursor:
            result.append(Gene(**row))

        cursor.close()
        conn.close()
        print(result)
        return result

    @staticmethod
    def get_cromosomi():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT cromosoma 
                    FROM gene 
                    where cromosoma != 0 """
        cursor.execute(query)
        for row in cursor:
            result.append(row['cromosoma'])
        cursor.close()
        conn.close()
        print(result)
        return result

    @staticmethod
    def get_Interazioni():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT
                    g1.chromosome AS c1,
                    g2.chromosome AS c2,
                    SUM(i.correlation) AS peso
                    FROM interactions i
                    JOIN genes g1 ON i.gene1 = g1.gene_id
                    JOIN genes g2 ON i.gene2 = g2.gene_id
                    WHERE g1.chromosome != g2.chromosome
                    GROUP BY c1, c2"""
        cursor.execute(query)
        for row in cursor:
            result.append((row["c1"], row["c2"], row["peso"]))
        cursor.close()
        conn.close()
        print(result)
        return result