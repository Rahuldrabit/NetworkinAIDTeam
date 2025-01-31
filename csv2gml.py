import pandas as pd

# Load CSV file
df = pd.read_csv("C:\Users\User\Documents\Network Aid\EmegencyTeam\Emergency Team(Edges).csv")

# Define GML file content
gml_content = "graph [\n"

# Add nodes
for _, row in df.iterrows():
    gml_content += f'  node [\n    id {row["id"]}\n    label "{row["label"]}"\n  ]\n'

gml_content += "]"

# Save to a file
with open("Emergency_Team_Nodes.gml", "w") as f:
    f.write(gml_content)

print("GML file created successfully!")
