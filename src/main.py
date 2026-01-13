import duckdb
import pandas as pd

# Paths to the CSV files
calendar_csv_path = 'attached_assets/calendar-2025_1768252689924.csv'
listings_csv_path = 'attached_assets/listings_1768255458526.csv'

# Initialize DuckDB connection
con = duckdb.connect()

# 1. Monthly Active Listings (from calendar)
active_listings_query = f"""
SELECT 
    strftime(date::DATE, '%Y-%m') as month,
    count(distinct listing_id) as active_listings
FROM read_csv_auto('{calendar_csv_path}')
WHERE available = 'f'
GROUP BY 1
ORDER BY 1
"""

# 2. Monthly New Listings (from listings)
# host_since is the column used for listing creation date context (assuming first listing date)
new_listings_query = f"""
SELECT 
    strftime(host_since::DATE, '%Y-%m') as month,
    count(distinct id) as new_listings
FROM read_csv_auto('{listings_csv_path}')
WHERE host_since IS NOT NULL
GROUP BY 1
ORDER BY 1
"""

# 3. Join Data for future host-level analysis
# This creates a view combining supply health (active status) with host metadata
join_query = f"""
CREATE OR REPLACE VIEW supply_analysis AS
SELECT 
    c.listing_id,
    c.date,
    c.available,
    l.host_id,
    l.host_since,
    l.neighbourhood_cleansed
FROM read_csv_auto('{calendar_csv_path}') c
JOIN read_csv_auto('{listings_csv_path}') l ON c.listing_id = l.id
"""

# Execute queries
active_df = con.execute(active_listings_query).df()
active_df.to_csv("monthly_active_listings.csv", index=False)

new_listings_df = con.execute(new_listings_query).df()
new_listings_df.to_csv("monthly_new_listings.csv", index=False)

con.execute(join_query)

print("Monthly Active Listings (First 10 rows):")
print(active_df.head(10))

print("\nMonthly New Listings (First 10 rows):")
print(new_listings_df.head(10))

print("\nSupply Analysis View Created (listing + host join)")
