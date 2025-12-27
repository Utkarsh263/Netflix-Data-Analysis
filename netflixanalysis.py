import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"

netflix_data = pd.read_csv("/content/netflix_content_2023.csv")


netflix_data.head()

