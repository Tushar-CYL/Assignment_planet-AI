import streamlit as st
from agents.market_research_agent import market_research
from agents.use_case_generation_agent import generate_use_cases
from agents.asset_collection_agent import collect_datasets
from agents.proposal_compiler import compile_proposal

# Streamlit App Layout
st.title("Multi-Agent AI Project - Customer Support Solutions")

st.sidebar.title("Steps")
selected_step = st.sidebar.radio("Select Step:", ["Market Research", "Use Case Generation", "Dataset Collection", "Proposal Compilation"])

# Step 1: Market Research
if selected_step == "Market Research":
    st.header("Market Research Agent")
    if st.button("Run Market Research Agent"):
        market_research()
        st.success("Market Research completed! Insights saved in 'results/research_insights.json'.")
        st.write(open("results/research_insights.json").read())

# Step 2: Use Case Generation
elif selected_step == "Use Case Generation":
    st.header("Use Case Generation Agent")
    if st.button("Generate Use Cases"):
        generate_use_cases()
        st.success("Use Cases generated! Check 'results/use_cases.md'.")
        st.markdown(open("results/use_cases.md").read())

# Step 3: Dataset Collection
elif selected_step == "Dataset Collection":
    st.header("Dataset Collection Agent")
    if st.button("Collect Datasets"):
        collect_datasets()
        st.success("Datasets collected! Check 'results/datasets_links.md'.")
        st.markdown(open("results/datasets_links.md").read())

# Step 4: Proposal Compilation
elif selected_step == "Proposal Compilation":
    st.header("Proposal Compilation")
    if st.button("Compile Final Proposal"):
        compile_proposal()
        st.success("Proposal compiled! Check 'results/final_proposal.pdf'.")
        st.markdown("Download the proposal [here](results/final_proposal.pdf)", unsafe_allow_html=True)
