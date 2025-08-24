🚀 Space Mission Launches Analysis

This project performs Exploratory Data Analysis (EDA) and Visualization of global space mission launches using Python, Pandas, and Plotly.

It analyzes launch trends, mission costs, organizations’ contributions, and success rates over time, while providing rich interactive plots for better insights.

📊 Features & Analysis

The script covers the following:

Data Cleaning & Preprocessing

Cleans price data ($, , removal).

Parses mixed date formats.

Extracts year, month, and day from launch dates.

Classifies mission status (Success / Failure).

Extracts country from launch location.

Exploratory Data Analysis (EDA)

📈 Total Launches Over Time
Line chart of launches per year.

🏢 Top Organisations
Top 10 organisations by launches over time.

💰 Mission Cost Trends
Average mission cost per year.

📅 Popular Launch Months
Bar chart of launches by month.

✅ Mission Success Rate
Annual mission success percentage.

🌍 Launches by Country (Bonus)
Choropleth world map showing number of launches by country.

Key Insights

Soviet Union dominated the 1970s & 1980s, while SpaceX dominates recent years.

Mission success rate has significantly improved over decades.

Average mission costs show a declining trend with fluctuations.

Launch activity shows cyclical peaks across decades.

🛠️ Tech Stack

Python

Pandas → Data cleaning & manipulation

Plotly (Express & Graph Objects) → Interactive visualizations

Warnings → Suppressed unnecessary warnings

📂 Dataset

The script expects a dataset file:

mission_launches.csv


Columns used:

Date → Launch date

Price → Mission cost

Organisation → Launching organization

Mission_Status → Mission outcome

Location → Launch site

⚠️ Ensure the file is placed in the same directory as the script.

▶️ How to Run

Clone this repo or download the script.

Install dependencies:

pip install pandas plotly


Place mission_launches.csv in the project folder.

Run the script:

python space_mission_analysis.py


Interactive charts will open in your browser.

📸 Example Visualizations

Launch Trends per Year

Top Organisations by Launches

Mission Costs Over Time

Success Rate Over Time

Launches by Country (World Map)

🔖 Tags

#DataAnalysis #Plotly #SpaceMissions #EDA #Visualization #Pandas
