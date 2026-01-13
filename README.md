# Airbnb Marketplace Supply Health Analysis

## Objective
Analyse marketplace supply health by distinguishing between active listings (retention/utilisation) and new supply creation.

## Data Source
Data sourced from Inside Airbnb (open data):
https://insideairbnb.com/get-the-data/

Calendar data was filtered to a single year (2025) for analysis due to file size constraints.
Raw CSV files are not included in this repository.

## Methodology
- SQL (DuckDB) used for aggregation and cohort-style analysis
- Python used for orchestration and exporting outputs
- Metrics computed:
  - Monthly active listings (distinct listings booked at least once)
  - Monthly new listings (by creation date)

## Key Outputs
- `monthly_active_listings.csv`
- `monthly_new_listings.csv`

## Tools
Python, DuckDB, SQL, Pandas
Update README
