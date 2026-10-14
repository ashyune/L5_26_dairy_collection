"""Demonstrate a dairy cooperative's milk collection ledger."""

import hashlib
import sqlite3


def create_connection():
    """Create an in-memory database and its milk collection table."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        """
        CREATE TABLE milk (
            id INTEGER PRIMARY KEY,
            farmer TEXT,
            litres REAL,
            fat REAL,
            day TEXT
        )
        """
    )
    return connection


def record_milk(connection, farmer, litres, fat, day):
    """Record a farmer's milk delivery in the ledger."""
    connection.execute(
        """
        INSERT INTO milk (farmer, litres, fat, day)
        VALUES (?, ?, ?, ?)
        """,
        (farmer, litres, fat, day),
    )
    connection.commit()


def farmer_token(farmer):
    """Return a deterministic SHA-256 identifier for a farmer's name."""
    return hashlib.sha256(farmer.encode("utf-8")).hexdigest()


def daily_total(connection, day):
    """Return the total litres collected on a given day."""
    rows = connection.execute(
        "SELECT litres FROM milk WHERE day = ?",
        (day,),
    ).fetchall()
    total_litres = sum(row[0] for row in rows)
    return f"Total: {total_litres:.1f} litres"


def top_farmer(connection):
    """Return the farmer with the greatest total delivery, or None if empty."""
    rows = connection.execute(
        """
        SELECT farmer, SUM(litres)
        FROM milk
        GROUP BY farmer
        ORDER BY SUM(litres) DESC
        LIMIT 1
        """
    ).fetchone()
    return rows[0] if rows else None


def print_slip(farmer):
    """Print a message for the farmer's collection slip."""
    print(f"printing slip for {farmer}")


def low_fat(connection):
    """Return farmers whose recorded milk fat is missing or below 3.5%."""
    rows = connection.execute(
        "SELECT farmer, fat FROM milk"
    ).fetchall()
    return [
        farmer
        for farmer, fat in rows
        if fat is None or fat < 3.5
    ]


def main():
    """Run a short demonstration of the dairy collection ledger."""
    connection = create_connection()
    try:
        record_milk(connection, "Gopal", 12.5, 4.1, "Mon")
        record_milk(connection, "Lata", 20.0, 3.2, "Mon")
        print(
            daily_total(connection, "Mon"),
            top_farmer(connection),
            low_fat(connection),
        )
        print_slip("Gopal")
        print(farmer_token("Lata"))
    finally:
        connection.close()


if __name__ == "__main__":
    main()
