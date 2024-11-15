import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the Data
file_path = 'sales_data.csv'

def load_data(file_path):
    """Load the sales data from a CSV file into a DataFrame."""
    df = pd.read_csv(file_path)
    return df

# 2. Data Preparation
def prepare_data(df):
    """Convert Date column to datetime and create a month column."""
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')  # Extract month{dt stands for date time (properties)}
    print(df)
    return df

# 3. Data Grouping
def group_data(df):
    """Group data to calculate total sales per product, monthly sales, and sales by category."""
    total_sales_per_product = df.groupby('Product')['Sales'].sum().reset_index()
    monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()
    total_sales_by_category = df.groupby('Category')['Sales'].sum().reset_index()
    print(total_sales_per_product)
    print(monthly_sales)
    print(total_sales_by_category)
    print()
    
    
    return total_sales_per_product, monthly_sales, total_sales_by_category

# 4. Create Visualizations
def create_visualizations(total_sales_per_product, monthly_sales, total_sales_by_category):
    """Create bar, line, and pie charts to visualize sales data."""
    
    # Bar Chart: Total Sales per Product
    plt.figure(figsize=(10, 6))
    plt.bar(total_sales_per_product['Product'], total_sales_per_product['Sales'], color='skyblue')
    plt.title('Total Sales per Product')
    plt.xlabel('Product')
    plt.ylabel('Sales Amount')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    print()
"""
    # Line Chart: Monthly Sales Trends
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_sales['Month'].astype(str), monthly_sales['Sales'], marker='o', color='orange')
    plt.title('Monthly Sales Trends')
    plt.xlabel('Month')
    plt.ylabel('Sales Amount')
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.show()

    # Pie Chart: Distribution of Sales by Product Category
    plt.figure(figsize=(10, 6))
    plt.pie(total_sales_by_category['Sales'], labels=total_sales_by_category['Category'], autopct='%1.1f%%', startangle=140)
    plt.title('Sales Distribution by Product Category')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.tight_layout()
    plt.show()
"""

# 5. Main Function
def main():
    # Load the dataset
    df = load_data(file_path)
    
    # Prepare the data
    df = prepare_data(df)
    
    # Group the data
    total_sales_per_product, monthly_sales, total_sales_by_category = group_data(df)
    
    # Create visualizations
    create_visualizations(total_sales_per_product, monthly_sales, total_sales_by_category)

if __name__ == '__main__':
    main()
