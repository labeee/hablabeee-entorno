import pandas as pd
from glob import glob

ex = {
  "originAddresses": [ "Greenwich, Greater London, UK"],
  "destinationAddresses": [ "Stockholm County, Sweden", "Dlouhá 609/2, 110 00 Praha-Staré Město, Česká republika" ],
  "rows": [ {
    "elements": [ {
      "status": "OK",
      "duration": {
        "value": 70778,
        "text": "19 hours 40 mins"
      },
      "distance": {
        "value": 1887508,
        "text": "1173 mi"
      }
    }, {
      "status": "OK",
      "duration": {
        "value": 44476,
        "text": "12 hours 21 mins"
      },
      "distance": {
        "value": 1262780,
        "text": "785 mi"
      }
    } ]
  } ]
}

# df_unfiltered = pd.DataFrame(ex)
# df_unfiltered.to_csv(r'testingPlayground/example_raw_matrix.csv', sep=';')

rows = ex.get('rows')[0].get('elements')
df_filtered = pd.DataFrame(rows)
df_filtered.drop(columns=['status'], axis=1, inplace=True)
df_filtered.to_csv(f'testingPlayground/example_semiraw_matrix.csv', sep=';')
