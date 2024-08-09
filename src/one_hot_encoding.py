import pandas as pd

def convert_to_one_hot(data: pd.DataFrame) -> pd.DataFrame:
    unique_values = data['whoAmI'].unique()
    one_hot_df = pd.concat(
        [data['whoAmI'].apply(lambda x: 1 if x == val else 0) for val in unique_values], 
        axis=1
    )
    one_hot_df.columns = unique_values
    return one_hot_df

if __name__ == "__main__":
    import os
    from data.generate_data import generate_sample_data

    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)

    # Generate and save the sample data
    df = generate_sample_data()
    df.to_csv('data/sample_data.csv', index=False)

    # Perform one-hot encoding
    one_hot_encoded_df = convert_to_one_hot(df)
    print(one_hot_encoded_df.head())
