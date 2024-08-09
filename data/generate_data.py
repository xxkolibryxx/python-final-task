import pandas as pd
import random

def generate_sample_data() -> pd.DataFrame:
    lst = ['robot'] * 10
    lst += ['human'] * 10
    random.shuffle(lst)
    data = pd.DataFrame({'whoAmI': lst})
    return data

if __name__ == "__main__":
    df = generate_sample_data()
    print(df.head())