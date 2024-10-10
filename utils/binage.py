import pandas as pd
import json

def bin_age(age_col):
    """
    
    * Joubert2020 modalities : Infant (20); Child (690); Young (1591); Early career (3 633); Late career (2 283); Unknown (473)

    * Sun2015 modalities : 15–19; 20–24; 25–29; 30–34; 35–39; 40–44; 45–49; 50–54; 55–59; 60–64; 65–69; 70/ +
    * Fournier2021 modalitites : 0-9 10-14 15-19 20-24 (25-44?) 45-54 55-64 >65
    * Ma2018 : <30 years old, 30-40, 40-50, 50-60, >60
    * Hor2020 : <15    15-29    30-44    45-59    60-74    75+
    * Yameogo2021 : 0-2; 3-5; 6-10; 11-14; 15-17; 18-24; 25-29; 30-39; 40-54; 55-64; 65-79; 80/+
    
    """

    with open('config.json', 'r') as config_path:
        config = json.load(config_path)
        
    age_thresholds = config['age_bins']
    age_labels = list(range(len(age_thresholds)-1))
    return pd.cut(age_col, bins=age_thresholds, labels=age_labels)