import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Function for generating static plots using Matplotlib/Seaborn
def static_visualization(df):
    print("Choose visualization type: ")
    print("1. Bar Plot")
    print("2. Histogram")
    print("3. Scatter Plot")
    print("4. Box Plot")
    
    choice = int(input("Enter choice number: "))
    
    if choice == 1:
        sns.barplot(x=df.columns[0], y=df.columns[2], data=df)
    elif choice == 2:
        df.hist()
    elif choice == 3:
        sns.scatterplot(x=df.columns[0], y=df.columns[1], data=df,marker='d',s=100)
    elif choice == 4:
        sns.boxplot(data=df)
    
    plt.show()

# Function for generating interactive plots using Plotly
def interactive_visualization(df):
    print("Choose visualization type: ")
    print("1. Interactive Bar Plot")
    print("2. Interactive Scatter Plot")
    
    choice = int(input("Enter choice number: "))
    
    if choice == 1:
        fig = px.bar(df, x=df.columns[0], y=df.columns[1], title='Interactive Bar Plot',hover_data=[df.columns[0],df.columns[1],df.columns[2]])
    elif choice == 2:
        fig = px.scatter(df, x=df.columns[0], y=df.columns[1], title='Interactive Scatter Plot')
    
    fig.show()

def main():
    file_path = input("Enter the path to your dataset: ")
    df = load_data(file_path)
    print(df)
    print("Choose the type of visualization: ")
    print("1. Static (Matplotlib/Seaborn)")
    print("2. Interactive (Plotly)")
    
    vis_type = int(input("Enter choice number: "))
    
    if vis_type == 1:
        static_visualization(df)
    elif vis_type == 2:
        interactive_visualization(df)

main()
