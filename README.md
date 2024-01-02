# **Project Title: Sentiment Analysis on Crypto News Headlines**

---

**Overview:**

This project focuses on sentiment analysis performed on a dataset containing cryptocurrency news headlines. It involves the implementation of various Natural Language Processing (NLP) techniques and machine learning models to analyze the sentiment associated with these headlines.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## **Step 1: Crypto News Headlines Scraping and Aggregation**

This Python script `webscrapper.py` facilitates the scraping of cryptocurrency news headlines from various online news websites such as CoinTelegraph and CoinDesk related to Bitcoin, Blockchain, Altcoins, Ethereum, and general cryptocurrency news. The extracted headlines are then aggregated into an Excel file `crypto_news_headlines.xlsx` for further analysis.

### **Code Overview:**

- `scrape_news_cointelegraph(url)`: Scrapes headlines from CoinTelegraph's Bitcoin and Blockchain sections.
- `scrape_news_blockchain_tech(url)`: Gathers news headlines from BlockchainTechnology-News for Altcoins and Ethereum.
- `scrape_news_coindesk(url)`: Fetches headlines from CoinDesk.

**Instructions:**
1. **Setup and Dependencies:**
    - Ensure you have Python installed along with required libraries (`requests`, `BeautifulSoup`, `pandas`, etc.).
    - The script assumes Python 3.x. If dependencies are not installed, run `pip install -r requirements.txt`.

2. **Running the Script:**
    - Execute the Python script in an environment with internet access.
    - The script collects headlines from specified URLs and combines them into an Excel file.

3. **Output:**
    - The output file `crypto_news_headlines.xlsx` contains the aggregated headlines in the specified file path.
    - If the file already exists, new headlines will be appended to the existing file.

---

## **Step 2: Crypto News Sentiment Analysis:**

- **Dataset:** The project uses a dataset named `crypto_news_headlines.csv`, which includes raw news headlines in the cryptocurrency domain.
  
- **Preprocessing:**
  - **Cleaning:** The headlines undergo various cleaning steps such as removing HTML tags, special characters, stop words, and normalization.
  - **Sentiment Analysis:** Sentiment analysis is conducted using TextBlob, assigning positive, negative, or neutral labels based on sentiment scores.
  
- **Modeling:**
  - **Random Forest:** Trains and evaluates a Random Forest classifier on the preprocessed headlines.
  - **CNN, LSTM, RNN, Word2Vec CNN:** Implements various neural network architectures (CNN, LSTM, RNN) and a Word2Vec-based CNN for sentiment analysis.
  
- **Visualization:**
  - Visualizes the distribution of cleaned headline lengths.
  - Plots sentiment distribution and sentiment score distributions.
  - Generates word clouds for positive, negative, and neutral sentiments.
  - Displays model accuracy and loss plots for each implemented model.
  - Compares model accuracies against a baseline Random Forest classifier.

### **Libraries Used:**

- `Pandas`, `Numpy`, `NLTK`, `Regex`, `BeautifulSoup`, `Seaborn`, `Matplotlib`, `TensorFlow`, `Keras`, `Gensim`, `TextBlob`, `Sklearn`

**Instructions:**
1. **Data Loading:** Place the `crypto_news_headlines.csv` dataset in the specified location.
2. **Dependencies:** Install the necessary Python libraries using `pip install -r requirements.txt`.
3. **Code Execution:** Execute the provided Python code cells in a Jupyter Notebook or Python environment.
4. **Results and Visualizations:** View generated visualizations to understand the sentiment analysis results.
5. **Model Evaluation:** Review the model accuracies and metrics obtained for different sentiment analysis models.

### **Additional Notes:**

- The code provides detailed comments to understand each step of the process.
- Adjust the file paths and dataset locations as per your system configuration.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
