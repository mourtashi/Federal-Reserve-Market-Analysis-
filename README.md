# Federal-Reserve-Market-Analysis-
Overview:

This tool uses the FRED API to fetch data of a specified series (like 'UNRATE' for Unemployment Rate), calculates the moving average, and then performs several types of plots including a time series plot, a scatter plot with a trendline, and exports the data to an Excel file. It also calculates the percentage change in data over a year.

How it works:

The program contains several functions each handling a different aspect of the analysis:

1.	get_fred_data(series_id): Fetches data for the specified series ID from the FRED API. It converts the 'date' column to a datetime type, and the 'value' column to a numeric type. It also calculates the percentage change from the previous year for each data point.
2.	calculate_moving_average(df, window): Calculates the moving average of the 'value' column over the specified window of time.
3.	plot_time_series(df, series_id): Plots the original data and its moving average over time.
4.	plot_year_over_year(df, series_id): Plots the year-over-year percentage change in a bar graph.
5.	plot_scatter_with_trendline(df, series_id, x_col, y_col): Plots a scatter plot of the specified x and y columns, along with a trendline showing the moving average.
6.	export_to_excel(df, series_id): Exports the DataFrame to an Excel file.

The main part of the program fetches the data for a specified series ID, calculates its moving average, plots its time series, exports the data to an Excel file, and then plots a scatter plot with a trendline.

Libraries Used:

Requests, Pandas, Matplotlib, Seaborn, 

Usage:

1.	Replace the API_KEY with your FRED API key.
2.	Replace the series_id with the FRED series ID you are interested in.
3.	Run the script. It fetches the data, calculates the moving average, and presents various plots (these plots will be displayed on an interactive environment such as Jupyter Notebook).
4.	An Excel file is created in the working directory, named as {series_id}_data.xlsx.

This tool serves as an interface to fetch and analyze economic data from FRED. Economists, data scientists, researchers, and students could use it to get insights into various economic parameters.

