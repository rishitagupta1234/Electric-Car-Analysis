# 🔋 Electric Car Data Analysis and Dashboard

This project showcases an end-to-end data analysis and interactive dashboard built using real-world electric car data. The goal was to explore, clean, analyze, and visualize insights about electric vehicles using Python libraries and Tableau.

---

## 🚀 Tools & Technologies Used

- Python
  - NumPy
  - Pandas
- Excel (Raw and Cleaned Data)
- Tableau Public
- Streamlit
- Git & GitHub

---

## 📁 Folder Structure

electric-car-analysis/
│
├── car.xlsx                      # Raw electric car data
├── cleaned_data.xlsx             # Cleaned dataset (NaN handled)
├── ev data.xlsx                  # Filtered data (high cell count)
├── final ev data.xlsx            # Final file with normalized range
│
├── cleaned_data.py               # Numpy + Pandas cleaning and analysis
├── electric_dashboard.py         # Streamlit launcher for dashboard
├── README.md                     # Project explanation

**📌 Note:** All `.xlsx` files are included so you can directly run the project without downloading extra datasets.

## 📊 About the Dataset
The dataset contains specifications of various electric vehicles, including technical and performance details.  
It includes:
- Vehicle brand, model, and body type
- Battery capacity, number of cells, charging power
- Performance stats like range, acceleration, top speed, torque
- Dimensional details like height, length, and width

This dataset was used to analyze trends in electric vehicle technology and performance.

 ## ⚙️ How to Run the Project
``` bash
# Clone the repository
git clone https://github.com/rishitagupta1234/Electric-Car-Analysis.git
cd Electric-Car-Analysis

# Install dependencies
pip install pandas numpy streamlit openpyxl

# Run Python data cleaning script
python cleaned_data.py

# Launch Streamlit app
streamlit run electric_dashboard.py
```

## 🌟 Features

- Raw electric car dataset cleaning using Pandas & NumPy

- Missing value handling (mean for numeric, "Unknown" for categorical)

- Statistical analysis with NumPy (mean, median, std dev, normalization)

- Interactive dashboard using Tableau Public

- Streamlit app to embed Tableau dashboard

- Clean folder structure for easy navigation

## 🧠 Challenges Faced

- Handling missing values in multiple columns and deciding whether to fill or drop them.

- Understanding how to normalize numeric data using NumPy.

- Embedding the Tableau dashboard into a Streamlit app without connection issues.

- Cleaning column names and removing unnecessary columns from the raw dataset.

- Making the dashboard visually appealing and easy to understand.

## 📚 Lessons Learned

- How to clean and preprocess datasets using Pandas.

- How to perform statistical analysis and normalization using NumPy.

- How to create and publish interactive dashboards using Tableau Public.

- How to integrate Tableau dashboards inside a Streamlit web app.

- How to manage a project structure and upload it properly to GitHub.

## 👩‍💻 Author
**Rishita Gupta**  
B.Tech IT Student | Data Analyst & Web Developer | Tableau Enthusiast  
📧 Email: rishitagupta7942@gmail.com  
🔗 GitHub: [rishitagupta1234](https://github.com/rishitagupta1234)

