import json
import pandas as pd
import pendulum

# Load the data
with open('C:/projects/battle-tube-2-analysis/data/scrapping-all.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create a DataFrame
df = pd.DataFrame(data)

# Convert created_at to datetime (UTC)
df['created_at'] = pd.to_datetime(df['created_at'])

# Define timezone
timezone = 'America/Sao_Paulo'

# Function to convert to local date
def get_local_date(dt):
    # Ensure it's timezone aware (UTC) then convert
    if dt.tz is None:
        dt = dt.tz_localize('UTC')
    return dt.tz_convert(timezone).date()

# Apply conversion
df['local_date'] = df['created_at'].apply(get_local_date)

# Count clips per day
daily_counts = df['local_date'].value_counts().sort_values(ascending=False)

print("Top 5 Days with Most Clips (America/Sao_Paulo):")
print(daily_counts.head(5))

# Check specific dates
date_1 = pd.to_datetime('2025-01-26').date()
date_2 = pd.to_datetime('2025-07-12').date()

print(f"\nCounts for specific dates:")
if date_1 in daily_counts.index:
    print(f"{date_1}: {daily_counts[date_1]}")
else:
    print(f"{date_1}: 0")

if date_2 in daily_counts.index:
    print(f"{date_2}: {daily_counts[date_2]}")
else:
    print(f"{date_2}: 0")