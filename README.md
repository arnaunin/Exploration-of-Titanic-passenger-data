# Exploration of Titanic Passenger Data

This project is a **Streamlit** dashboard to explore the Titanic passenger dataset, using **Python** and various data analytics techniques. The dataset is downloaded from [Kaggle's Titanic competition](https://www.kaggle.com/c/titanic) and allows users to interactively explore and visualize the data, apply filters, and even make predictions about survival using an AI model.

## Features

- **Three Interactive Pages**:
  1. **Data Description**: Displays the raw Titanic passenger data, including basic descriptive statistics.
  2. **Data Analytics**: Allows users to explore the dataset through interactive visualizations like bar charts, scatter plots, pie charts, treemaps, and heatmaps. You can filter by passenger characteristics like age, class, gender, and more.
  3. **Artificial Intelligence**: Users can input passenger characteristics and get predictions on whether the passenger would survive, based on an AI model.

## Project Structure

The project is divided into three main parts:

1. **Data Description**: A simple overview of the Titanic dataset, with options to view the full data and get summary statistics.
2. **Data Analytics**: Interactive visualizations of the data where users can filter by different variables (e.g., passenger class, age, gender, etc.) and choose various chart types (e.g., bar, pie, scatter, treemap).
3. **Artificial Intelligence**: A model to predict whether a passenger would survive based on input features such as age, class, and fare.


## Cloud Storage of Data

To give the project a more **professional approach**, the Titanic dataset CSV file has been uploaded to **Amazon S3**. By hosting the data in the cloud, we ensure that the dataset is readily available, scalable, and accessible for use in the app without needing to store it locally.

Amazon S3 provides a reliable and secure way to store files, and in this project, we leverage it to host the Titanic dataset as a **publicly accessible CSV file**. This means that any user running the app can directly download and interact with the dataset in real time without manually handling the file.

The S3 file can be accessed via the following URL (used in the code for the dashboard):

- [Titanic Dataset on S3](https://conquerblocksbucket.s3.eu-north-1.amazonaws.com/train.csv) *This will automaticaly download the Titanic dataset CSV file*

By using this approach, the project demonstrates how real-world data pipelines might integrate cloud storage services such as **AWS S3** for ease of access, especially in large-scale or distributed systems.


## Installation and Execution

1. Clone this repository:
   ```
   https://github.com/arnaunin/Exploration-of-Titanic-passenger-data.git
   ```

2. Install the necessary dependencies:
   
    - **Python 3.7+**
    - **Streamlit**
    - **Pandas**
    - **Plotly**
    - **Scikit-learn**
  
    You can install the required libraries using the following commands:
  
    ```
    pip install streamlit
    ```
    ```
    pip install pandas
    ```
    ```
    pip install plotly
    ```
    ```
    pip install Scikit-learn
    ```

4. Navigate into the cloned repository
   ```
   cd path_to_repository/
   ```
   
5. Run the project:
   ```
   python streamlit_titanic.py
   ```
   or
   ```
   python3 streamlit_titanic.py
   ```

### Run the App
To run the Streamlit app, simply execute:

```
streamlit run app.py
```
This will open the application in your web browser.

## Dataset
The data used in this project is from the Kaggle Titanic dataset, which contains detailed information about passengers, such as:

- Passenger's class (1st, 2nd, 3rd)
- Name, Age, and Gender
- Number of siblings/spouses aboard
- Number of parents/children aboard
- Fare paid
- Port of embarkation (Southampton, Cherbourg, Queenstown)
- Whether the passenger survived

## AI Model
The AI model predicts whether a passenger would have survived or not based on various features. It uses a pre-trained machine learning model built using scikit-learn.

## How to Use
- Page 1: Data Description:
  View the complete Titanic dataset and its summary statistics.
- Page 2: Data Analytics:
  Filter the data by characteristics like gender, class, age, etc.
  Choose between various chart types: bar, scatter, pie, treemap, or heatmap.
- Page 3: Artificial Intelligence:
  Input details such as class, age, gender, and fare to predict whether a passenger would survive.
  
## Learnings
This project is a great way to get hands-on experience with:
- Data cleaning and preprocessing using Pandas.
- Interactive dashboard creation with Streamlit.
- Data visualization using Plotly.
- Machine learning model prediction with scikit-learn.
- It provides insights into both data analytics and the Titanic dataset, a popular dataset used in beginner-level data science projects.



## Contributing
Contributions are welcome! Please follow these steps:
1. **Fork the Repository**
2. **Create a Feature Branch (`git checkout -b feature-branch`)**
3. **Commit Your Changes (`git commit -m 'Add some feature'`)**
4. **Push to the Branch (`git push origin feature-branch`)**
5. **Open a Pull Request**
