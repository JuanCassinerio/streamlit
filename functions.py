
import requests
import pandas as pd
import yfinance as yf

def dolar(start_date_date, end_date):
    url = "https://api.argentinadatos.com/v1/cotizaciones/dolares"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    data = requests.get(url, headers=headers, verify=False).json()
    data = pd.DataFrame.from_dict(data)
    data['precio'] = (data['compra'] + data['venta']) / 2
    data = data[['fecha', 'precio', 'casa']]
    casa_values = data['casa'].unique()  # Get unique casa values
    for casa in casa_values:
        data[f'{casa}'] = data[data['casa'] == casa]['precio']
    data.drop(['casa', 'precio', 'solidario'], axis=1, inplace=True)

    def fill_missing_by_fecha(df):
        return pd.concat([df[['fecha']], df.groupby('fecha').transform(lambda x: x.fillna(method='ffill'))], axis=1)

    data1 = fill_missing_by_fecha(data.copy())  # Avoid modifying original data
    data1.sort_index(ascending=False, inplace=True)  # Sort DataFrame by index in descending order
    data1.drop_duplicates(subset='fecha', keep='first',
                          inplace=True)  # Keep the first occurrence of each unique 'fecha'
    data1.sort_index(ascending=True, inplace=True)  # Sort DataFrame by index in ascending order again

    url = "https://dolarapi.com/v1/dolares"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    data = requests.get(url, headers=headers, verify=False).json()
    data = pd.DataFrame.from_dict(data)
    data['precio'] = (data['compra'] + data['venta']) / 2
    data = data[['fechaActualizacion', 'precio', 'casa']]
    casa_values = data['casa'].unique()  # Get unique casa values
    for casa in casa_values:
        data[f'{casa}'] = data[data['casa'] == casa]['precio']
    data.drop(['casa', 'precio'], axis=1, inplace=True)

    def fill_missing_by_fecha(df):
        return pd.concat([df[['fechaActualizacion']],
                          df.groupby('fechaActualizacion').transform(lambda x: x.fillna(method='ffill'))], axis=1)

    data2 = fill_missing_by_fecha(data.copy())  # Avoid modifying original data
    data2.sort_index(ascending=False, inplace=True)  # Sort DataFrame by index in descending order
    data2.drop_duplicates(subset='fechaActualizacion', keep='first',
                          inplace=True)  # Keep the first occurrence of each unique 'fecha'
    data2.sort_index(ascending=True, inplace=True)  # Sort DataFrame by index in ascending order again
    data2['fechaActualizacion'] = pd.to_datetime(data['fechaActualizacion'])  # Convert to datetime if not already
    data2['fechaActualizacion'] -= pd.Timedelta(hours=1)
    data2 = data2.rename(columns={'fechaActualizacion': 'fecha'})
    data2['fecha'] = pd.to_datetime(data2['fecha']).dt.strftime('%Y-%m-%d')

    data = pd.concat([data1, data2], ignore_index=True)
    data['fecha'] = pd.to_datetime(data['fecha'])

    filtered_df = data[data['fecha'].dt.date >= start_date_date]
    filtered_df = filtered_df[filtered_df['fecha'].dt.date <= end_date]
    return filtered_df

def price(ticker,start_date,end_date):

    '''


    -Downloads at ET time zone
    -HISTORIC STOCKS PRICES (DIVIDEND ACCOUNTED)(adj close)
    '''


    # start_date=date.today() - pd.DateOffset(years=6), end_date=date.today()
    price = yf.download(ticker, start=start_date, end=end_date, auto_adjust=False)
    price.columns = price.columns.droplevel(1)  # Drop the first level (Ticker)
    price =price.rename_axis(None, axis=1)['Adj Close']
    price = pd.DataFrame(price)
    price = price.sort_values(by='Date', ascending=False)
    price['Date'] = price.index
    #price['ticker'] = ticker
    price['Adj Close']=round(price['Adj Close'],2)
    price = price.reset_index(drop=True)
    return price