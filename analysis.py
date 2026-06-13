import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set visual style
sns.set_theme(style="whitegrid")
# Custom palette inspired by non-profit themes (soft greens, deep blues, warm tones)
custom_palette = ["#2E8B57", "#4682B4", "#DAA520", "#D2691E", "#556B2F"]

def perform_eda_and_visualizations(data_path='data/nayepankh_data_12_months.csv', output_dir='output_plots'):
    os.makedirs(output_dir, exist_ok=True)
    df = pd.read_csv(data_path)
    
    # 1. Exploratory Data Analysis & Correlation
    print("--- Exploratory Data Analysis ---")
    print(df.describe())
    
    # Select columns for correlation matrix
    cols_of_interest = ['Website_Traffic_Page_Views', 'Unique_Donors', 'Total_Donations_INR', 
                        'YouTube_Views', 'Instagram_Engagement_Rate']
    corr_matrix = df[cols_of_interest].corr()
    
    print("\n--- Correlation Matrix ---")
    print(corr_matrix)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="YlGnBu", vmin=-1, vmax=1)
    plt.title("Correlation Matrix: Traffic, Engagement, and Donations")
    plt.tight_layout()
    plt.savefig(f'{output_dir}/correlation_heatmap.png')
    plt.close()
    
    # 2. Line Chart: Monthly Donation Trends vs Website Traffic
    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Total Donations (INR)', color=custom_palette[0])
    ax1.plot(df['Month'], df['Total_Donations_INR'], marker='o', color=custom_palette[0], label='Donations (INR)', linewidth=2)
    ax1.tick_params(axis='y', labelcolor=custom_palette[0])
    plt.xticks(rotation=45)
    
    ax2 = ax1.twinx()
    ax2.set_ylabel('Website Traffic (Page Views)', color=custom_palette[1])
    ax2.plot(df['Month'], df['Website_Traffic_Page_Views'], marker='s', color=custom_palette[1], linestyle='--', label='Website Traffic', linewidth=2)
    ax2.tick_params(axis='y', labelcolor=custom_palette[1])
    
    fig.suptitle('Monthly Donation Trends Alongside Website Traffic', fontsize=16)
    fig.tight_layout()
    plt.savefig(f'{output_dir}/donations_vs_traffic.png')
    plt.close()
    
    # 3. Grouped Bar Chart: Engagement Rates Across Platforms
    plt.figure(figsize=(12, 6))
    eng_cols = ['Month', 'Instagram_Engagement_Rate', 'LinkedIn_Engagement_Rate', 'Facebook_Engagement_Rate', 'X_Engagement_Rate']
    df_eng = df[eng_cols].melt(id_vars='Month', var_name='Platform', value_name='Engagement Rate (%)')
    df_eng['Platform'] = df_eng['Platform'].str.replace('_Engagement_Rate', '')
    
    sns.barplot(x='Month', y='Engagement Rate (%)', hue='Platform', data=df_eng, palette=custom_palette[:4])
    plt.title('Monthly Engagement Rates Across Social Media Platforms', fontsize=16)
    plt.xticks(rotation=45)
    plt.legend(title='Platform', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/engagement_rates.png')
    plt.close()
    
    # 4. Donut Chart: Donor Acquisition Channels (Mock Data)
    # We will generate static mock percentages to represent channels
    channels = ['Instagram', 'LinkedIn', 'Direct Website', 'WhatsApp', 'YouTube']
    donors = [35, 15, 30, 10, 10]
    
    plt.figure(figsize=(8, 8))
    plt.pie(donors, labels=channels, autopct='%1.1f%%', startangle=140, colors=custom_palette)
    # Draw circle to make it a donut chart
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    
    plt.title('Distribution of Donor Acquisition Channels', fontsize=16)
    plt.tight_layout()
    plt.savefig(f'{output_dir}/acquisition_channels.png')
    plt.close()

    print(f"\nVisualizations successfully generated and saved in the '{output_dir}/' directory.")

if __name__ == "__main__":
    perform_eda_and_visualizations()
