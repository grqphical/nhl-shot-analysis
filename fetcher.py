"""Used to fetch and combine all the goalie data from moneypuck between the 2008-2023 seasons"""

import requests
import pandas as pd
from io import StringIO

all_data = pd.DataFrame()

for season in range(2008, 2024, 1):
    url = f"https://moneypuck.com/moneypuck/playerData/seasonSummary/{season}/regular/goalies.csv"
    resp = requests.get(url)
    if resp.status_code == 200:
        data = StringIO(resp.text)
        df = pd.read_csv(data)
        all_data = pd.concat([all_data, df])

    combined_df = pd.concat([all_data], ignore_index=True)
    combined_df.to_csv("data/goalies_2008-2023.csv", index=False)
