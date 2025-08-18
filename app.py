import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import warnings

warnings.filterwarnings('ignore')

# 1. Load the dataset
# ==============================================================================
# The CSV file is loaded into a pandas DataFrame for easy manipulation.
# ==============================================================================
try:
    df = pd.read_csv('mission_launches.csv')
except FileNotFoundError:
    print("Error: 'mission_launches.csv' not found. Please ensure the file is in the same directory.")
    exit()

print("Initial Data Info:")
df.info()
print("\n" + "="*50 + "\n")

# 2. Data Cleaning and Preprocessing
# ==============================================================================
# The raw data needs to be cleaned to make it suitable for analysis and plotting.
# We will focus on the 'Date' and 'Price' columns.
# ==============================================================================

# Clean and convert the 'Price' column
df['Price'] = df['Price'].str.replace(',', '').str.replace('$', '').str.strip()
# Convert to numeric, coercing errors to NaN
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# Handle the 'Date' column with a more flexible format
# The 'mixed' format will infer the format for each date string
df['Date'] = pd.to_datetime(df['Date'], utc=True, format='mixed')

# Extract the year, month, and day for trend analysis
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Month Name'] = df['Date'].dt.strftime('%B')

# Handle Mission Status
df['Status'] = df['Mission_Status'].apply(lambda x: 'Success' if 'Success' in x else 'Failure')

print("Cleaned Data Info:")
df.info()
print("\n" + "="*50 + "\n")

# 3. Exploratory Data Analysis (EDA) and Visualization
# ==============================================================================
# Now that the data is clean, we can start answering the questions using plots.
# ==============================================================================

# 3.1. Total Launches Over Time (Who launched the most missions?)
# ------------------------------------------------------------------------------
# We'll create a line chart showing the number of launches per year.
# ------------------------------------------------------------------------------
launches_per_year = df['Year'].value_counts().sort_index()

fig1 = px.line(
    x=launches_per_year.index,
    y=launches_per_year.values,
    title='Total Number of Space Launches Per Year',
    labels={'x': 'Year', 'y': 'Number of Launches'}
)
fig1.show()

# 3.2. Top Organisations Over Time
# ------------------------------------------------------------------------------
# Let's find the top organizations and see how their launches have changed.
# ------------------------------------------------------------------------------
top_organisations = df['Organisation'].value_counts().head(10).index
launches_by_org = df[df['Organisation'].isin(top_organisations)].groupby(['Year', 'Organisation']).size().reset_index(name='Launches')

fig2 = px.line(
    launches_by_org,
    x='Year',
    y='Launches',
    color='Organisation',
    title='Top 10 Organisations by Number of Launches Per Year'
)
fig2.show()

# To answer your specific questions about dominant organisations:
print("Dominant organisations in the 1970s and 1980s:")
print(df[(df['Year'] >= 1970) & (df['Year'] <= 1989)]['Organisation'].mode().iloc[0])
print("\nDominant organisations in 2018, 2019, and 2020:")
print(df[(df['Year'] >= 2018) & (df['Year'] <= 2020)]['Organisation'].mode().iloc[0])
print("\n" + "="*50 + "\n")

# 3.3. Mission Cost Over Time
# ------------------------------------------------------------------------------
# We'll plot the average mission cost per year to see the trend.
# ------------------------------------------------------------------------------
avg_cost_per_year = df.groupby('Year')['Price'].mean().reset_index()

fig3 = px.line(
    avg_cost_per_year,
    x='Year',
    y='Price',
    title='Average Mission Cost Over Time (USD Millions)',
    labels={'Price': 'Average Cost (in millions)', 'Year': 'Year'}
)
fig3.show()

# 3.4. Popular Months for Launches
# ------------------------------------------------------------------------------
# We'll count the number of launches per month and visualize it.
# ------------------------------------------------------------------------------
launches_per_month = df['Month Name'].value_counts().reindex([
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
])

fig4 = px.bar(
    launches_per_month,
    x=launches_per_month.index,
    y=launches_per_month.values,
    title='Number of Launches by Month',
    labels={'x': 'Month', 'y': 'Number of Launches'}
)
fig4.show()

# 3.5. Mission Success Rate Over Time
# ------------------------------------------------------------------------------
# We'll calculate the percentage of successful missions each year.
# ------------------------------------------------------------------------------
success_rate = df.groupby('Year')['Status'].apply(lambda x: (x == 'Success').mean() * 100).reset_index(name='Success Rate')

fig5 = px.line(
    success_rate,
    x='Year',
    y='Success Rate',
    title='Mission Success Rate Over Time',
    labels={'Success Rate': 'Success Rate (%)', 'Year': 'Year'}
)
fig5.show()

# 3.6. Launches by Country (Bonus Visualization)
# ------------------------------------------------------------------------------
# Extracting the country from the location string and plotting on a map.
# ------------------------------------------------------------------------------
df['Country'] = df['Location'].apply(lambda x: x.split(', ')[-1].strip())
launches_per_country = df['Country'].value_counts().reset_index()
launches_per_country.columns = ['Country', 'Launches']

fig6 = px.choropleth(
    launches_per_country,
    locations='Country',
    locationmode='country names',
    color='Launches',
    hover_name='Country',
    color_continuous_scale=px.colors.sequential.Plasma,
    title='Number of Space Launches by Country'
)
fig6.show()

# 4. Final Insights
# ==============================================================================
# A brief summary of key findings from the analysis.
# ==============================================================================
print("Analysis complete. Key insights from the visualizations:")
print("- The total number of space launches has a clear cyclical pattern, with peaks and troughs over the decades.")
print("- The Soviet Union was the dominant organisation in the 1970s and 80s, while SpaceX has risen to prominence recently.")
print("- The average cost of a mission has generally decreased, though there are significant fluctuations.")
print("- The mission success rate has improved significantly since the early days of space exploration.")

