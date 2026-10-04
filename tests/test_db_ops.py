import sqlite3

import pytest

import db_ops


@pytest.fixture
def connection():
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    yield conn
    conn.close()


def test_create_table_and_insert(connection):
    db_ops.create_table(connection, "users", {"id": "INTEGER PRIMARY KEY", "name": "TEXT"})
    assert db_ops.table_exists(connection, "users") is True
    row_id = db_ops.insert_record(connection, "users", {"name": "Ada"})
    assert row_id == 1


def test_fetch_all_and_count(connection):
    db_ops.create_table(connection, "users", {"id": "INTEGER PRIMARY KEY", "name": "TEXT"})
    db_ops.insert_record(connection, "users", {"name": "Ada"})
    db_ops.insert_record(connection, "users", {"name": "Grace"})
    assert db_ops.count_records(connection, "users") == 2
    rows = db_ops.fetch_all(connection, "users")
    assert len(rows) == 2


def test_update_and_delete_record(connection):
    db_ops.create_table(connection, "users", {"id": "INTEGER PRIMARY KEY", "name": "TEXT"})
    row_id = db_ops.insert_record(connection, "users", {"name": "Ada"})
    affected = db_ops.update_record(connection, "users", row_id, {"name": "Ada Lovelace"})
    assert affected == 1
    row = db_ops.fetch_by_id(connection, "users", row_id)
    assert row["name"] == "Ada Lovelace"
    deleted = db_ops.delete_record(connection, "users", row_id)
    assert deleted == 1
    assert db_ops.count_records(connection, "users") == 0


def test_bulk_insert(connection):
    db_ops.create_table(connection, "users", {"id": "INTEGER PRIMARY KEY", "name": "TEXT"})
    inserted = db_ops.bulk_insert(
        connection, "users", [{"name": "Ada"}, {"name": "Grace"}, {"name": "Linus"}]
    )
    assert inserted == 3
    assert db_ops.count_records(connection, "users") == 3
