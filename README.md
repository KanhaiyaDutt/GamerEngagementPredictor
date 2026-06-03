# 🎮 Gamer Engagement Predictor

A Machine Learning project that predicts a player's engagement level (**Low, Medium, or High**) based on gameplay behavior, player progression, and activity patterns.

### 🚀 Live Demo

https://studentmarkspredictor-j7mnzmmjdpacf2bsgpo7ma.streamlit.app/

### 📂 GitHub Repository

https://github.com/KanhaiyaDutt/GamerEngagementPredictor

---

## 📌 Project Overview

Gaming companies often need to identify highly engaged players, moderate users, and players at risk of disengagement.

This project uses machine learning techniques to classify gamers into three engagement categories:

* 📉 Low Engagement
* ⚡ Medium Engagement
* 🔥 High Engagement

The model analyzes player behavior and gameplay statistics to make predictions that can be useful for:

* Player retention strategies
* Personalized recommendations
* Reward systems
* Marketing campaigns
* Community engagement analysis

---

## ✨ Key Features

* 🎯 Single Player Engagement Prediction
* 📂 Batch CSV Prediction
* 👀 CSV Data Preview Before Prediction
* 📊 Prediction Confidence Scores
* 📈 Engagement Distribution Summary
* ⬇ Download Predicted CSV Results
* 🤖 Automated Feature Selection with SelectKBest
* ⚡ Hyperparameter-Tuned Machine Learning Models

---

## 📊 Dataset Features

### Numerical Features

* Age
* PlayTimeHours
* InGamePurchases
* SessionsPerWeek
* AvgSessionDurationMinutes
* PlayerLevel
* AchievementsUnlocked

### Categorical Features

* Gender
* Location
* GameGenre
* GameDifficulty

### Target Variable

`EngagementLevel`

* Low → 0
* Medium → 1
* High → 2

---

## 🛠 Machine Learning Workflow

### 1. Data Preprocessing

The project uses a Scikit-Learn Pipeline for automated preprocessing.

#### Numerical Features

* StandardScaler
* MinMaxScaler

#### Categorical Features

* Missing value imputation using Most Frequent strategy
* One-Hot Encoding

---

### 2. Feature Engineering

A `ColumnTransformer` combines numerical and categorical preprocessing into a single pipeline.

---

### 3. Feature Selection

The model applies:

```python
SelectKBest(score_func=f_classif, k=7)
```

Only the top 7 most informative features are selected for training.

#### Selected Features

```text
num__InGamePurchases
num__SessionsPerWeek
num__AvgSessionDurationMinutes
num__PlayerLevel
num__AchievementsUnlocked
cat__GameGenre_Simulation
cat__GameDifficulty_Hard
```

---

### 4. Model Training

The project evaluates multiple algorithms:

#### Random Forest Classifier

Hyperparameters tuned:

* n_estimators
* max_depth
* max_features

#### XGBoost Classifier

Hyperparameters tuned:

* max_depth
* learning_rate
* n_estimators

---

### 5. Hyperparameter Tuning

Model optimization is performed using:

```python
RandomizedSearchCV
```

Configuration:

* 5-Fold Cross Validation
* 25 Random Search Iterations
* ROC-AUC OVR Scoring

---

## ⚙️ Final Pipeline

```text
Data
 ↓
Preprocessing
 ↓
Feature Selection (SelectKBest)
 ↓
Model Training
 ↓
Prediction
```

The entire pipeline is saved as:

```text
final_model.pkl
```

using Joblib serialization.

---

## 📈 Model Capabilities

The trained model can:

* Predict engagement level for individual players
* Estimate class probabilities and confidence scores
* Support single-player predictions through an interactive interface
* Perform batch predictions using CSV files
* Preview uploaded CSV data before prediction
* Generate engagement predictions for all records in the uploaded dataset
* Display prediction summaries and engagement distribution charts
* Export results as a downloadable CSV file with prediction columns added

### 📂 Batch CSV Prediction Workflow

1. Upload a CSV file containing player data.
2. Preview the uploaded dataset inside the application.
3. Validate required columns automatically.
4. Run predictions for all players in the dataset.
5. View engagement distribution and prediction summaries.
6. Download the generated CSV file containing:

   * Original player data
   * Predicted engagement level
   * Class probability scores (when available)
   * Prediction confidence values

This functionality allows the application to analyze large groups of players efficiently instead of predicting one player at a time.

---

## 📂 Project Structure

```text
GamerEngagementPredictor/
│
├── app.py
├── final_model.pkl
├── Gamer_behaviours_dataset.csv
├── requirements.txt
├── README.md
├── notebook.py
│
└── .streamlit/
    └── config.toml
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/KanhaiyaDutt/GamerEngagementPredictor.git
```

Move into the project folder:

```bash
cd GamerEngagementPredictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 🧰 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Joblib
* Streamlit

---

## 🎯 Future Improvements

* SHAP-based model explainability
* Advanced feature engineering
* Deep Learning approaches
* REST API deployment
* Real-time prediction services
* Model monitoring dashboard

---

## 👨‍💻 Author

**Kanhaiya Dutt**

If you found this project useful, consider giving the repository a ⭐.
