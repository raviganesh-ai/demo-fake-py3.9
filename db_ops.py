"""
db_ops.py - A collection of SQLite database operation helpers.

Written for Python 3.9. Uses the stdlib sqlite3 module and
typing.List/Optional/Tuple/Dict/Any in the pre-3.10 style.
"""
import csv
import os
import sqlite3
from typing import Any, Dict, List, Optional, Tuple


def get_connection(db_path: str) -> sqlite3.Connection:
    """Open and return a connection to the SQLite database at db_path."""
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    return connection


def close_connection(connection: sqlite3.Connection) -> None:
    """Close an open database connection."""
    connection.close()


def create_table(connection: sqlite3.Connection, table_name: str, columns: Dict[str, str]) -> None:
    """Create a table with the given column name -> type mapping if it doesn't exist."""
    column_defs = ", ".join(f"{name} {col_type}" for name, col_type in columns.items())
    connection.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({column_defs})")
    connection.commit()


def drop_table(connection: sqlite3.Connection, table_name: str) -> None:
    """Drop a table if it exists."""
    connection.execute(f"DROP TABLE IF EXISTS {table_name}")
    connection.commit()


def table_exists(connection: sqlite3.Connection, table_name: str) -> bool:
    """Return True if the given table exists in the database."""
    cursor = connection.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,)
    )
    return cursor.fetchone() is not None


def list_tables(connection: sqlite3.Connection) -> List[str]:
    """Return the names of all user tables in the database."""
    cursor = connection.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
    )
    return [row[0] for row in cursor.fetchall()]


def get_table_schema(connection: sqlite3.Connection, table_name: str) -> List[Tuple[Any, ...]]:
    """Return the schema (column info) for a table."""
    cursor = connection.execute(f"PRAGMA table_info({table_name})")
    return cursor.fetchall()


def column_exists(connection: sqlite3.Connection, table_name: str, column_name: str) -> bool:
    """Return True if the given column exists on the given table."""
    schema = get_table_schema(connection, table_name)
    return any(column[1] == column_name for column in schema)


def add_column(connection: sqlite3.Connection, table_name: str, column_name: str, column_type: str) -> None:
    """Add a new column to an existing table."""
    connection.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}")
    connection.commit()


def rename_table(connection: sqlite3.Connection, old_name: str, new_name: str) -> None:
    """Rename a table."""
    connection.execute(f"ALTER TABLE {old_name} RENAME TO {new_name}")
    connection.commit()


def create_index(connection: sqlite3.Connection, index_name: str, table_name: str, column_name: str) -> None:
    """Create an index on a column."""
    connection.execute(f"CREATE INDEX IF NOT EXISTS {index_name} ON {table_name} ({column_name})")
    connection.commit()


def drop_index(connection: sqlite3.Connection, index_name: str) -> None:
    """Drop an index if it exists."""
    connection.execute(f"DROP INDEX IF EXISTS {index_name}")
    connection.commit()


def insert_record(connection: sqlite3.Connection, table_name: str, record: Dict[str, Any]) -> int:
    """Insert a record (column -> value mapping) and return its row id."""
    columns = ", ".join(record.keys())
    placeholders = ", ".join("?" for _ in record)
    values = tuple(record.values())
    cursor = connection.execute(
        f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})", values
    )
    connection.commit()
    return cursor.lastrowid


def bulk_insert(connection: sqlite3.Connection, table_name: str, records: List[Dict[str, Any]]) -> int:
    """Insert multiple records in a single transaction. Returns the count inserted."""
    if not records:
        return 0
    columns = ", ".join(records[0].keys())
    placeholders = ", ".join("?" for _ in records[0])
    values = [tuple(record.values()) for record in records]
    connection.executemany(
        f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})", values
    )
    connection.commit()
    return len(records)


def update_record(
    connection: sqlite3.Connection,
    table_name: str,
    record_id: int,
    updates: Dict[str, Any],
    id_column: str = "id",
) -> int:
    """Update a record by id. Returns the number of rows affected."""
    set_clause = ", ".join(f"{column} = ?" for column in updates)
    values = tuple(updates.values()) + (record_id,)
    cursor = connection.execute(
        f"UPDATE {table_name} SET {set_clause} WHERE {id_column} = ?", values
    )
    connection.commit()
    return cursor.rowcount


def bulk_update(
    connection: sqlite3.Connection,
    table_name: str,
    updates: Dict[str, Any],
    where_column: str,
    where_value: Any,
) -> int:
    """Update every record matching where_column = where_value. Returns rows affected."""
    set_clause = ", ".join(f"{column} = ?" for column in updates)
    values = tuple(updates.values()) + (where_value,)
    cursor = connection.execute(
        f"UPDATE {table_name} SET {set_clause} WHERE {where_column} = ?", values
    )
    connection.commit()
    return cursor.rowcount


def delete_record(connection: sqlite3.Connection, table_name: str, record_id: int, id_column: str = "id") -> int:
    """Delete a record by id. Returns the number of rows affected."""
    cursor = connection.execute(f"DELETE FROM {table_name} WHERE {id_column} = ?", (record_id,))
    connection.commit()
    return cursor.rowcount


