import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(page_title="Agentic Insights", layout="wide")

# Title
st.title("Agentic Platform — Key Metrics Dashboard")

# Generate fake time-series data for the last 14 days
dates = [datetime.today() - timedelta(days=i) for i in range(13, -1, -1)]

data = pd.DataFrame({
    "date": dates,
    "Daily Active Users": np.random.randint(800, 1200, size=14),
    "Avg. Session Duration (min)": np.round(np.random.uniform(5.0, 12.0, size=14), 1),
    "Conversion Rate (%)": np.round(np.random.uniform(1.5, 4.0, size=14), 2)
})

# Layout: three metrics at top
a, b, c = st.columns(3)

# Latest values
a.metric("Daily Active Users", int(data['Daily Active Users'].iloc[-1]),
          int(data['Daily Active Users'].iloc[-1] - data['Daily Active Users'].iloc[-2]))

b.metric("Avg. Session Duration", f"{data['Avg. Session Duration (min)'].iloc[-1]} min",
          f"{data['Avg. Session Duration (min)'].iloc[-1] - data['Avg. Session Duration (min)'].iloc[-2]:+.1f} min")

c.metric("Conversion Rate", f"{data['Conversion Rate (%)'].iloc[-1]}%",
          f"{data['Conversion Rate (%)'].iloc[-1] - data['Conversion Rate (%)'].iloc[-2]:+.2f}%")

st.markdown("---")

# Time-series charts
st.line_chart(data.set_index('date'))

# Insight explanations
st.header("Key Insights")
insights = [
    "1. **User Growth:** Daily Active Users have grown by "
    f"{data['Daily Active Users'].iloc[-1] - data['Daily Active Users'].iloc[-2]} users "
    "in the last day, indicating strong adoption momentum.",

    "2. **Engagement:** The average session duration is "
    f"{data['Avg. Session Duration (min)'].iloc[-1]} minutes, up by "
    f"{data['Avg. Session Duration (min)'].iloc[-1] - data['Avg. Session Duration (min)'].iloc[-2]:.1f} minutes, "
    "showing users are finding value in the platform.",

    "3. **Conversion Efficiency:** Conversion rate stands at "
    f"{data['Conversion Rate (%)'].iloc[-1]}%, a "
    f"{data['Conversion Rate (%)'].iloc[-1] - data['Conversion Rate (%)'].iloc[-2]:.2f}% increase, "
    "demonstrating improved ability to turn engagement into action."
]
for line in insights:
    st.write(line)
