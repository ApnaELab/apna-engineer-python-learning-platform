import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import lesson_ui, create_code_executor, create_exercise

def lesson_content():
    st.markdown("# Data Visualization in Python")
    
    st.markdown("""
    Data visualization is the graphical representation of data to help understand patterns, trends, and relationships. 
    Python offers several powerful libraries for creating visualizations.
    
    In this lesson, we'll explore:
    
    1. **Matplotlib**: The foundation of visualization in Python
    2. **Seaborn**: Statistical plotting based on Matplotlib
    3. **Pandas Plotting**: Direct visualization from pandas DataFrames
    """)
    
    st.markdown("## Introduction to Matplotlib")
    
    st.markdown("""
    Matplotlib is the most widely used Python library for creating static, animated, and interactive visualizations. 
    It provides a MATLAB-like interface and works well with NumPy arrays.
    
    Let's start with basic plots:
    """)
    
    code1 = """import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure and axis
plt.figure(figsize=(10, 6))

# Plot data
plt.plot(x, y1, label='Sine', color='blue', linewidth=2)
plt.plot(x, y2, label='Cosine', color='red', linewidth=2, linestyle='--')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine and Cosine Functions')

# Add grid and legend
plt.grid(True, alpha=0.3)
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()
"""
    
    st.code(code1, language='python')
    
    # Create the matplotlib example plot
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y1, label='Sine', color='blue', linewidth=2)
    ax.plot(x, y2, label='Cosine', color='red', linewidth=2, linestyle='--')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Sine and Cosine Functions')
    ax.grid(True, alpha=0.3)
    ax.legend()
    st.pyplot(fig)
    
    st.markdown("Try creating your own plot:")
    create_code_executor(code1)
    
    st.markdown("## Common Plot Types with Matplotlib")
    
    st.markdown("""
    Matplotlib supports many types of plots. Let's explore some common ones:
    """)
    
    st.markdown("### Scatter Plot")
    code2 = """import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(42)
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.7, cmap='viridis')

plt.colorbar(label='Color Value')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Size and Color Variation')
plt.grid(True, alpha=0.3)
plt.show()
"""
    
    st.code(code2, language='python')
    
    # Create scatter plot example
    np.random.seed(42)
    x = np.random.rand(50)
    y = np.random.rand(50)
    colors = np.random.rand(50)
    sizes = 1000 * np.random.rand(50)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    scatter = ax.scatter(x, y, c=colors, s=sizes, alpha=0.7, cmap='viridis')
    plt.colorbar(scatter, ax=ax, label='Color Value')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Scatter Plot with Size and Color Variation')
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    
    st.markdown("### Bar Plot")
    code3 = """import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
categories = ['A', 'B', 'C', 'D', 'E']
values = [25, 40, 30, 55, 15]

# Create bar plot
plt.figure(figsize=(10, 6))
plt.bar(categories, values, color='skyblue', edgecolor='navy')

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot Example')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
"""
    
    st.code(code3, language='python')
    
    # Create bar plot example
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [25, 40, 30, 55, 15]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(categories, values, color='skyblue', edgecolor='navy')
    ax.set_xlabel('Categories')
    ax.set_ylabel('Values')
    ax.set_title('Bar Plot Example')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig)
    
    st.markdown("### Histogram")
    code4 = """import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(42)
data = np.random.normal(0, 1, 1000)  # 1000 points from a normal distribution

# Create histogram
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, color='green', alpha=0.7, edgecolor='black')

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Normal Distribution')
plt.grid(axis='y', alpha=0.3)
plt.show()
"""
    
    st.code(code4, language='python')
    
    # Create histogram example
    np.random.seed(42)
    data = np.random.normal(0, 1, 1000)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(data, bins=30, color='green', alpha=0.7, edgecolor='black')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Normal Distribution')
    ax.grid(axis='y', alpha=0.3)
    st.pyplot(fig)
    
    st.markdown("### Pie Chart")
    code5 = """import matplotlib.pyplot as plt

# Data for pie chart
labels = ['A', 'B', 'C', 'D', 'E']
sizes = [15, 30, 25, 10, 20]
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'lightpink']
explode = (0.1, 0, 0, 0, 0)  # explode the 1st slice (i.e. 'A')

# Create pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')
plt.title('Pie Chart Example')
plt.show()
"""
    
    st.code(code5, language='python')
    
    # Create pie chart example
    labels = ['A', 'B', 'C', 'D', 'E']
    sizes = [15, 30, 25, 10, 20]
    colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'lightpink']
    explode = (0.1, 0, 0, 0, 0)
    
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(sizes, explode=explode, labels=labels, colors=colors,
           autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')
    ax.set_title('Pie Chart Example')
    st.pyplot(fig)
    
    st.markdown("Try creating these different types of plots:")
    create_code_executor(code3)  # Using the bar plot example as default
    
    st.markdown("## Subplots and Multiple Figures")
    
    st.markdown("""
    Matplotlib allows you to create multiple plots in a single figure using subplots:
    """)
    
    code6 = """import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.linspace(0, 5, 100)
y1 = np.sin(x)
y2 = np.exp(-x)
y3 = x**2
y4 = np.log(x + 1)

# Create a figure with 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot on each subplot
axes[0, 0].plot(x, y1, 'b-')
axes[0, 0].set_title('Sine Function')
axes[0, 0].set_xlabel('x')
axes[0, 0].set_ylabel('sin(x)')
axes[0, 0].grid(True)

axes[0, 1].plot(x, y2, 'r-')
axes[0, 1].set_title('Exponential Decay')
axes[0, 1].set_xlabel('x')
axes[0, 1].set_ylabel('exp(-x)')
axes[0, 1].grid(True)

axes[1, 0].plot(x, y3, 'g-')
axes[1, 0].set_title('Quadratic Function')
axes[1, 0].set_xlabel('x')
axes[1, 0].set_ylabel('x²')
axes[1, 0].grid(True)

axes[1, 1].plot(x, y4, 'y-')
axes[1, 1].set_title('Logarithmic Function')
axes[1, 1].set_xlabel('x')
axes[1, 1].set_ylabel('log(x+1)')
axes[1, 1].grid(True)

plt.tight_layout()
plt.show()
"""
    
    st.code(code6, language='python')
    
    # Create subplots example
    x = np.linspace(0, 5, 100)
    y1 = np.sin(x)
    y2 = np.exp(-x)
    y3 = x**2
    y4 = np.log(x + 1)
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    axes[0, 0].plot(x, y1, 'b-')
    axes[0, 0].set_title('Sine Function')
    axes[0, 0].set_xlabel('x')
    axes[0, 0].set_ylabel('sin(x)')
    axes[0, 0].grid(True)
    
    axes[0, 1].plot(x, y2, 'r-')
    axes[0, 1].set_title('Exponential Decay')
    axes[0, 1].set_xlabel('x')
    axes[0, 1].set_ylabel('exp(-x)')
    axes[0, 1].grid(True)
    
    axes[1, 0].plot(x, y3, 'g-')
    axes[1, 0].set_title('Quadratic Function')
    axes[1, 0].set_xlabel('x')
    axes[1, 0].set_ylabel('x²')
    axes[1, 0].grid(True)
    
    axes[1, 1].plot(x, y4, 'y-')
    axes[1, 1].set_title('Logarithmic Function')
    axes[1, 1].set_xlabel('x')
    axes[1, 1].set_ylabel('log(x+1)')
    axes[1, 1].grid(True)
    
    plt.tight_layout()
    st.pyplot(fig)
    
    st.markdown("Try creating subplots:")
    create_code_executor(code6)
    
    st.markdown("## Introduction to Seaborn")
    
    st.markdown("""
    Seaborn is a statistical data visualization library based on Matplotlib. It provides a high-level interface for drawing attractive statistical graphics.
    
    Key features of Seaborn:
    - Built-in themes for styling Matplotlib graphics
    - Functions for visualizing univariate and bivariate distributions
    - Tools for choosing color palettes
    - Functions for plotting statistical time series data
    """)
    
    code7 = """import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Set the theme
sns.set_theme(style="whitegrid")

# Create a dataset
np.random.seed(42)
tips = pd.DataFrame({
    'total_bill': np.random.uniform(10, 50, 200),
    'tip': np.random.uniform(1, 10, 200),
    'sex': np.random.choice(['Male', 'Female'], 200),
    'smoker': np.random.choice(['Yes', 'No'], 200),
    'day': np.random.choice(['Sun', 'Sat', 'Fri', 'Thur'], 200),
    'time': np.random.choice(['Dinner', 'Lunch'], 200),
    'size': np.random.choice([1, 2, 3, 4, 5, 6], 200)
})

# Create a simple scatterplot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='time', style='time', s=100)

plt.title('Relationship between Total Bill and Tip')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.show()
"""
    
    st.code(code7, language='python')
    
    # Create seaborn example
    sns.set_theme(style="whitegrid")
    
    # Create a dataset
    np.random.seed(42)
    tips = pd.DataFrame({
        'total_bill': np.random.uniform(10, 50, 200),
        'tip': np.random.uniform(1, 10, 200),
        'sex': np.random.choice(['Male', 'Female'], 200),
        'smoker': np.random.choice(['Yes', 'No'], 200),
        'day': np.random.choice(['Sun', 'Sat', 'Fri', 'Thur'], 200),
        'time': np.random.choice(['Dinner', 'Lunch'], 200),
        'size': np.random.choice([1, 2, 3, 4, 5, 6], 200)
    })
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='total_bill', y='tip', data=tips, hue='time', style='time', s=100, ax=ax)
    ax.set_title('Relationship between Total Bill and Tip')
    ax.set_xlabel('Total Bill ($)')
    ax.set_ylabel('Tip ($)')
    st.pyplot(fig)
    
    st.markdown("## Common Seaborn Plots")
    
    st.markdown("### Categorical Plots")
    
    code8 = """import seaborn as sns
import matplotlib.pyplot as plt

# Bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='day', y='total_bill', data=tips)
plt.title('Average Total Bill by Day')
plt.xlabel('Day')
plt.ylabel('Average Total Bill ($)')
plt.show()

# Box plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='day', y='total_bill', data=tips)
plt.title('Distribution of Total Bill by Day')
plt.xlabel('Day')
plt.ylabel('Total Bill ($)')
plt.show()

# Violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x='day', y='total_bill', data=tips, hue='time', split=True)
plt.title('Distribution of Total Bill by Day and Time')
plt.xlabel('Day')
plt.ylabel('Total Bill ($)')
plt.show()
"""
    
    st.code(code8, language='python')
    
    # Seaborn categorical plots examples
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='day', y='total_bill', data=tips, ax=ax)
    ax.set_title('Average Total Bill by Day')
    ax.set_xlabel('Day')
    ax.set_ylabel('Average Total Bill ($)')
    st.pyplot(fig)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='day', y='total_bill', data=tips, ax=ax)
    ax.set_title('Distribution of Total Bill by Day')
    ax.set_xlabel('Day')
    ax.set_ylabel('Total Bill ($)')
    st.pyplot(fig)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.violinplot(x='day', y='total_bill', data=tips, hue='time', split=True, ax=ax)
    ax.set_title('Distribution of Total Bill by Day and Time')
    ax.set_xlabel('Day')
    ax.set_ylabel('Total Bill ($)')
    st.pyplot(fig)
    
    st.markdown("### Distribution Plots")
    
    code9 = """import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Histogram with KDE
plt.figure(figsize=(10, 6))
sns.histplot(tips['total_bill'], kde=True, bins=20)
plt.title('Distribution of Total Bill')
plt.xlabel('Total Bill ($)')
plt.ylabel('Count')
plt.show()

# KDE plot
plt.figure(figsize=(10, 6))
sns.kdeplot(data=tips, x='total_bill', hue='time', fill=True, common_norm=False, palette="crest", alpha=.5)
plt.title('KDE of Total Bill by Time')
plt.xlabel('Total Bill ($)')
plt.ylabel('Density')
plt.show()

# Pair plot
plt.figure(figsize=(12, 10))
sns.pairplot(tips, hue='time', height=2.5)
plt.suptitle('Pair Plot of Tips Dataset', y=1.02)
plt.show()
"""
    
    st.code(code9, language='python')
    
    # Seaborn distribution plots examples
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(tips['total_bill'], kde=True, bins=20, ax=ax)
    ax.set_title('Distribution of Total Bill')
    ax.set_xlabel('Total Bill ($)')
    ax.set_ylabel('Count')
    st.pyplot(fig)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.kdeplot(data=tips, x='total_bill', hue='time', fill=True, common_norm=False, palette="crest", alpha=.5, ax=ax)
    ax.set_title('KDE of Total Bill by Time')
    ax.set_xlabel('Total Bill ($)')
    ax.set_ylabel('Density')
    st.pyplot(fig)
    
    # Pair plot (this will be larger)
    pairgrid = sns.pairplot(tips[['total_bill', 'tip', 'size']], hue='size', height=2.5)
    pairgrid.fig.suptitle('Pair Plot of Tips Dataset (Subset)', y=1.02)
    st.pyplot(pairgrid.fig)
    
    st.markdown("Try creating seaborn plots:")
    create_code_executor(code8)
    
    st.markdown("## Plotting with Pandas")
    
    st.markdown("""
    Pandas has built-in plotting functionality based on Matplotlib. This provides a convenient way to visualize data directly from DataFrames:
    """)
    
    code10 = """import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a time series dataset
dates = pd.date_range('20230101', periods=100)
df = pd.DataFrame({
    'A': np.random.randn(100).cumsum(),
    'B': np.random.randn(100).cumsum(),
    'C': np.random.randn(100).cumsum(),
    'D': np.random.randn(100).cumsum()
}, index=dates)

# Line plot
df.plot(figsize=(10, 6), title='Line Plot with Pandas')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()

# Bar plot
df.iloc[0:10].plot.bar(figsize=(10, 6), title='Bar Plot with Pandas')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()

# Histogram
df.plot.hist(bins=20, alpha=0.7, figsize=(10, 6), title='Histogram with Pandas')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Scatter plot
df.plot.scatter(x='A', y='B', figsize=(10, 6), title='Scatter Plot with Pandas', 
                c='C', cmap='viridis', s=df['D'].abs() * 100)
plt.xlabel('A')
plt.ylabel('B')
plt.grid(True)
plt.show()
"""
    
    st.code(code10, language='python')
    
    # Pandas plotting examples
    dates = pd.date_range('20230101', periods=100)
    df = pd.DataFrame({
        'A': np.random.randn(100).cumsum(),
        'B': np.random.randn(100).cumsum(),
        'C': np.random.randn(100).cumsum(),
        'D': np.random.randn(100).cumsum()
    }, index=dates)
    
    st.markdown("Line Plot Output:")
    fig, ax = plt.subplots(figsize=(10, 6))
    df.plot(ax=ax, title='Line Plot with Pandas')
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.grid(True)
    st.pyplot(fig)
    
    st.markdown("Bar Plot Output:")
    fig, ax = plt.subplots(figsize=(10, 6))
    df.iloc[0:10].plot.bar(ax=ax, title='Bar Plot with Pandas')
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.grid(True)
    st.pyplot(fig)
    
    st.markdown("Line Plot Output (safer than area plot):")
    fig, ax = plt.subplots(figsize=(10, 6))
    df.plot(ax=ax, alpha=0.7, title='Line Plot with Pandas')
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.grid(True)
    st.pyplot(fig)
    
    st.markdown("Scatter Plot Output:")
    fig, ax = plt.subplots(figsize=(10, 6))
    df.plot.scatter(x='A', y='B', ax=ax, title='Scatter Plot with Pandas', 
                    c='C', cmap='viridis', s=df['D'].abs() * 100)
    ax.set_xlabel('A')
    ax.set_ylabel('B')
    ax.grid(True)
    st.pyplot(fig)
    
    st.markdown("Try pandas plotting:")
    create_code_executor(code10)
    
    st.markdown("## Exercise: Data Visualization")
    
    # Exercise for data visualization
    exercise_solution = """import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create the dataset
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [23, 48, 17, 35, 29]
}
df = pd.DataFrame(data)

# Create the horizontal bar chart
plt.figure(figsize=(10, 6))
plt.barh(df['Category'], df['Values'], color='skyblue')
plt.xlabel('Values')
plt.ylabel('Category')
plt.title('Horizontal Bar Chart')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()
"""
    
    exercise_passed = create_exercise(
        """Create a horizontal bar chart using matplotlib with the following requirements:
        
        1. Create a DataFrame with two columns: 'Category' (letters A through E) and 'Values' (random numbers between 10 and 50)
        2. Plot a horizontal bar chart (hint: use plt.barh)
        3. Set appropriate labels for the x-axis, y-axis, and title
        4. Add a grid only for the x-axis
        5. Use 'skyblue' for the bar color
        """,
        exercise_solution
    )
    
    return exercise_passed

# Render the lesson using the utility function
lesson_ui("Data Visualization", lesson_content)
