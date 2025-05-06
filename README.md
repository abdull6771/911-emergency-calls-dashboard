Here's a polished and structured `README.md` version of your project description:

---

# 📊 911 Emergency Calls Dashboard

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Flask](https://img.shields.io/badge/Flask-2.3.2-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Tailwind CSS](https://img.shields.io/badge/TailwindCSS-3.x-blueviolet.svg)](https://tailwindcss.com/)
[![Plotly](https://img.shields.io/badge/Plotly-5.15.0-orange.svg)](https://plotly.com/python/)
[![Kaggle Dataset](https://img.shields.io/badge/Dataset-Kaggle-blue)](https://www.kaggle.com/)

An interactive, web-based dashboard built using **Flask**, **Tailwind CSS**, and **Plotly** to visualize and analyze 911 emergency calls in **Montgomery County, PA**. The dashboard uncovers critical insights into emergency call types (EMS, Fire, Traffic), temporal trends, geographic patterns, and high-volume areas—empowering public safety efforts with actionable data.

---

## 🚀 Features

* **Interactive Visualizations** powered by Plotly:

  * 📊 Bar chart for call reasons (EMS, Fire, Traffic)
  * 📈 Line chart for monthly call volume
  * 🌡️ Heatmap for call frequency by day and hour
  * 🗺️ Scatter map for call locations (latitude/longitude)
  * 🏙️ Bar chart for top 10 townships by call volume

* **Dynamic Filters**: Filter charts by call reason (All, EMS, Fire, Traffic)

* **Geographic Insights**: Interactive map using Plotly’s Mapbox

* **📄 Downloadable PDF Reports**: Summarized charts, insights, and recommendations

* **💡 Responsive Design**: Tailwind CSS for mobile-friendly UI

* **🌙 Light/Dark Mode**: Toggle theme for better accessibility

* **🔗 Shareable Insights**: Share via Twitter/X or Web Share API

* **📚 Data Storytelling**: Narrative-driven layout for guided exploration

---

## 📂 Dataset

The dashboard uses the **911 Calls dataset** with key fields:

* `lat`, `lng`, `desc`, `zip`, `title`, `timeStamp`, `twp`, `addr`, `e`

Data preprocessing includes:

* Handling missing values
* Parsing timestamps
* Extracting call reasons

---

## ⚙️ Installation

### Prerequisites

* Python 3.8+
* Git
* Web browser (Chrome, Firefox, etc.)

### Setup Steps

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/911-emergency-calls-dashboard.git
cd 911-emergency-calls-dashboard
```

2. **Set Up a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Download the Dataset**

* Download `911.csv` from [Kaggle](https://www.kaggle.com/)
* Place it in the project root directory

5. **Run the Application**

```bash
python app.py
```

6. **View in Browser**

Open [http://localhost:5000](http://localhost:5000)

---

## 🧭 Usage

### Explore the Dashboard

* Use the dropdown to filter by call reason
* Hover, zoom, and download Plotly charts
* Toggle light/dark mode from the navbar
* Share insights using the social buttons
* Navigate with the sidebar or “Back to Top” button

### Generate PDF Report

Click **“Generate PDF Report”** in the conclusion section to download a summary with charts and recommendations.

---

## 📁 Project Structure

```
911-emergency-calls-dashboard/
├── static/
│   └── js/
│       └── dashboard.js       # JS for interactivity (filters, theme, sharing)
├── templates/
│   └── index.html             # Main template with Tailwind CSS
├── app.py                     # Flask backend for data & PDF logic
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── 911.csv                    # Dataset (not included; download from Kaggle)
```

---

## 📦 Dependencies

Listed in `requirements.txt`:

* `flask==2.3.2`
* `pandas==2.0.3`
* `plotly==5.15.0`
* `reportlab==4.0.4`
* `kaleido==0.2.1`

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m "Add your feature"`
4. Push to your branch: `git push origin feature/your-feature`
5. Open a pull request

> Please follow **PEP 8** and include tests where appropriate.

---

## 📜 License

This project is licensed under the **MIT License**. See `LICENSE` for details.

---

## 🙏 Acknowledgments

* **Dataset**: [Kaggle Montcoalert](https://www.kaggle.com/)
* **Frameworks**: Flask, Tailwind CSS, Plotly
* **Inspiration**: Data storytelling & modern dashboard design

---

## 📬 Contact

For questions or feedback, open an issue or contact: `your-email@example.com`

---

Would you like a badge set (e.g., Python version, license, stars) added at the top too?
