import pandas as pd
from datetime import datetime
import os

def generate_monthly_report(data_path='data/nayepankh_data_12_months.csv', month=None):
    if not os.path.exists(data_path):
        print("Dataset not found. Please run `generate_data.py` first.")
        return
        
    df = pd.read_csv(data_path)
    
    if month is None:
        month = df['Month'].iloc[-1] # Default to the latest month
        
    try:
        month_data = df[df['Month'] == month].iloc[0]
    except IndexError:
        print(f"Data for month '{month}' not found.")
        return
    
    report_md = f"""# NayePankh Foundation - Monthly Performance Report
**Month:** {month}
**Generated On:** {datetime.today().strftime('%Y-%m-%d')}

## 🌟 Executive Summary
In the month of {month}, NayePankh Foundation successfully raised **₹{month_data['Total_Donations_INR']:,.2f}** from **{month_data['Unique_Donors']}** unique donors. Our website traffic reached **{month_data['Website_Traffic_Page_Views']:,}** page views.

## 📱 Social Media Highlights
- **Instagram:** Reached {month_data['Instagram_Followers']} followers with an engagement rate of {month_data['Instagram_Engagement_Rate']}%.
- **LinkedIn:** Grew to {month_data['LinkedIn_Followers']} followers ({month_data['LinkedIn_Engagement_Rate']}% engagement).
- **YouTube:** Achieved {month_data['YouTube_Views']} views across {month_data['YouTube_Videos']} new videos.
- **Facebook & X:** Maintained steady growth with {month_data['Facebook_Engagement_Rate']}% and {month_data['X_Engagement_Rate']}% engagement respectively.

## 💡 Key Insights & Recommendations
1. **Donation Correlation:** Based on our EDA, there is a strong positive correlation between YouTube viral content, increased website traffic, and the number of unique donors. 
2. **Platform Focus:** Instagram continues to drive the highest engagement out of all social channels. We recommend doubling down on Instagram Reels, Stories, and interactive content.
3. **Action Item:** Consider launching a targeted LinkedIn outreach campaign next month, as professional networks often yield higher average individual donation amounts.

*This report was automatically generated via the Data Analytics Pipeline for the internship project.*
"""
    
    os.makedirs('reports', exist_ok=True)
    report_filename = f"reports/Performance_Report_{month}.md"
    
    with open(report_filename, 'w', encoding='utf-8') as f:
        f.write(report_md)
        
    print(f"Automated Report generated successfully: {report_filename}")
    return report_md

if __name__ == "__main__":
    generate_monthly_report()
