import sqlite3
from flask import Flask, jsonify




def main():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    app.config['DEBUG'] = True

    def connect(query):
        with sqlite3.connect("animal.db") as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
        return result



    @app.route('/<int:itemid>')
    def get_animals(itemid):
        # with sqlite3.connect("animal.db") as connection:
        #     cursor = connection.cursor()
        #     cursor.execute(
        #          "SELECT * FROM animals_final WHERE id= :itemid", {"id": itemid } # Я не смог здесь передать данные,
        #                                                        пришлось предать через f строку. Подскажите пожалуйста
        #                                                        как здесь правильно передать?
        #     )
        #     response = cursor.fetchall()

        query = f"""
            SELECT *
            FROM animals_final
            WHERE id = '{itemid}'
        """

        response = connect(query)[0]

        result = {
            'ID СТРОКИ': response[0],
            'ВОЗРОСТ ЖИВОТНОГО': response[1],
            'ID ЖИВОТНОГО': response[2],
            'ВИД ЖИВОТНОГО':response[3],
            'КЛИЧКА ЖИВОТНОГО': response[4],
            'ПОРОДА ЖИВОТНОГО': response[5],
            'ДАТА РОЖДЕНИЯ ЖИВОТНОГО': response[6]
        }

        return jsonify(result)

    app.run()


if __name__ == '__main__':
    main()



