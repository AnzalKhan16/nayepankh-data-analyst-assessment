import pandas as pd
import numpy as np
from datetime import datetime

def generate_mock_data(filename='data/nayepankh_data_12_months.csv'):
    np.random.seed(42)
    months = pd.date_range(end=datetime.today(), periods=12, freq='ME').strftime('%Y-%m').tolist()
    
    data = {
        'Month': months,
        'Instagram_Followers': np.cumsum(np.random.randint(100, 500, size=12)) + 10000,
        'Instagram_Engagement_Rate': np.random.uniform(2.5, 6.0, size=12).round(2),
        'Instagram_Posts': np.random.randint(10, 30, size=12),
        'LinkedIn_Followers': np.cumsum(np.random.randint(50, 200, size=12)) + 5000,
        'LinkedIn_Engagement_Rate': np.random.uniform(1.5, 4.0, size=12).round(2),
        'LinkedIn_Posts': np.random.randint(5, 15, size=12),
        'YouTube_Subscribers': np.cumsum(np.random.randint(20, 100, size=12)) + 2000,
        'YouTube_Views': np.random.randint(1000, 15000, size=12),
        'YouTube_Videos': np.random.randint(1, 5, size=12),
        'Facebook_Followers': np.cumsum(np.random.randint(30, 100, size=12)) + 8000,
        'Facebook_Engagement_Rate': np.random.uniform(1.0, 3.0, size=12).round(2),
        'X_Followers': np.cumsum(np.random.randint(10, 50, size=12)) + 3000,
        'X_Engagement_Rate': np.random.uniform(0.5, 2.5, size=12).round(2),
        'Website_Traffic_Page_Views': np.random.randint(5000, 25000, size=12),
        'Website_Bounce_Rate': np.random.uniform(40, 65, size=12).round(2),
        'Unique_Donors': np.random.randint(50, 300, size=12),
    }
    
    df = pd.DataFrame(data)
    
    # Introduce some realistic correlations
    # Example: A viral month with high YouTube views -> more traffic -> more donors
    viral_month_idx = 7 
    df.loc[viral_month_idx, 'YouTube_Views'] = 55000
    df.loc[viral_month_idx, 'Website_Traffic_Page_Views'] = 80000
    df.loc[viral_month_idx, 'Unique_Donors'] = 850
    df.loc[viral_month_idx, 'Instagram_Engagement_Rate'] = 8.5
    
    # Calculate donations based on donors (average donation between 500 and 2000 INR)
    df['Total_Donations_INR'] = df['Unique_Donors'] * np.random.uniform(500, 2000, size=12).round(2)
    
    import os
    os.makedirs('data', exist_ok=True)
    df.to_csv(filename, index=False)
    print(f"Mock data generated successfully and saved to {filename}")
    return df

if __name__ == "__main__":
    generate_mock_data()
