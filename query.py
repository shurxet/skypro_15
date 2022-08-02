import sqlite3


def connect(query):
    with sqlite3.connect('animal.db') as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

    return result


def main():
    query_1 = """
        CREATE TABLE IF NOT EXISTS colors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            color VARCHAR(50)
    )
    """
    print(connect(query_1))


    query_2 = """
            CREATE TABLE IF NOT EXISTS animal_color (
                animal_id INTEGER,
                color_id INTEGER,
                FOREIGN KEY (animal_id) REFERENCES animals("index"),
                FOREIGN KEY (color_id) REFERENCES colors(id)
        )
        """
    print(connect(query_2))


    query_3 = """
        INSERT INTO colors (color)
        
        SELECT DISTINCT * FROM(
            SELECT DISTINCT color1 AS  color
            FROM animals
            WHERE color IS NOT NULL
            UNION ALL
            SELECT DISTINCT color2 AS color
            FROM animals
            WHERE color IS NOT NULL
        )
    """
    print(connect(query_3))


    query_4 = """
        INSERT INTO animal_color (animal_id, color_id)
        SELECT DISTINCT animals."index", colors.id
        FROM animals
        JOIN colors ON colors.color = animals.color1
        UNION ALL
        SELECT DISTINCT animals."index", colors.id 
        FROM animals
        JOIN colors ON colors.color = animals.color2
    """
    print(connect(query_4))


    query_5 = """
        CREATE TABLE IF NOT EXISTS outcome(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subtype VARCHAR (50),
            "type" VARCHAR (50),
            "mounth" INTEGER,
            "year" INTEGER
    )
    """
    print(connect(query_5))


    query_6 = """
        INSERT INTO outcome (subtype, "type", "mounth", "year")
        SELECT DISTINCT 
            animals.outcome_subtype,
            animals.outcome_type,
            animals.outcome_month,
            animals.outcome_year
        FROM animals
    """
    print(connect(query_6))


    query_7 = """
        CREATE TABLE IF NOT EXISTS animals_final (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age_upon_outcome VARCHAR (50),
            animal_id VARCHAR (50),
            animal_type VARCHAR (50),
            name VARCHAR (50),
            breed VARCHAR (50),
            date_of_birth VARCHAR (50),
            outcome_id INTEGER,
            FOREIGN KEY (outcome_id) REFERENCES outcome(id)
        )
    """
    print(connect(query_7))


    query_8 = """
        INSERT INTO animals_final (age_upon_outcome, animal_id, animal_type, name, breed, date_of_birth, outcome_id)
        SELECT DISTINCT
            animals.age_upon_outcome,
            animals.animal_id,
            animals.animal_type,
            animals.name,
            animals.breed,
            animals.date_of_birth,
            outcome.id
        FROM animals
        JOIN outcome
            ON outcome.subtype = animals.outcome_subtype
            AND outcome."type" = animals.outcome_type
            AND outcome."mounth" = animals.outcome_month
            AND outcome."year" = animals.outcome_year
    """
    print(connect(query_8))

    query_9 = """
            INSERT INTO animal_color (animal_id, color_id)
            SELECT DISTINCT animals_final.id, colors.id
            FROM animals
            JOIN colors ON colors.color = animals.color1
            JOIN animals_final ON animals_final.animal_id = animals.animal_id
            UNION ALL
            SELECT DISTINCT animals_final.id, colors.id
            FROM animals
            JOIN colors ON colors.color = animals.color2
            JOIN animals_final ON animals_final.animal_id = animals.animal_id

        """
    print(connect(query_9))


    query_10 = """
        CREATE TABLE IF NOT EXISTS types (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            "type" VARCHAR (50)
        )
    """
    print(connect(query_10))


    query_11 = """
        INSERT INTO types ("type")
            SELECT DISTINCT animals.animal_type
        FROM animals
    """
    print(connect(query_11))


    query_12 = """
        CREATE TABLE IF NOT EXISTS breeds (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            breed VARCHAR (50)
        )
    """
    print(connect(query_12))


    query_13 = """
        INSERT INTO breeds (breed)
            SELECT DISTINCT animals.breed
        FROM animals
    """
    print(connect(query_13))



if __name__ == '__main__':
    main()