import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from utils import lesson_ui, create_code_executor, create_exercise

def lesson_content():
    st.markdown("# Data Visualization in Python")
    
    st.markdown("""
    Data visualization is a powerful way to understand and communicate insights from your data. 
    Python offers several excellent libraries for creating visualizations:
    
    - **Matplotlib**: The foundation for most Python plotting libraries
    - **Seaborn**: Statistical data visualization built on matplotlib
    - **Pandas**: Built-in plotting functionality for DataFrames
    - **Plotly**: Interactive visualizations
    - **Bokeh**: Interactive web visualizations
    
    In this lesson, we'll focus on Matplotlib, Seaborn, and Pandas for visualizing data.
    """)
    
    st.markdown("## Introduction to Matplotlib")
    
    st.markdown("""
    Matplotlib is the most widely used Python library for creating static, animated, and interactive visualizations.
    Let's start with some basic examples:
    """)
    
    # Basic line plot example
    code1 = """import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y = np.sin(x)                # sine function

# Create a figure and axes
plt.figure(figsize=(10, 6))

# Plot the data
plt.plot(x, y, label='sin(x)')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Basic Line Plot: Sine Function')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
"""
    
    st.code(code1, language='python')
    
    # Execute and display the matplotlib plot directly in Streamlit
    st.markdown("Output:")
    
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, label='sin(x)')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Basic Line Plot: Sine Function')
    ax.legend()
    ax.grid(True)
    
    st.pyplot(fig)
    
    st.markdown("Try it yourself (customize the plot as you wish):")
    create_code_executor(code1)
    
    st.markdown("## Multiple Plots and Customization")
    
    st.markdown("""
    Matplotlib allows you to create multiple plots and customize them in various ways:
    """)
    
    code2 = """import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create figure and axes
plt.figure(figsize=(12, 8))

# First subplot
plt.subplot(2, 1, 1)  # (rows, columns, index)
plt.plot(x, y1, 'b-', linewidth=2, label='sin(x)')
plt.title('Sine Function')
plt.grid(True)
plt.legend()

# Second subplot
plt.subplot(2, 1, 2)
plt.plot(x, y2, 'r--', linewidth=2, label='cos(x)')
plt.title('Cosine Function')
plt.grid(True)
plt.legend()

# Adjust layout and show
plt.tight_layout()
plt.show()
"""
    
    st.code(code2, language='python')
    
    st.markdown("Output:")
    
    # Multiple plots example
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    
    ax1.plot(x, y1, 'b-', linewidth=2, label='sin(x)')
    ax1.set_title('Sine Function')
    ax1.grid(True)
    ax1.legend()
    
    ax2.plot(x, y2, 'r--', linewidth=2, label='cos(x)')
    ax2.set_title('Cosine Function')
    ax2.grid(True)
    ax2.legend()
    
    plt.tight_layout()
    st.pyplot(fig)
    
    st.markdown("Try creating subplots:")
    create_code_executor(code2)
    
    st.markdown("## Different Types of Plots")
    
    st.markdown("""
    Matplotlib and Seaborn support many different types of visualizations. Here are some common ones:
    """)
    
    code3 = """import matplotlib.pyplot as plt
import numpy as np

# Generate data
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 47, 12, 36, 29]

# Bar chart
plt.figure(figsize=(10, 6))
plt.bar(categories, values, color='skyblue')
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Scatter plot
plt.figure(figsize=(10, 6))
x = np.random.rand(50)
y = x + np.random.normal(0, 0.3, 50)
plt.scatter(x, y, alpha=0.6, s=100, c='green', edgecolors='black')
plt.title('Scatter Plot Example')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True)
plt.show()

# Pie chart
plt.figure(figsize=(10, 6))
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90, 
        shadow=True, explode=[0, 0.1, 0, 0, 0], colors=plt.cm.Paired.colors)
plt.title('Pie Chart Example')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
plt.show()
"""
    
    st.code(code3, language='python')
    
    st.markdown("Bar Chart Output:")
    
    # Bar chart
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [23, 47, 12, 36, 29]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(categories, values, color='skyblue')
    ax.set_title('Bar Chart Example')
    ax.set_xlabel('Categories')
    ax.set_ylabel('Values')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig)
    
    st.markdown("Scatter Plot Output:")
    
    # Scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.random.rand(50)
    y = x + np.random.normal(0, 0.3, 50)
    ax.scatter(x, y, alpha=0.6, s=100, c='green', edgecolors='black')
    ax.set_title('Scatter Plot Example')
    ax.set_xlabel('X values')
    ax.set_ylabel('Y values')
    ax.grid(True)
    st.pyplot(fig)
    
    st.markdown("Pie Chart Output:")
    
    # Pie chart
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.pie(values, labels=categories, autopct='%1.1f%%', startangle=90, 
          shadow=True, explode=[0, 0.1, 0, 0, 0], colors=plt.cm.Paired.colors)
    ax.set_title('Pie Chart Example')
    ax.axis('equal')
    st.pyplot(fig)
    
    st.markdown("Try creating these different charts:")
    create_code_executor(code3)
    
    st.markdown("## Data Visualization with Pandas")
    
    st.markdown("""
    Pandas provides convenient plotting functions that build on Matplotlib. Let's see some examples:
    """)
    
    code4 = """import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a DataFrame
np.random.seed(42)  # For reproducibility
dates = pd.date_range('20230101', periods=12)
df = pd.DataFrame({
    'A': np.random.randn(12).cumsum(),
    'B': np.random.randn(12).cumsum(),
    'C': np.random.randn(12).cumsum(),
    'D': np.random.randn(12).cumsum()
}, index=dates)

print("Sample DataFrame:")
print(df.head())

# Line plot with Pandas
ax = df.plot(figsize=(10, 6), title='Line Plot with Pandas')
ax.set_xlabel('Date')
ax.set_ylabel('Value')
ax.grid(True)
plt.show()

# Bar plot with Pandas
ax = df.iloc[0].plot(kind='bar', figsize=(10, 6), color='skyblue', 
                    title='Bar Plot with Pandas')
ax.set_xlabel('Column')
ax.set_ylabel('Value')
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Area plot with Pandas
ax = df.plot.area(figsize=(10, 6), alpha=0.5, title='Area Plot with Pandas')
ax.set_xlabel('Date')
ax.set_ylabel('Value')
ax.grid(True)
plt.show()
"""
    
    st.code(code4, language='python')
    
    # Create a sample DataFrame
    np.random.seed(42)
    dates = pd.date_range('20230101', periods=12)
    df = pd.DataFrame({
        'A': np.random.randn(12).cumsum(),
        'B': np.random.randn(12).cumsum(),
        'C': np.random.randn(12).cumsum(),
        'D': np.random.randn(12).cumsum()
    }, index=dates)
    
    st.markdown("Sample DataFrame:")
    st.dataframe(df.head())
    
    st.markdown("Line Plot Output:")
    fig, ax = plt.subplots(figsize=(10, 6))
    df.plot(ax=ax, title='Line Plot with Pandas')
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.grid(True)
    st.pyplot(fig)
    
    st.markdown("Bar Plot Output:")
    fig, ax = plt.subplots(figsize=(10, 6))
    df.iloc[0].plot(kind='bar', ax=ax, color='skyblue', title='Bar Plot with Pandas')
    ax.set_xlabel('Column')
    ax.set_ylabel('Value')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig)
    
    st.markdown("Area Plot Output:")
    fig, ax = plt.subplots(figsize=(10, 6))
    df.plot.area(ax=ax, alpha=0.5, title='Area Plot with Pandas')
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.grid(True)
    st.pyplot(fig)
    
    st.markdown("Try creating pandas visualizations:")
    create_code_executor(code4)
    
    st.markdown("## Statistical Visualization with Seaborn")
    
    st.markdown("""
    Seaborn is a statistical data visualization library built on top of Matplotlib. 
    It provides a high-level interface for drawing attractive and informative statistical graphics.
    """)
    
    code5 = """import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set the theme
sns.set_theme(style="whitegrid")

# Create sample dataset
np.random.seed(42)
tips = pd.DataFrame({
    'total_bill': np.random.uniform(10, 50, 100),
    'tip': np.random.uniform(1, 10, 100),
    'sex': np.random.choice(['Male', 'Female'], 100),
    'smoker': np.random.choice(['Yes', 'No'], 100),
    'day': np.random.choice(['Sun', 'Sat', 'Fri', 'Thur'], 100),
    'time': np.random.choice(['Dinner', 'Lunch'], 100),
    'size': np.random.choice([1, 2, 3, 4, 5, 6], 100)
})

print("Tips Dataset (first 5 rows):")
print(tips.head())

# Simple scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='total_bill', y='tip', hue='time', style='time', 
                s=100, data=tips)
plt.title('Scatter Plot of Tips vs Total Bill')
plt.show()

# Regression plot
plt.figure(figsize=(10, 6))
sns.regplot(x='total_bill', y='tip', data=tips, scatter_kws={'alpha':0.5})
plt.title('Regression Plot with Confidence Interval')
plt.show()

# Box plot
plt.figure(figsize=(12, 6))
sns.boxplot(x='day', y='total_bill', hue='time', data=tips)
plt.title('Box Plot of Total Bill by Day and Time')
plt.show()

# Violin plot
plt.figure(figsize=(12, 6))
sns.violinplot(x='day', y='total_bill', hue='sex', data=tips, split=True)
plt.title('Violin Plot of Total Bill by Day and Sex')
plt.show()

# Pair plot
sns.pairplot(tips, hue='time', height=2.5)
plt.suptitle('Pair Plot of Tips Dataset', y=1.02)
plt.show()
"""
    
    st.code(code5, language='python')
    
    # Create sample dataset for seaborn examples
    np.random.seed(42)
    tips = pd.DataFrame({
        'total_bill': np.random.uniform(10, 50, 100),
        'tip': np.random.uniform(1, 10, 100),
        'sex': np.random.choice(['Male', 'Female'], 100),
        'smoker': np.random.choice(['Yes', 'No'], 100),
        'day': np.random.choice(['Sun', 'Sat', 'Fri', 'Thur'], 100),
        'time': np.random.choice(['Dinner', 'Lunch'], 100),
        'size': np.random.choice([1, 2, 3, 4, 5, 6], 100)
    })
    
    st.markdown("Tips Dataset (first 5 rows):")
    st.dataframe(tips.head())
    
    st.markdown("Scatter Plot Output:")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='total_bill', y='tip', hue='time', style='time', s=100, data=tips, ax=ax)
    ax.set_title('Scatter Plot of Tips vs Total Bill')
    st.pyplot(fig)
    
    st.markdown("Regression Plot Output:")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.regplot(x='total_bill', y='tip', data=tips, scatter_kws={'alpha':0.5}, ax=ax)
    ax.set_title('Regression Plot with Confidence Interval')
    st.pyplot(fig)
    
    st.markdown("Box Plot Output:")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(x='day', y='total_bill', hue='time', data=tips, ax=ax)
    ax.set_title('Box Plot of Total Bill by Day and Time')
    st.pyplot(fig)
    
    st.markdown("Violin Plot Output:")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.violinplot(x='day', y='total_bill', hue='sex', data=tips, split=True, ax=ax)
    ax.set_title('Violin Plot of Total Bill by Day and Sex')
    st.pyplot(fig)
    
    st.markdown("Pair Plot Output:")
    fig = sns.pairplot(tips, hue='time', height=2.5)
    fig.fig.suptitle('Pair Plot of Tips Dataset', y=1.02)
    st.pyplot(fig.fig)
    
    st.markdown("Try creating seaborn visualizations:")
    create_code_executor(code5)
    
    st.markdown("## Exercises: Data Visualization")
    
    st.markdown("""
    Let's practice creating some visualizations using the knowledge you've gained.
    """)
    
    # First exercise
    exercise1_solution = """import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
temperatures = [7, 9, 14, 18, 23, 27]

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(months, temperatures, color='orange')
plt.title('Average Monthly Temperatures')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()"""

    exercise1_passed = create_exercise(
        "Create a bar chart showing the average monthly temperatures for the first half of the year. Use the following data: Jan: 7°C, Feb: 9°C, Mar: 14°C, Apr: 18°C, May: 23°C, Jun: 27°C. Add appropriate labels and a title.",
        exercise1_solution
    )
    
    # Second exercise
    if exercise1_passed:
        exercise2_solution = """import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a DataFrame with random data
np.random.seed(42)
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Group1': np.random.randint(1, 10, 4),
    'Group2': np.random.randint(1, 10, 4)
}
df = pd.DataFrame(data)

# Create a grouped bar chart
width = 0.35
x = np.arange(len(df['Category']))

plt.figure(figsize=(10, 6))
plt.bar(x - width/2, df['Group1'], width, label='Group 1')
plt.bar(x + width/2, df['Group2'], width, label='Group 2')

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Grouped Bar Chart Comparison')
plt.xticks(x, df['Category'])
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()"""

        exercise2_passed = create_exercise(
            "Create a grouped bar chart comparing two groups across different categories. Generate random data for this exercise. Include a legend, appropriate labels, and a title.",
            exercise2_solution
        )
    else:
        exercise2_passed = False
    
    return exercise1_passed and exercise2_passed

# Render the lesson using the utility function
lesson_ui("Data Visualization", lesson_content)
