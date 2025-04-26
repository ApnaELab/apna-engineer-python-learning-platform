import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from utils import lesson_ui, create_code_executor, create_exercise

def lesson_content():
    st.markdown("# Data Analysis with Python")
    
    st.markdown("""
    Data analysis is the process of inspecting, cleaning, transforming, and modeling data to discover useful information, 
    draw conclusions, and support decision-making. Python has become one of the most popular languages for data analysis 
    due to its rich ecosystem of libraries.
    
    In this lesson, we'll explore the fundamental tools for data analysis in Python:
    
    - **Pandas**: For data manipulation and analysis
    - **NumPy**: For numerical computing
    - **SciPy**: For scientific computing
    - **Statsmodels**: For statistical modeling
    """)
    
    st.markdown("## Introduction to Pandas")
    
    st.markdown("""
    Pandas is the most popular library for data manipulation and analysis in Python. It provides data structures 
    for efficiently storing and manipulating tabular data, time series, and matrices.
    
    The primary data structures in pandas are:
    1. **Series**: A one-dimensional labeled array
    2. **DataFrame**: A two-dimensional labeled data structure with columns of potentially different types
    
    Let's start with some basic examples:
    """)
    
    code1 = """import pandas as pd
import numpy as np

# Creating a Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print("Series example:")
print(s)
print()

# Creating a DataFrame from a dictionary
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 42],
    'City': ['New York', 'Paris', 'Berlin', 'London'],
    'Salary': [65000, 70000, 62000, 85000]
}

df = pd.DataFrame(data)
print("DataFrame example:")
print(df)
print()

# Basic information about the DataFrame
print("DataFrame info:")
print(df.info())
print()

print("DataFrame description:")
print(df.describe())
"""
    
    st.code(code1, language='python')
    
    st.markdown("Let's see the outputs:")
    
    # Example Series and DataFrame
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    
    data = {
        'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 34, 29, 42],
        'City': ['New York', 'Paris', 'Berlin', 'London'],
        'Salary': [65000, 70000, 62000, 85000]
    }
    
    df = pd.DataFrame(data)
    
    st.markdown("Series example:")
    st.write(s)
    
    st.markdown("DataFrame example:")
    st.dataframe(df)
    
    st.markdown("DataFrame description:")
    st.write(df.describe())
    
    st.markdown("Try creating and exploring dataframes:")
    create_code_executor(code1)
    
    st.markdown("## Data Loading and Inspection")
    
    st.markdown("""
    Pandas can read data from various file formats including CSV, Excel, SQL databases, JSON, and more.
    For this lesson, we'll simulate loading data:
    """)
    
    code2 = """import pandas as pd
import numpy as np

# Create a simulated dataset
np.random.seed(42)  # For reproducibility
n_samples = 1000

# Create a DataFrame with simulated sales data
dates = pd.date_range('20230101', periods=n_samples)
df = pd.DataFrame({
    'date': dates,
    'product_id': np.random.choice(['P001', 'P002', 'P003', 'P004', 'P005'], n_samples),
    'category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home', 'Food'], n_samples),
    'quantity': np.random.randint(1, 10, n_samples),
    'price': np.round(np.random.uniform(10, 100, n_samples), 2),
    'customer_id': np.random.choice(['C' + str(i).zfill(3) for i in range(1, 201)], n_samples)
})

# Calculate total sales
df['total_sales'] = df['quantity'] * df['price']

# Inspect the data
print("First 5 rows:")
print(df.head())
print()

print("Data information:")
print(df.info())
print()

print("Summary statistics:")
print(df.describe())
print()

print("Check for missing values:")
print(df.isnull().sum())
print()

print("Unique values in categorical columns:")
print("Products:", df['product_id'].nunique())
print("Categories:", df['category'].nunique())
print("Customers:", df['customer_id'].nunique())
"""
    
    st.code(code2, language='python')
    
    # Create a simulated dataset
    np.random.seed(42)
    n_samples = 1000
    
    # Create a DataFrame with simulated sales data
    dates = pd.date_range('20230101', periods=n_samples)
    sales_df = pd.DataFrame({
        'date': dates,
        'product_id': np.random.choice(['P001', 'P002', 'P003', 'P004', 'P005'], n_samples),
        'category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home', 'Food'], n_samples),
        'quantity': np.random.randint(1, 10, n_samples),
        'price': np.round(np.random.uniform(10, 100, n_samples), 2),
        'customer_id': np.random.choice(['C' + str(i).zfill(3) for i in range(1, 201)], n_samples)
    })
    
    # Calculate total sales
    sales_df['total_sales'] = sales_df['quantity'] * sales_df['price']
    
    st.markdown("First 5 rows:")
    st.dataframe(sales_df.head())
    
    st.markdown("Summary statistics:")
    st.write(sales_df.describe())
    
    st.markdown("Unique values in categorical columns:")
    st.write(f"Products: {sales_df['product_id'].nunique()}")
    st.write(f"Categories: {sales_df['category'].nunique()}")
    st.write(f"Customers: {sales_df['customer_id'].nunique()}")
    
    st.markdown("Try loading and inspecting data:")
    create_code_executor(code2)
    
    st.markdown("## Data Manipulation and Transformation")
    
    st.markdown("""
    Pandas provides a rich set of methods for manipulating and transforming data. 
    Let's explore some common operations:
    """)
    
    code3 = """import pandas as pd
import numpy as np

# Continue with our sales dataset
# Let's perform some basic data manipulation

# 1. Filtering data
# Get sales for Electronics category
electronics = df[df['category'] == 'Electronics']
print("Electronics sales (first 5 rows):")
print(electronics.head())
print()

# Get high-value transactions (total_sales > 200)
high_value = df[df['total_sales'] > 200]
print("High-value transactions (first 5 rows):")
print(high_value.head())
print()

# 2. Sorting data
# Sort by total sales (descending)
top_sales = df.sort_values('total_sales', ascending=False)
print("Top sales (first 5 rows):")
print(top_sales.head())
print()

# 3. Adding new columns
# Add a discount column (random discounts)
df['discount'] = np.round(np.random.uniform(0, 0.3, len(df)), 2)
df['discounted_sales'] = df['total_sales'] * (1 - df['discount'])
print("Data with discount (first 5 rows):")
print(df.head())
print()

# 4. Grouping and aggregation
# Total sales by category
category_sales = df.groupby('category')['total_sales'].sum().reset_index()
print("Total sales by category:")
print(category_sales)
print()

# Average quantity and price by product
product_stats = df.groupby('product_id').agg({
    'quantity': 'mean',
    'price': 'mean',
    'total_sales': 'sum'
}).reset_index()
print("Product statistics:")
print(product_stats)
print()

# 5. Pivot tables
# Create a pivot table of total sales by category and product
pivot = df.pivot_table(
    values='total_sales',
    index='category',
    columns='product_id',
    aggfunc='sum'
)
print("Pivot table of sales by category and product:")
print(pivot)
"""
    
    st.code(code3, language='python')
    
    # Data manipulation examples
    st.markdown("Electronics sales (first 5 rows):")
    electronics = sales_df[sales_df['category'] == 'Electronics']
    st.dataframe(electronics.head())
    
    st.markdown("High-value transactions (first 5 rows):")
    high_value = sales_df[sales_df['total_sales'] > 200]
    st.dataframe(high_value.head())
    
    st.markdown("Top sales (first 5 rows):")
    top_sales = sales_df.sort_values('total_sales', ascending=False)
    st.dataframe(top_sales.head())
    
    # Add discount column for demonstration
    sales_df['discount'] = np.round(np.random.uniform(0, 0.3, len(sales_df)), 2)
    sales_df['discounted_sales'] = sales_df['total_sales'] * (1 - sales_df['discount'])
    
    st.markdown("Total sales by category:")
    category_sales = sales_df.groupby('category')['total_sales'].sum().reset_index()
    st.dataframe(category_sales)
    
    st.markdown("Pivot table of sales by category and product:")
    pivot = sales_df.pivot_table(
        values='total_sales',
        index='category',
        columns='product_id',
        aggfunc='sum'
    )
    st.dataframe(pivot)
    
    st.markdown("Try data manipulation techniques:")
    create_code_executor(code3)
    
    st.markdown("## Time Series Analysis")
    
    st.markdown("""
    Pandas has excellent support for time series data. Let's explore some time series analysis:
    """)
    
    code4 = """import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Using our sales data for time series analysis
# First, convert date to datetime if it's not already
df['date'] = pd.to_datetime(df['date'])

# Set the date as index
df_ts = df.set_index('date')
print("Time series data (first 5 rows):")
print(df_ts.head())
print()

# Resample data by day
daily_sales = df_ts['total_sales'].resample('D').sum()
print("Daily sales (first 10 days):")
print(daily_sales.head(10))
print()

# Resample data by month
monthly_sales = df_ts['total_sales'].resample('M').sum()
print("Monthly sales:")
print(monthly_sales)
print()

# Resample by day and plot
plt.figure(figsize=(12, 6))
daily_sales.plot()
plt.title('Daily Sales')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()

# Create a 7-day rolling average
rolling_avg = daily_sales.rolling(window=7).mean()

plt.figure(figsize=(12, 6))
daily_sales.plot(alpha=0.5, label='Daily')
rolling_avg.plot(label='7-day Rolling Average')
plt.title('Daily Sales with 7-day Rolling Average')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.legend()
plt.grid(True)
plt.show()
"""
    
    st.code(code4, language='python')
    
    # Time series analysis examples
    sales_df['date'] = pd.to_datetime(sales_df['date'])
    df_ts = sales_df.set_index('date')
    
    st.markdown("Time series data (first 5 rows):")
    st.dataframe(df_ts.head())
    
    daily_sales = df_ts['total_sales'].resample('D').sum()
    monthly_sales = df_ts['total_sales'].resample('M').sum()
    
    st.markdown("Daily sales (first 10 days):")
    st.dataframe(daily_sales.head(10))
    
    st.markdown("Monthly sales:")
    st.dataframe(monthly_sales)
    
    # Plot daily sales
    fig, ax = plt.subplots(figsize=(12, 6))
    daily_sales.plot(ax=ax)
    ax.set_title('Daily Sales')
    ax.set_xlabel('Date')
    ax.set_ylabel('Total Sales')
    ax.grid(True)
    st.pyplot(fig)
    
    # Plot with rolling average
    rolling_avg = daily_sales.rolling(window=7).mean()
    
    fig, ax = plt.subplots(figsize=(12, 6))
    daily_sales.plot(alpha=0.5, label='Daily', ax=ax)
    rolling_avg.plot(label='7-day Rolling Average', ax=ax)
    ax.set_title('Daily Sales with 7-day Rolling Average')
    ax.set_xlabel('Date')
    ax.set_ylabel('Total Sales')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
    
    st.markdown("Try time series analysis:")
    create_code_executor(code4)
    
    st.markdown("## Basic Statistical Analysis")
    
    st.markdown("""
    Pandas and NumPy provide functions for basic statistical analysis. For more advanced statistics, 
    you can use SciPy and Statsmodels.
    """)
    
    code5 = """import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Using our sales dataset
# Let's perform some statistical analysis

# 1. Basic descriptive statistics
print("Summary statistics for price:")
price_stats = df['price'].describe()
print(price_stats)
print()

print("Correlation matrix:")
corr_matrix = df[['quantity', 'price', 'total_sales', 'discount', 'discounted_sales']].corr()
print(corr_matrix)
print()

# 2. Distribution analysis
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(df['price'], kde=True)
plt.title('Distribution of Prices')
plt.grid(True)

plt.subplot(1, 2, 2)
sns.histplot(df['total_sales'], kde=True)
plt.title('Distribution of Total Sales')
plt.grid(True)

plt.tight_layout()
plt.show()

# 3. Categorical data analysis
# Average sales by category
cat_avg = df.groupby('category')['total_sales'].agg(['mean', 'median', 'std']).reset_index()
print("Statistics by category:")
print(cat_avg)
print()

# 4. T-test: comparing two categories
electronics = df[df['category'] == 'Electronics']['total_sales']
clothing = df[df['category'] == 'Clothing']['total_sales']

t_stat, p_value = stats.ttest_ind(electronics, clothing)
print(f"T-test Electronics vs Clothing: t={t_stat:.4f}, p={p_value:.4f}")
print(f"Mean Electronics: ${electronics.mean():.2f}")
print(f"Mean Clothing: ${clothing.mean():.2f}")
print()

# 5. ANOVA: comparing all categories
categories = df['category'].unique()
category_sales = [df[df['category'] == cat]['total_sales'] for cat in categories]

f_stat, p_value = stats.f_oneway(*category_sales)
print(f"ANOVA for all categories: F={f_stat:.4f}, p={p_value:.4f}")
print()

# 6. Regression analysis
x = df['quantity']
y = df['total_sales']

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print(f"Linear regression: total_sales = {slope:.2f} * quantity + {intercept:.2f}")
print(f"R-squared: {r_value**2:.4f}")

plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.5)
plt.plot(x, intercept + slope*x, 'r')
plt.title('Regression: Quantity vs Total Sales')
plt.xlabel('Quantity')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()
"""
    
    st.code(code5, language='python')
    
    # Statistical analysis examples
    st.markdown("Summary statistics for price:")
    price_stats = sales_df['price'].describe()
    st.write(price_stats)
    
    st.markdown("Correlation matrix:")
    corr_matrix = sales_df[['quantity', 'price', 'total_sales', 'discount', 'discounted_sales']].corr()
    st.dataframe(corr_matrix)
    
    # Distribution analysis
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    
    sns.histplot(sales_df['price'], kde=True, ax=ax[0])
    ax[0].set_title('Distribution of Prices')
    ax[0].grid(True)
    
    sns.histplot(sales_df['total_sales'], kde=True, ax=ax[1])
    ax[1].set_title('Distribution of Total Sales')
    ax[1].grid(True)
    
    plt.tight_layout()
    st.pyplot(fig)
    
    # Categorical data analysis
    cat_avg = sales_df.groupby('category')['total_sales'].agg(['mean', 'median', 'std']).reset_index()
    st.markdown("Statistics by category:")
    st.dataframe(cat_avg)
    
    # T-test example
    electronics = sales_df[sales_df['category'] == 'Electronics']['total_sales']
    clothing = sales_df[sales_df['category'] == 'Clothing']['total_sales']
    
    t_stat, p_value = stats.ttest_ind(electronics, clothing)
    st.markdown(f"T-test Electronics vs Clothing: t={t_stat:.4f}, p={p_value:.4f}")
    st.markdown(f"Mean Electronics: ${electronics.mean():.2f}")
    st.markdown(f"Mean Clothing: ${clothing.mean():.2f}")
    
    # Regression analysis
    x = sales_df['quantity']
    y = sales_df['total_sales']
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    st.markdown(f"Linear regression: total_sales = {slope:.2f} * quantity + {intercept:.2f}")
    st.markdown(f"R-squared: {r_value**2:.4f}")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(x, y, alpha=0.5)
    ax.plot(x, intercept + slope*x, 'r')
    ax.set_title('Regression: Quantity vs Total Sales')
    ax.set_xlabel('Quantity')
    ax.set_ylabel('Total Sales')
    ax.grid(True)
    st.pyplot(fig)
    
    st.markdown("Try statistical analysis:")
    create_code_executor(code5)
    
    st.markdown("## Exercises: Data Analysis")
    
    # First exercise
    exercise1_solution = """import pandas as pd
import numpy as np

# Create the DataFrame
data = {
    'student_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Julia'],
    'math_score': [85, 92, 78, 96, 88, 72, 91, 86, 79, 94],
    'science_score': [92, 88, 76, 93, 90, 69, 87, 89, 75, 91],
    'english_score': [88, 90, 84, 91, 93, 75, 86, 90, 82, 89]
}

df = pd.DataFrame(data)

# Calculate the average score for each student
df['average_score'] = (df['math_score'] + df['science_score'] + df['english_score']) / 3
df['average_score'] = df['average_score'].round(2)

# Sort by average score in descending order
df_sorted = df.sort_values('average_score', ascending=False)

# Print the top 3 students
print("Top 3 students by average score:")
print(df_sorted[['name', 'average_score']].head(3))

# Calculate overall class average for each subject
subject_avgs = {
    'Math': df['math_score'].mean(),
    'Science': df['science_score'].mean(),
    'English': df['english_score'].mean(),
    'Overall': df['average_score'].mean()
}

print("\\nClass averages:")
for subject, avg in subject_avgs.items():
    print(f"{subject}: {avg:.2f}")"""

    exercise1_passed = create_exercise(
        "Create a DataFrame with student grades data (10 students) including student_id, name, and scores for math, science, and english. Calculate the average score for each student, sort by average score, and display the top 3 students. Also calculate the class average for each subject.",
        exercise1_solution
    )
    
    # Second exercise
    if exercise1_passed:
        exercise2_solution = """import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create date range and simulated sales data
np.random.seed(42)
dates = pd.date_range(start='2023-01-01', periods=365, freq='D')

sales_data = pd.DataFrame({
    'date': dates,
    'daily_sales': np.random.normal(1000, 200, 365) + np.sin(np.linspace(0, 4*np.pi, 365)) * 200
})

# Set date as index
sales_data = sales_data.set_index('date')

# Calculate 7-day moving average
sales_data['7day_avg'] = sales_data['daily_sales'].rolling(window=7).mean()

# Resample to get monthly sales
monthly_sales = sales_data['daily_sales'].resample('M').sum()

# Plot daily sales and moving average
plt.figure(figsize=(12, 6))
plt.plot(sales_data.index, sales_data['daily_sales'], alpha=0.5, label='Daily Sales')
plt.plot(sales_data.index, sales_data['7day_avg'], linewidth=2, label='7-day Moving Average')
plt.title('Daily Sales with 7-day Moving Average')
plt.xlabel('Date')
plt.ylabel('Sales Amount')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Print monthly sales summary
print("Monthly Sales Summary:")
print(monthly_sales)

# Calculate growth rate for each month
monthly_pct_change = monthly_sales.pct_change() * 100
print("\\nMonthly Growth Rate (%):")
print(monthly_pct_change.dropna())

# Identify the month with highest and lowest sales
max_month = monthly_sales.idxmax()
min_month = monthly_sales.idxmin()

print(f"\\nMonth with highest sales: {max_month.strftime('%B %Y')}: ${monthly_sales[max_month]:.2f}")
print(f"Month with lowest sales: {min_month.strftime('%B %Y')}: ${monthly_sales[min_month]:.2f}")"""

        exercise2_passed = create_exercise(
            "Create a time series dataset of daily sales for a full year (365 days) with random fluctuations and seasonal patterns. Calculate a 7-day moving average and plot both the daily sales and the moving average. Additionally, resample the data to find monthly sales totals and identify which month had the highest and lowest sales.",
            exercise2_solution
        )
    else:
        exercise2_passed = False
    
    return exercise1_passed and exercise2_passed

# Render the lesson using the utility function
lesson_ui("Data Analysis", lesson_content)
