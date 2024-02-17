import mysql.connector
from db_utils import get_connection, close_connection


def with_db_connection(func):
    def wrapper(*args, **kwargs):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                # Pass the cursor to the decorated function
                return func(cursor, *args, **kwargs)
        finally:
            close_connection(connection)

    return wrapper


@with_db_connection
def read_sources(cursor):
    # Example function to read sources from the MySQL table
    cursor.execute("SELECT id, source_name FROM sources")
    return cursor.fetchall()


@with_db_connection
def perform_operation(cursor, source_id, source_name):
    # Example function to perform an operation on each source
    print(f"Performing operation on source {source_id}: {source_name}")
    # Perform your operation here


@with_db_connection
def update_source(cursor, source_id, new_source_name):
    # Example function to update the source in the MySQL table
    cursor.execute("UPDATE sources SET source_name = %s WHERE id = %s", (new_source_name, source_id))


def main():
    # Read sources from the table
    sources = read_sources()

    for source_id, source_name in sources:
        # Perform operation on each source
        perform_operation(source_id, source_name)

        # Update the source in the table
        new_source_name = f"Updated_{source_name}"
        update_source(source_id, new_source_name)


if __name__ == "__main__":
    main()
