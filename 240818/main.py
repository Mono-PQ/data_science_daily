import streamlit as st 
import pandas as pd 
import numpy as np 
import plotly.express as px 

st.title("Online Shopping Trends in Singapore")
st.write("*Data Source: [data.gov.sg](https://beta.data.gov.sg/collections/242/view)*")

# Online shopper by age group with cleaning to remove minors
shopper_agegroup = pd.read_csv("data/OnlineShoppersbyAgeGroup.csv")
shopper_agegroup = shopper_agegroup[~shopper_agegroup['age_group'].isin(['less than 7', '7 to 14 years'])]

st.write("### Line chart - Percentage of Online Shoppers by Age Group during 2007 - 2018")
st.write("From the chart above, we noted the following observations.")
st.markdown("- 25 to 34 years have the highest proportion of online shoppers at 95% in 2018. 15 to 24 years and 35 to 39 years followed closely behind at 83% in 2018.") 
st.markdown("- An increase in percentage of 50 to 59 years was observed between 2016 and 2018.")
st.markdown("- A worrying trend of those 60 and above where proportion of online shoppers remained largely unchanged. One possible reason can be the rate of technology adoption is slower for this age group.")

fig = px.line(shopper_agegroup, x='year', y='percentage', color='age_group', markers=True,
            title="% Online Shoppers by Age Group", labels={"age_group": "Age Group"})
st.plotly_chart(fig)


# Online shopper by value of purchase
shopper_purchasevalue = pd.read_csv("data/OnlineShoppersbyValueofPurchase.csv")

st.write("### Line chart - Percentage of Online Shoppers by Value of Purchase during 2007 - 2018")
st.markdown("From the chart above, the highest percentage of online purchases were valued less than $100 :dollar: in year 2018.")
st.markdown("As shown in the chart, purchases with value :red[more than $1,000] saw a dip :chart_with_downwards_trend: in 2013. One of the possible reasons could be consumers' concerns over the quality and legitimacy of products and/or services sold on online platforms (ref: [Alibaba spent US$161m fighting fakes since 2013](https://www.businesstimes.com.sg/startups-tech/technology/alibaba-spent-us161m-fighting-fakes-2013)). It could also be due to consumers' preference to experience the product in-stores before pricing such high valued products/services.")

fig2 = px.line(shopper_purchasevalue, x='year', y='percentage', color='value_of_purchase', markers=True,
            title="% Value of Purchase by Year", labels={"value_of_purchase": "Purchase Value"},
            template="plotly_white")
st.plotly_chart(fig2)