import sqlite3

def init_db():
    conn = sqlite3.connect('data/legacy_corp.db')
    cursor = conn.cursor()
    
    # Simulating a typical legacy table: Uppercase, underscores, messy formats
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS T_CUSTOMERS_STG (
            CUST_ID INTEGER PRIMARY KEY,
            FULL_NAME TEXT,
            STATUS_CODE TEXT, -- 'A' for Active, 'I' for Inactive
            LAST_UPDATED TEXT  -- Format: YYYYMMDD (Legacy style)
        )
    ''')
    
    # Insert some mock data
    mock_data = [
        (101, 'PAPADOPOULOS IOANNIS', 'A', '20231201'),
        (102, 'SMITH MARIA', 'I', '20231115'),
        (103, 'GEORGIOU NIKOS', 'A', '20240110')
    ]
    
    cursor.executemany('INSERT OR REPLACE INTO T_CUSTOMERS_STG VALUES (?,?,?,?)', mock_data)
    conn.commit()
    conn.close()
    print("Legacy Mock DB initialized in /data/legacy_corp.db")

if __name__ == "__main__":
    init_db()