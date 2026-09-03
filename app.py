
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("1_food_loss_waste_synthetic.csv")

st.title("FoodLens: India")
st.subheader("Food Loss & Waste Analysis")

st.write(
    "Dataset contains food-loss observations across commodities, "
    "food groups, years, and supply-chain stages."
)

st.dataframe(df.head(10))

st.header("Average Food Loss by Food Group")

food_group_summary = (
    df.groupby("Food_Group", as_index=False)["Loss_Percentage"]
      .mean()
      .sort_values("Loss_Percentage", ascending=False)
)

fig1 = px.bar(
    food_group_summary,
    x="Food_Group",
    y="Loss_Percentage",
    title="Average Food Loss by Food Group",
    labels={
        "Food_Group": "Food Group",
        "Loss_Percentage": "Average Loss Percentage"
    }
)

st.plotly_chart(fig1, use_container_width=True)

st.dataframe(food_group_summary)

st.header("Average Food Loss by Supply-Chain Stage")

stage_summary = (
    df.groupby("Supply_Chain_Stage", as_index=False)["Loss_Percentage"]
      .mean()
      .sort_values("Loss_Percentage", ascending=False)
)

fig2 = px.bar(
    stage_summary,
    x="Supply_Chain_Stage",
    y="Loss_Percentage",
    title="Average Food Loss by Supply-Chain Stage",
    labels={
        "Supply_Chain_Stage": "Supply-Chain Stage",
        "Loss_Percentage": "Average Loss Percentage"
    }
)

st.plotly_chart(fig2, use_container_width=True)

st.dataframe(stage_summary)

st.header("Average Food Loss Over the Years")

yearly_summary = (
    df.groupby("Year", as_index=False)["Loss_Percentage"]
      .mean()
      .sort_values("Year")
)

fig3 = px.line(
    yearly_summary,
    x="Year",
    y="Loss_Percentage",
    markers=True,
    title="Average Food Loss Trend Over the Years",
    labels={
        "Year": "Year",
        "Loss_Percentage": "Average Loss Percentage"
    }
)

st.plotly_chart(fig3, use_container_width=True)

st.dataframe(yearly_summary)

st.header("Top 10 Commodities by Average Food Loss")

top_10 = (
    df.groupby("Commodity", as_index=False)["Loss_Percentage"]
      .mean()
      .sort_values("Loss_Percentage", ascending=False)
      .head(10)
)

fig4 = px.bar(
    top_10,
    x="Loss_Percentage",
    y="Commodity",
    orientation="h",
    title="Top 10 Commodities by Average Food Loss",
    labels={
        "Loss_Percentage": "Average Loss Percentage",
        "Commodity": "Commodity"
    }
)

fig4.update_layout(yaxis={"categoryorder": "total ascending"})

st.plotly_chart(fig4, use_container_width=True)

st.dataframe(top_10)
