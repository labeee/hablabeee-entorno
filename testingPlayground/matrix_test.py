import pandas as pd
from glob import glob

ex = {
  "originAddresses": [ "Greenwich, Greater London, UK", "13 Great Carleton Square, Edinburgh, City of Edinburgh EH16 4, UK" ],
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
  }, {
    "elements": [ {
      "status": "OK",
      "duration": {
        "value": 96000,
        "text": "1 day 3 hours"
      },
      "distance": {
        "value": 2566737,
        "text": "1595 mi"
      }
    }, {
      "status": "OK",
      "duration": {
        "value": 69698,
        "text": "19 hours 22 mins"
      },
      "distance": {
        "value": 1942009,
        "text": "1207 mi"
      }
    } ]
  } ]
}

df_unfiltered = pd.DataFrame(ex)
df_unfiltered.to_csv(r'testingPlayground/example_raw_matrix.csv', sep=';')

rows = ex.get('rows')
count = 0
for each in rows:
    count += 1
    df_filtered = pd.DataFrame(each)
    df_filtered.to_csv(f'testingPlayground/example_semiraw_matrix_{count}.csv', sep=';')
