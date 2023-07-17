import streamlit as st
import plotly.graph_objects as go

def create_sunburst_chart():
    # Data for the sunburst chart
    labels = ['World', 'Asia', 'Europe', 'Africa', 'North America', 'South America']
    parents = ['', 'World', 'World', 'World', 'World', 'World']
    values = [100, 50, 30, 20, 10, 5]

    # Create the sunburst chart figure
    fig = go.Figure(go.Sunburst(labels=labels, parents=parents, values=values))

    # Set the layout for the chart
    fig.update_layout(
        title='World Population (World Bank, 2017)',
        width=800,
        height=800,
    )

    # Display the sunburst chart
    st.plotly_chart(fig)

# Main Streamlit application
def main():
    st.title("Sunburst Chart Example")
    create_sunburst_chart()

if __name__ == '__main__':
    main()
