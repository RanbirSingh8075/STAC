# 🌌 STAC WARS: Master Technical Submission & Solution Repository
> **Space Technology & Astronomy Club (STAC) Hackathon — IIT Mandi**  
> *Complete Multi-Disciplinary Submission Covering PS1 (Rocketry), PS2 (Data Analytics & Prediction), PS3 (Exoplanet Astronomy), and Bonus Project Pitch.*

---

## 📜 Table of Contents
1. [Executive Summary](#-executive-summary)
2. [PS 1: Mission Mustafar — High-Altitude Rocket Simulation](#-ps-1-mission-mustafar--high-altitude-rocket-simulation)
3. [PS 2: Voyage-123 — Solar Radiation Analysis & Prediction](#-ps-2-voyage-123--solar-radiation-analysis--prediction)
4. [PS 3: Operation Dim Star — Exoplanet Detection & Habitability](#-ps-3-operation-dim-star--exoplanet-detection--habitability)
5. [Bonus Pitch: Project OrbitWatch / Open-SAT](#-bonus-pitch-project-orbitwatch--open-sat)
6. [Repository Structure & Execution Guide](#-repository-structure--execution-guide)

---

## 📑 Executive Summary

This repository contains the complete analytical solutions, code pipelines, and engineering design files for the **STAC WARS Hackathon**:

| Task | Domain | Target Objective | Key Result / Metric | Status |
| :--- | :--- | :--- | :--- | :--- |
| **PS 1** | Rocketry Engineering | Design a cardboard rocket for planet Mustafar ($700\text{ K}$, $75\text{ kPa}$) | **$4042.9\text{ m}$ Apogee** (Window: $3900\text{--}4100\text{ m}$) | **COMPLETED** |
| **PS 2** | Data Science & ML | Analyze Voyage-123 solar logs & build predictive regression model | **$R^2 = 0.932$, $RMSE = 92.42\text{ W/m}^2$** (Random Forest) | **COMPLETED** |
| **PS 3** | Exoplanet Astronomy | Analyze stellar light curves (STAC 1–3) & locate habitable world | **Selected STAC-3b** ($R_p = 1.64 R_\oplus, a = 0.1817\text{ AU}$) | **COMPLETED** |
| **Bonus** | Space Software Pitch | Propose a feasible, high-impact software/hardware club project | **Project OrbitWatch** (3D Satellite Tracker + SDR Station) | **COMPLETED** |

---

## 🚀 PS 1: Mission Mustafar — High-Altitude Rocket Simulation

### 1. Problem Context & Environmental Physics
The mission requires engineering a 2-stage sounding rocket to launch on planet Mustafar under extreme ambient parameters:
* **Atmospheric Temperature:** $700\text{ K}$
* **Surface Pressure:** $75\text{ kPa}$
* **Surface Gravity:** $6.5\text{ m/s}^2$
* **Wind Profile:** $10\text{ m/s}$ at $270^\circ$ (Turbulence: $0$)
* **Airframe Materials:** Pure Cardboard (strictly zero mass overrides)
* **Payload Mass:** $1.000\text{ kg}$
* **Airframe Geometry:** Length $2050\text{ mm}$ (below $2200\text{ mm}$ limit)

### 2. Motor Selection & Delay Optimization
* **Booster Stage:** Cesaroni J540R ($54\text{ mm}$ bore, $1.5\text{ mm}$ wall thickness). Ejects at burnout.
* **Sustainer Stage:** Cesaroni **CTI 128G185-12A** ($38\text{ mm}$ bore, $127\text{ mm}$ length).
* **Ejection Delay Optimization:**
  * Burnout occurs at $t = 2.99\text{ s}$; Apogee occurs at $t = 28.25\text{ s}$.
  * Corrected Ejection Delay: $28.25\text{ s} - 2.99\text{ s} = \mathbf{25.3\text{ s}}$.
  * *Impact:* Eliminates premature payload separation ($6.7\text{ s}$ before apogee) and prevents atmospheric tumbling.

### 3. OpenRocket Simulation Flight Performance
* **Peak Apogee:** **$4042.9\text{ m}$** *(Fits inside the required $3900\text{ m}$ to $4100\text{ m}$ window)*
* **Max Velocity:** $368.9\text{ m/s}$ ($\text{Mach } 0.647$)
* **Launch Rod Exit Velocity:** $39.8\text{ m/s}$ off a $4\text{ m}$ rod (Ensures flight stability)
* **Deployment Velocity:** $1.99\text{ m/s}$ (Low mechanical deployment shock)
* **Total Flight Time:** $661\text{ s}$ ($\approx 11\text{ min}$ dual-parachute descent)

---

## ☀️ PS 2: Voyage-123 — Solar Radiation Analysis & Prediction

### 1. Data Visualizations & Inferences (Parts A & B)
* **Diurnal Pattern:** Solar radiation follows a parabolic curve, peaking between 11:00 AM and 1:00 PM local solar noon.
* **Temperature Correlation:** Strong positive linear correlation ($r \approx 0.73$). Solar flux directly drives surface ambient heating.
* **Humidity Attenuation:** Inverse relationship; high atmospheric moisture/cloud cover reduces net solar irradiance.
* **Solar Flare Outliers:** Extreme spikes above $1200\text{ W/m}^2$ (up to $1601.26\text{ W/m}^2$) represent transient solar flare events logged by Voyage-123.

### 2. Solar Day Analysis Report (Part C)
* **Date with Maximum Radiation:** `2016-11-30`
* **Peak Radiation Recorded:** $1601.26\text{ W/m}^2$
* **Peak Timestamp:** `12:10:00 PM`
* **Conditions at Peak:** Temp: $64^\circ\text{F}$ | Humidity: $32\%$ | Wind: $9.0\text{ mph}$
* **Time Elapsed After Sunrise:** $5\text{ Hours } 28\text{ Minutes}$

### 3. Machine Learning Prediction Model (Bonus)
* **Model Architecture:** `RandomForestRegressor(n_estimators=100, random_state=42)`
* **Coefficient of Determination ($R^2$):** **$0.932$** (High predictive accuracy)
* **Root Mean Squared Error (RMSE):** **$92.42\text{ W/m}^2$**
* **Feature Importances:** Temperature ($48\%$), Hour of Day ($32\%$), Humidity ($12\%$), Wind Speed ($8\%$).

---

## 🪐 PS 3: Operation Dim Star — Exoplanet Detection & Habitability

### 1. Formulations & Physics
* **Transit Depth ($\delta$):** $\delta = \frac{F_{\text{normal}} - F_{\text{transit}}}{F_{\text{normal}}} \approx \left(\frac{R_p}{R_s}\right)^2$
* **Kepler's Third Law:** $P^2 = \frac{a^3}{M} \implies a = \sqrt[3]{P^2 \cdot M}$ *(with $P$ in years, $M$ in $M_\odot$, $a$ in AU)*
* **Habitable Zone Boundary:** $d_{\text{HZ}} \approx \sqrt{L / L_\odot}\text{ AU}$

### 2. Master Parameter Matrix

| Parameter | STAC-1b | STAC-2b | STAC-3b (SELECTED CANDIDATE) |
| :--- | :--- | :--- | :--- |
| **Orbital Period ($P$)** | $4.0\text{ days}$ ($0.0110\text{ yr}$) | $80.0\text{ days}$ ($0.2190\text{ yr}$) | **$40.0\text{ days}$ ($0.1095\text{ yr}$)** |
| **Transit Depth ($\delta$)** | $0.0030\ (0.30\%)$ | $0.0010\ (0.10\%)$ | **$0.0009\ (0.09\%)$** |
| **Radius ($R_p$ in km)** | $38,121.5\text{ km}$ | $17,607.7\text{ km}$ | **$10,440.0\text{ km}$** |
| **Radius ($R_p$ in $R_\oplus$)** | $5.98\ R_\oplus$ | $2.76\ R_\oplus$ | **$1.64\ R_\oplus$** |
| **Classification** | Neptune-sized Gas Planet | Large Super-Earth | **Terrestrial Super-Earth** |
| **Orbital Distance ($a$)** | $0.0493\text{ AU}$ | $0.3373\text{ AU}$ | **$0.1817\text{ AU}$** |
| **Habitable Zone ($d_{\text{HZ}}$)**| $1.000\text{ AU}$ (Scorched) | $0.632\text{ AU}$ (Interior edge) | **$0.283\text{ AU}$ (Closest boundary)** |

### 3. Selection Rationale for STAC-3b
1. **Solid Terrestrial Surface ($1.64\ R_\oplus$):** Sits below the $1.8\text{--}2.0\ R_\oplus$ threshold, guaranteeing a solid rocky surface rather than a gas envelope.
2. **Thermal Equilibrium:** Orbits a cool M-dwarf star ($3800\text{ K}$, $0.08\ L_\odot$). Its $0.1817\text{ AU}$ orbit sits closest to the star's habitable zone ($0.283\text{ AU}$).
3. **Follow-up Protocol:** Perform **Transmission Spectroscopy** during upcoming transits to evaluate $H_2O$, $CO_2$, and $O_3$ atmospheric signatures.

---

## 🛰️ Bonus Pitch: Project OrbitWatch / Open-SAT

### 1. Executive Summary
**OrbitWatch** is a campus-hosted, open-source software and hardware initiative designed to bridge **orbital mechanics, radio astronomy, and web development**. It tracks LEO satellites in 3D and automatically decodes live weather satellite imagery (NOAA / METEOR-M) via a campus Software Defined Radio (SDR) station.

### 2. System Architecture
[ CelesTrak TLE Data ] ──▶ [ Python Skyfield Engine ] ──▶ [ 3D CesiumJS Dashboard ]
│
▼
[ Campus Antenna / RTL-SDR ] ──▶ [ Automated Audio Decoder ] ──▶ [ Live Weather Images ]
### 3. Value Proposition for STAC
* **Low Hardware Cost:** Uses standard RTL-SDR USB dongles ($<\$30$) and DIY dipole antennas.
* **High Feasibility:** Achievable within a single academic semester.
* **Campus Outreach:** Provides STAC with a flagship, live web portal on a college subdomain.

---

## 🛠️ Repository Structure & Execution Guide
├── PS1_Rocketry/
│   └── 1792897427853_Mustafar.ork          # OpenRocket simulation design file
├── PS2_SolarAnalytics/
│   ├── SolarPrediction.csv                 # Voyage-123 solar dataset
│   ├── solar_analysis.py                   # Python analysis & ML pipeline
│   ├── generate_report.py                  # ReportLab PDF report generator
│   └── Solar_Radiation_Analysis_Report.pdf # Final PDF report
├── PS3_Astronomy/
│   ├── operation_dim_star_ieee.tex         # IEEE LaTeX source code
│   └── operation_dim_star_ieee_report.html # IEEE publication PDF layout
├── Master_Presentation/
│   └── STAC_Wars_Master_Presentation.pptx  # Unified PPTX presentation deck
└── README.md                               # Master documentation file


### Quick Execution Commands:
```bash
# 1. Install dependencies
python -m pip install pandas numpy matplotlib seaborn scikit-learn reportlab

# 2. Run PS2 Data Pipeline & ML Training
python PS2_SolarAnalytics/solar_analysis.py

# 3. Generate PS2 PDF Report
python PS2_SolarAnalytics/generate_report.py
