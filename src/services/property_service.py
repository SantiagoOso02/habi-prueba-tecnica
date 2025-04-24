from src.database.db import get_connection

def get_properties(filters: dict) -> list:
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT 
        p.address,
        p.city,
        s.name AS status,
        p.price,
        p.year,
        p.description
    FROM 
        property p
    JOIN (
        SELECT sh.property_id, sh.status_id
        FROM status_history sh
        INNER JOIN (
            SELECT property_id, MAX(update_date) AS latest_date
            FROM status_history
            GROUP BY property_id
        ) latest 
        ON sh.property_id = latest.property_id AND sh.update_date = latest.latest_date
    ) last_status
    ON p.id = last_status.property_id
    JOIN status s ON last_status.status_id = s.id
    WHERE s.name IN ('pre_venta', 'en_venta', 'vendido')
    """

    values = []

    if "year" in filters:
        query += " AND p.year = %s"
        values.append(filters["year"])
    
    if "city" in filters:
        query += " AND p.city = %s"
        values.append(filters["city"])

    cursor.execute(query, values)
    results = cursor.fetchall()

    cursor.close()
    connection.close()
    return results