def bulk_delete(connection: sqlite3.Connection, table_name: str, where_column: str, where_value: Any) -> int:
    """Delete every record matching where_column = where_value. Returns rows affected."""
    cursor = connection.execute(f"DELETE FROM {table_name} WHERE {where_column} = ?", (where_value,))
    connection.commit()
    return cursor.rowcount


def fetch_all(connection: sqlite3.Connection, table_name: str) -> List[sqlite3.Row]:
    """Fetch every record from a table."""
    cursor = connection.execute(f"SELECT * FROM {table_name}")
    return cursor.fetchall()


def fetch_one(connection: sqlite3.Connection, table_name: str, record_id: int, id_column: str = "id") -> Optional[sqlite3.Row]:
    """Fetch a single record by id, or None if not found."""
    cursor = connection.execute(f"SELECT * FROM {table_name} WHERE {id_column} = ?", (record_id,))
    return cursor.fetchone()


def fetch_by_id(connection: sqlite3.Connection, table_name: str, record_id: int) -> Optional[sqlite3.Row]:
    """Alias of fetch_one using the default 'id' column."""
    return fetch_one(connection, table_name, record_id)


def search_records(connection: sqlite3.Connection, table_name: str, column: str, pattern: str) -> List[sqlite3.Row]:
    """Search a table for records whose column matches a LIKE pattern."""
    cursor = connection.execute(f"SELECT * FROM {table_name} WHERE {column} LIKE ?", (pattern,))
    return cursor.fetchall()


def paginate_records(connection: sqlite3.Connection, table_name: str, page: int, page_size: int) -> List[sqlite3.Row]:
    """Return a page of records from a table."""
    offset = (page - 1) * page_size
    cursor = connection.execute(f"SELECT * FROM {table_name} LIMIT ? OFFSET ?", (page_size, offset))
    return cursor.fetchall()


def count_records(connection: sqlite3.Connection, table_name: str) -> int:
    """Return the number of records in a table."""
    cursor = connection.execute(f"SELECT COUNT(*) FROM {table_name}")
    return cursor.fetchone()[0]


def execute_query(connection: sqlite3.Connection, query: str, params: Tuple[Any, ...] = ()) -> List[sqlite3.Row]:
    """Execute an arbitrary SELECT query and return all rows."""
    cursor = connection.execute(query, params)
    return cursor.fetchall()


def execute_many(connection: sqlite3.Connection, query: str, params_list: List[Tuple[Any, ...]]) -> int:
    """Execute the same statement for many parameter sets. Returns rows affected."""
    cursor = connection.executemany(query, params_list)
    connection.commit()
    return cursor.rowcount


def execute_script(connection: sqlite3.Connection, script: str) -> None:
    """Execute a multi-statement SQL script."""
    connection.executescript(script)
    connection.commit()


def begin_transaction(connection: sqlite3.Connection) -> None:
    """Begin an explicit transaction."""
    connection.execute("BEGIN TRANSACTION")


def commit_transaction(connection: sqlite3.Connection) -> None:
    """Commit the current transaction."""
    connection.commit()


def rollback_transaction(connection: sqlite3.Connection) -> None:
    """Roll back the current transaction."""
    connection.rollback()


def get_last_insert_id(connection: sqlite3.Connection) -> int:
    """Return the row id of the most recently inserted row."""
    cursor = connection.execute("SELECT last_insert_rowid()")
    return cursor.fetchone()[0]


def check_connection_health(connection: sqlite3.Connection) -> bool:
    """Return True if the connection can execute a trivial query."""
    try:
        connection.execute("SELECT 1")
        return True
    except sqlite3.Error:
        return False


def backup_database(connection: sqlite3.Connection, backup_path: str) -> None:
    """Back up the database to another file."""
    backup_connection = sqlite3.connect(backup_path)
    with backup_connection:
        connection.backup(backup_connection)
    backup_connection.close()


def restore_database(backup_path: str, target_path: str) -> None:
    """Restore a database from a backup file by copying it."""
    with open(backup_path, "rb") as source, open(target_path, "wb") as destination:
        destination.write(source.read())


def get_database_size(db_path: str) -> int:
    """Return the size in bytes of a database file on disk."""
    return os.path.getsize(db_path)


def vacuum_database(connection: sqlite3.Connection) -> None:
    """Reclaim unused space in the database file."""
    connection.execute("VACUUM")


def optimize_database(connection: sqlite3.Connection) -> None:
    """Run the SQLite query planner optimizer."""
    connection.execute("PRAGMA optimize")


def export_to_csv(connection: sqlite3.Connection, table_name: str, csv_path: str) -> int:
    """Export a table's contents to a CSV file. Returns the number of rows written."""
    rows = fetch_all(connection, table_name)
    if not rows:
        return 0
    with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(rows[0].keys())
        for row in rows:
            writer.writerow(tuple(row))
    return len(rows)


def import_from_csv(connection: sqlite3.Connection, table_name: str, csv_path: str) -> int:
    """Import rows from a CSV file into a table. Returns the number of rows inserted."""
    with open(csv_path, "r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        records = [dict(row) for row in reader]
    return bulk_insert(connection, table_name, records)
