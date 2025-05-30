
#  Agentic Insights Challenge 

A lightweight data dashboard built with **Streamlit** to simulate and present core metrics for the Agentic Platform. This assignment aims to showcase key growth, engagement, and performance indicators to impress a data-driven investor.

![Agentic Dashboard Screenshot](https://github.com/viveknair6915/Agentic-Insights-Challenge/raw/main/Screenshots/Screenshot%20(6).png)
![Agentic Dashboard Screenshot](https://github.com/viveknair6915/Agentic-Insights-Challenge/raw/main/Screenshots/Screenshot%20(7).png)


##  Objective

> Imagine we’re pitching our Agentic Platform to an investor who loves data.  
> We showcase 3 key metrics proving our product is gaining traction.


##  Key Metrics Tracked

<details>
<summary><strong>1. Daily Active Users (DAUs)</strong></summary>

Measures how many unique users engage with the platform each day.  
Higher DAUs indicate strong user retention and product interest.
</details>

<details>
<summary><strong>2. Average Session Duration</strong></summary>

Shows how much time users spend in each session (in minutes).  
Longer durations suggest deeper engagement and satisfaction.
</details>

<details>
<summary><strong>3. Conversion Rate (%)</strong></summary>

The percentage of users completing a desired action (e.g., signing up, purchasing, etc.).  
Reflects how effectively engagement translates into value.
</details>

---

## Insights Derived from the Dashboard

1. **User Growth:** DAUs have grown steadily, indicating strong platform adoption.
2. **Engagement:** Session duration trends show users are spending more time in-app.
3. **Conversion Efficiency:** Increasing conversion rates reflect successful optimization and onboarding.

---

##  How to Set Up and Run the Dashboard

<details>
<summary><strong>Step-by-step setup</strong></summary>

###  Prerequisites

- Python 3.7 or higher
- Internet connection (to install dependencies)

###  1. Clone or download the repo

```bash
mkdir agentic-insights-challenge
cd agentic-insights-challenge
````

Create the following files inside:

* `dashboard.py`
* `requirements.txt`
* `README.md`

###  2. Create a virtual environment

**Windows:**

```bash
py -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

###  3. Install required libraries

```bash
pip install -r requirements.txt
```

###  4. Run the dashboard

```bash
streamlit run dashboard.py
```

Open the URL shown in your terminal (usually [http://localhost:8501](http://localhost:8501)).

</details>

##  Project File Structure

```
agentic-insights-challenge/
├── dashboard.py        
├── requirements.txt     
└── README.md           
```

## Author Notes

* Fake data is generated dynamically for demo purposes.
* You may extend this to include real-time integrations, database support, or UI customizations using Streamlit components.
* This project demonstrates skill in **dashboarding, communication, and structured insight design**.
