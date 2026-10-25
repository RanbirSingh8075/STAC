"""
STAC WARS - PS 2: SOLAR RADIATION ANALYSIS AND PREDICTION
Author: Alliance Data Analysis Team
Target Dataset: Voyage-123 Solar Observation Data (NASA Solar Radiation Dataset)
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Set overall plot styling
sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 10, 'figure.autolayout': True})

def load_and_preprocess(data_path="SolarPrediction.csv"):
    """Loads raw Voyage-123 observation logs and parses datetime features."""
    df = pd.read_csv(data_path)
    
    # Clean column names
    df.columns = df.columns.str.strip()
    
    # Task C Requirement: Convert Data and Time columns into a proper datetime column
    # Expected standard columns: UNIXTime, Data, Time, Radiation, Temperature, Pressure, Humidity, WindDirection(Degrees), Speed, TimeSunRise, TimeSunSet
    if 'UNIXTime' in df.columns:
        df['Datetime'] = pd.to_datetime(df['UNIXTime'], unit='s')
    else:
        df['Datetime'] = pd.to_datetime(df['Data'] + ' ' + df['Time'])
        
    df['Date'] = df['Datetime'].dt.date
    df['Hour'] = df['Datetime'].dt.hour
    df['Time_Only'] = df['Datetime'].dt.time
    
    return df


def generate_visualizations(df, output_dir="plots"):
    """Generates all Part A visualization plots."""
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Solar Radiation Variation with Time (Hourly diurnal pattern)
    plt.figure(figsize=(10, 5))
    df.groupby('Hour')['Radiation'].mean().plot(kind='line', marker='o', color='#e67e22', linewidth=2.5)
    plt.title('Average Solar Radiation Variation by Hour of Day')
    plt.xlabel('Hour of Day (24-hr)')
    plt.ylabel('Mean Radiation (W/m²)')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig(f"{output_dir}/1_radiation_vs_time.png", dpi=300)
    plt.close()

    # 2. Relationships: Radiation vs Temperature & Humidity
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    sns.scatterplot(data=df, x='Temperature', y='Radiation', alpha=0.3, color='#e74c3c', ax=axes[0])
    axes[0].set_title('Solar Radiation vs Temperature')
    axes[0].set_xlabel('Temperature (°F)')
    axes[0].set_ylabel('Radiation (W/m²)')

    sns.scatterplot(data=df, x='Humidity', y='Radiation', alpha=0.3, color='#3498db', ax=axes[1])
    axes[1].set_title('Solar Radiation vs Humidity')
    axes[1].set_xlabel('Humidity (%)')
    axes[1].set_ylabel('Radiation (W/m²)')

    plt.tight_layout()
    plt.savefig(f"{output_dir}/2_radiation_env_relationships.png", dpi=300)
    plt.close()

    # 3. Outlier and Distribution Boxplot
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='Radiation', data=df, color='#9b59b6')
    plt.title('Solar Radiation Outlier and Distribution Identification')
    plt.xlabel('Radiation (W/m²)')
    plt.savefig(f"{output_dir}/3_outliers_boxplot.png", dpi=300)
    plt.close()

    # 4. Bonus Visualisation: Hourly Heatmap across Temperature and Humidity
    plt.figure(figsize=(10, 6))
    correlation_matrix = df[['Radiation', 'Temperature', 'Pressure', 'Humidity', 'Speed']].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='YlOrRd', fmt=".2f")
    plt.title('Bonus: Feature Correlation Heatmap')
    plt.savefig(f"{output_dir}/4_bonus_correlation_heatmap.png", dpi=300)
    plt.close()


def Perform_solar_day_analysis(df):
    """Executes Part C daily activity transformation and reporting."""
    # Group observations by date
    daily_stats = df.groupby('Date').agg(
        max_radiation=('Radiation', 'max'),
        avg_radiation=('Radiation', 'mean')
    ).reset_index()

    # Determine date with highest recorded solar radiation
    max_day_row = daily_stats.loc[daily_stats['max_radiation'].idxmax()]
    peak_date = max_day_row['Date']
    
    # Filter for peak radiation instance on that date
    peak_day_df = df[df['Date'] == peak_date]
    peak_record = peak_day_df.loc[peak_day_df['Radiation'].idxmax()]
    
    # Sunrise & Sunset time calculations
    sunrise_time = pd.to_datetime(peak_record['TimeSunRise']).time() if 'TimeSunRise' in df.columns else None
    sunset_time = pd.to_datetime(peak_record['TimeSunSet']).time() if 'TimeSunSet' in df.columns else None
    
    peak_datetime = peak_record['Datetime']
    if 'TimeSunRise' in df.columns:
        sunrise_datetime = pd.to_datetime(f"{peak_date} {peak_record['TimeSunRise']}")
        time_diff_hrs = (peak_datetime - sunrise_datetime).total_seconds() / 3600.0
    else:
        time_diff_hrs = None

    # Top 5 days with highest average radiation
    top5_avg_days = daily_stats.sort_values(by='avg_radiation', ascending=False).head(5)

    return {
        "daily_stats": daily_stats,
        "peak_date": peak_date,
        "peak_record": peak_record,
        "time_diff_hrs": time_diff_hrs,
        "top5_avg_days": top5_avg_days
    }


def train_prediction_model(df):
    """Executes Bonus Machine Learning Solar Radiation Prediction model."""
    # Feature Engineering
    features = ['Temperature', 'Pressure', 'Humidity', 'Speed', 'Hour']
    target = 'Radiation'
    
    X = df[features]
    y = df[target]

    # Split train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model Training
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluation
    predictions = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    # Feature Importance
    importances = pd.Series(model.feature_importances_, index=features).sort_values(ascending=False)

    return model, rmse, r2, importances


if __name__ == "__main__":
    print("Executing Voyage-123 Solar Observation Analysis Pipeline...")
    
    # Load dataset
    df = load_and_preprocess("SolarPrediction.csv")
    
    # Part A Visualizations
    generate_visualizations(df)
    print("[SUCCESS] Part A: Visualizations generated in /plots directory.")

    # Part C Solar Day Analysis
    results = Perform_solar_day_analysis(df)
    print("\n--- Part C: Solar Day Analysis Report ---")
    print(f"Date with Highest Max Radiation: {results['peak_date']}")
    print(f"Peak Radiation: {results['peak_record']['Radiation']} W/m²")
    print(f"Time of Peak: {results['peak_record']['Time_Only']}")
    print(f"Temperature at Peak: {results['peak_record']['Temperature']} °F")
    print(f"Humidity at Peak: {results['peak_record']['Humidity']}%")
    print(f"Wind Speed at Peak: {results['peak_record']['Speed']} mph")
    if results['time_diff_hrs'] is not None:
        print(f"Hours After Sunrise Peak Occurred: {results['time_diff_hrs']:.2f} hours")
    print("\nTop 5 Days by Average Radiation:")
    print(results['top5_avg_days'].to_string(index=False))

    # Bonus Model Training
    model, rmse, r2, importances = train_prediction_model(df)
    print("\n--- Bonus: Machine Learning Model Evaluation ---")
    print(f"Model: Random Forest Regressor")
    print(f"RMSE: {rmse:.4f}")
    print(f"R² Score: {r2:.4f}")
    print("Feature Importances:")
    print(importances.to_string())