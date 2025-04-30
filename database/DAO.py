from database.DB_connect import DBConnect
from model.volo import Volo

class DAO():
    @staticmethod
    def getAllVoli(distanza):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
        from (SELECT ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID, AVG(DISTANCE) as media
        FROM flights
        group by ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID) s 
        where s.media >= %s"""
        cursor.execute(query, (distanza,))

        for row in cursor:
            result.append(Volo(row['ORIGIN_AIRPORT_ID'], row['DESTINATION_AIRPORT_ID'], row['media']))
        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getAllAeroporti():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT a.ID, a.AIRPORT
        FROM airports a"""
        cursor.execute(query)

        for row in cursor:
            result.append((row['ID'], row['AIRPORT']))
        cursor.close()
        conn.close()
        return result
