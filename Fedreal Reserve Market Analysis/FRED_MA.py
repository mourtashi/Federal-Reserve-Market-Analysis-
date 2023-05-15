import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

API_KEY = '1d1b5095885cc6d63187b786116e2d9b'  # Replace this with your FRED API key

def get_fred_data(series_id):
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={API_KEY}&file_type=json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()['observations']
        df = pd.DataFrame(data)
        df['date'] = pd.to_datetime(df['date'])
        df['value'] = pd.to_numeric(df['value'], errors='coerce')
        df['pct_change'] = df['value'].pct_change(periods=12) * 100
        df['pct_change'] = (df['value'] - df['value'].shift(12)) / df['value'].shift(12) * 100
        

        return df
    else:
        print(f"Error {response.status_code}: Failed to fetch data")
        return None

    

def calculate_moving_average(df, window):
    df['moving_average'] = df['value'].rolling(window=window).mean()
    return df

def plot_scatter_with_trendline(df, series_id, x_col='date', y_col='value'):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.regplot(x=x_col, y=y_col, data=df, ax=ax, order=2)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"{series_id} Scatter Plot with Trendline")
    plt.show()


def plot_time_series(df, series_id):
    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df['value'], label='Original Data')
    plt.plot(df['date'], df['moving_average'], label='Moving Average', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel(series_id)
    plt.title(f"{series_id} Time Series")
    plt.legend()
    plt.show()

def plot_year_over_year(df, series_id):
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.bar(df['date'], df['pct_change'], label='Year-over-Year % Change')
    
    ax.set_xlabel('Date')
    ax.set_ylabel('Year-over-Year % Change')
    plt.title(f"{series_id} Year-over-Year % Change")
    
    fig.legend()
    plt.show()



def plot_scatter_with_trendline(df, series_id, x_col, y_col):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df[x_col], df[y_col])
    ax.plot(df[x_col], df[y_col].rolling(window=12).mean(), label='Moving Average', linestyle='--')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"{series_id} Scatter Plot with Trendline")
    plt.legend()
    plt.show()


def export_to_excel(df, series_id):
    file_name = f"{series_id}_data.xlsx"
    df.to_excel(file_name, index=False)
    print(f"Data exported to {file_name}")


series_id = 'UNRATE'  # Replace this with the FRED series ID you are interested in
df = get_fred_data(series_id)

if df is not None:
    df = calculate_moving_average(df, window=12)
    plot_time_series(df, series_id)
    export_to_excel(df, series_id)
    plot_scatter_with_trendline(df, series_id, x_col='date', y_col='value')
