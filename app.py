import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import os

st.set_page_config(page_title="Fish Species Trait Explorer", layout="wide")

st.title("🐟 Fish Species Trait & Model Explorer")
st.markdown("Interactive exploration of fish physical traits, vulnerability, and machine learning predictions.")

# Dynamic path resolution to handle terminal launch variations
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_db_path():
    possible_paths = [
        os.path.join(BASE_DIR, "fish_species_project.db"),
        os.path.join(BASE_DIR, "sql", "fish_species_project.db"),
        os.path.join(BASE_DIR, "..", "sql", "fish_species_project.db"),
        os.path.join(BASE_DIR, "..", "fish_species_project.db"),
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return None

@st.cache_data
def load_data():
    db_path = get_db_path()
    if not db_path:
        raise FileNotFoundError("Could not find fish_species_project.db in local project directories.")
    
    conn = sqlite3.connect(db_path)
    df_traits = pd.read_sql("SELECT * FROM fish_species_traits;", conn)
    try:
        df_preds = pd.read_sql("SELECT * FROM fish_species_length_predictions;", conn)
        df_merged = pd.merge(df_traits, df_preds[['SpecCode', 'predicted_length', 'error']], on='SpecCode', how='left')
    except Exception:
        df_merged = df_traits
    conn.close()
    return df_merged

try:
    df = load_data()

    # Sidebar filters
    st.sidebar.header("Filter Options")
    shapes = ["All"] + list(df['BodyShapeI'].dropna().unique())
    selected_shape = st.sidebar.selectbox("Body Shape", shapes)
    
    if selected_shape != "All":
        df_filtered = df[df['BodyShapeI'] == selected_shape]
    else:
        df_filtered = df

    # Summary Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Species", len(df_filtered))
    col2.metric("Avg Length (cm)", f"{df_filtered['Length'].mean():.2f}")
    col3.metric("Avg Weight (g)", f"{df_filtered['Weight'].mean():.2f}")
    col4.metric("Avg Vulnerability", f"{df_filtered['Vulnerability'].mean():.2f}")

    # Display Visualizations
    tab1, tab2, tab3 = st.tabs(["📊 EDA & Trait Distributions", "🤖 Model Predictions", "📋 Raw Data"])

    with tab1:
        st.subheader("Length vs Weight by Vulnerability")
        fig_scatter = px.scatter(
            df_filtered, 
            x="Weight", 
            y="Length", 
            color="Vulnerability",
            hover_data=["Genus", "Species"],
            title="Fish Length vs Weight"
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

    with tab2:
        st.subheader("Actual vs Predicted Length")
        if 'predicted_length' in df_filtered.columns:
            fig_pred = px.scatter(
                df_filtered, 
                x="Length", 
                y="predicted_length", 
                color="error",
                hover_data=["Genus", "Species"],
                labels={"Length": "Actual Length (cm)", "predicted_length": "Predicted Length (cm)"},
                title="Actual vs Model Predicted Length"
            )
            st.plotly_chart(fig_pred, use_container_width=True)
        else:
            st.info("Run the notebook modeling cells to populate predictions into the SQLite database.")

    with tab3:
        st.subheader("Filtered Dataset")
        st.dataframe(df_filtered)

except Exception as e:
    st.error(f"Error loading dataset: {e}")
