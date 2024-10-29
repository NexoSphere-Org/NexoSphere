from graphviz import Digraph

# Initialize the Graph
dot = Digraph('Stock Market Data Aggregation Service Architecture', format='pdf')
dot.attr(rankdir='TB', size='10')

# Core Components of Architecture (Grouped by Layers)

# 1. Data Sources
dot.node('DataSources', 'Data Sources\n(Real-time & Historical APIs)', shape='parallelogram', style='filled', color='lightblue')

# 2. Data Ingestion Layer
dot.node('Ingestion', 'Data Ingestion\n(Azure Logic Apps, API Management)', shape='rectangle', style='filled', color='lightyellow')

# 3. Data Processing Layer
dot.node('Processing', 'Data Processing\n(Event Hub, Stream Analytics, Azure Functions)', shape='rectangle', style='filled', color='lightgreen')

# 4. Data Storage Layer
dot.node('Storage', 'Data Storage\n(Cosmos DB)', shape='cylinder', style='filled', color='lightpink')

# 5. API Layer
dot.node('API', 'API Layer\n(Azure API Management, SwaggerHub)', shape='rectangle', style='filled', color='lightcoral')

# 6. Optional Business Logic Layer
dot.node('BusinessLogic', 'Business Logic\n(Azure Functions, Machine Learning)', shape='rectangle', style='filled', color='lightgray')

# 7. User Interface Layer (Optional)
dot.node('UI', 'User Interface\n(Static Web Apps, Power BI)', shape='rectangle', style='filled', color='lavender')

# 8. Monitoring and Security
dot.node('Security', 'Monitoring & Security\n(Azure Monitor, Azure Key Vault)', shape='ellipse', style='filled', color='peachpuff')

# Data Flow Connections
dot.edge('DataSources', 'Ingestion', label='Fetch Data')
dot.edge('Ingestion', 'Processing', label='Standardize & Stream')
dot.edge('Processing', 'Storage', label='Process & Store')
dot.edge('Storage', 'API', label='Access Stored Data')
dot.edge('API', 'UI', label='Data for User Interface')
dot.edge('API', 'BusinessLogic', label='Data Processing & Analysis')
dot.edge('Security', 'API', label='Secure & Monitor', style='dotted')
dot.edge('Security', 'Storage', label='Secure Storage', style='dotted')

# Render the Graph
dot.render('docs/StockMarketServiceArchitecture')
