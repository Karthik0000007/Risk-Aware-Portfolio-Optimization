# 💹 Risk-Aware Portfolio Optimization using Deep Reinforcement Learning and Explainable AI

This repository is the foundation of a multi-phase AI-driven finance project that aims to build an **intelligent portfolio management system** using modern machine learning, reinforcement learning, and explainability tools.

---

## 🧠 Project Goal

Design and develop a portfolio optimization system that:

- Learns optimal trading and allocation strategies using **Deep Reinforcement Learning**
- Understands market **regimes and volatility**
- Is powered by **interpretable machine learning**
- Handles real-world **multi-asset financial data**

---

## ✅ Phase 1 Completed: Supervised Learning Module

We’ve successfully built and trained a powerful **XGBoost-based signal classifier** using:

- 📊 **Multi-ETF feature dataset**: QQQ, SPY, GLD, TLT, XLF, XLE, IWM
- 🧠 **Technical indicators**: MACD, RSI, Bollinger Band Width, Sharpe Ratio
- ⚠️ **Regime classification** using a Hidden Markov Model (HMM)
- 🎯 **Target**: Predict direction of QQQ returns (up/down)

### 💥 Model Accuracy: `98%`  
The model is saved for deployment or use in downstream reinforcement learning environments.

---

## Project Structure

```
Risk-Aware-Portfolio-Optimization/
│
├── .gitignore
├── README.md
├── requirements.txt
│
├── data/                     # Processed datasets (CSV files)
│   ├── gdp_growth.csv
│   ├── cpi.csv
│   ├── fed_funds_rate.csv
│   ├── unemployment_rate.csv
│   └── qqq_supervised.csv
│
├── models/                   # Saved models and scalers
│   ├── day7_xgb_multi_etf_classifier.json
│   └── day7_xgb_scaler.pkl
│
├── notebooks/                # Jupyter notebooks for analysis and modeling
│   ├── macro_data.ipynb
│   ├── regime_classification_hmm.ipynb
│   └── return_prediction_xgboost_classifier.ipynb
│
├── utils/                    # Utility scripts and helper functions
│
└── Risk_Aware_venv/          # Python virtual environment (do not edit)
```

---

## 📈 Next Steps (Planned)

- 🔍 Add **SHAP-based explainability** to uncover model insights
- 🧠 Build and train **Reinforcement Learning agents** for dynamic portfolio management
- 📊 Integrate real-time **Streamlit dashboard** for live tracking

---

## ⚙️ Tech Stack

- Python, Pandas, NumPy
- XGBoost, scikit-learn
- ta-lib (Technical Analysis)
- Hidden Markov Models (hmmlearn)
- Matplotlib / SHAP for interpretability

---

## 👨‍💻 Author

**Karthik** — Engineering student at SRM University-AP, building real-world AI projects for quantitative finance and smart investing.

---

