import requests

# define endpoint
api_url = "https://e8nuunz76exd7o1d.eastus.azure.endpoints.huggingface.cloud/predict"
headers = {
    "Accept": "application/json",
    "Authorization": "Bearer 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",
    "Content-Type": "application/json"
}

# Function to summarize text
def summarize_text(text, max_length=50):
    # Create payload contents
    payload = {
        "inputs": f"summarize: {text}",
        "parameters": {"max_length": max_length}
    }
    
    # Make the POST request
    response = requests.post(api_url, headers=headers, json=payload)
    
    # Check if the request was successful
    if response.status_code == 200:
        try:
            # Parse JSON response and get the summary text
            summary = response.json()[0].get('translation_text', "Summary text not found")
            return summary
        except (KeyError, IndexError):
            print("Error: Unexpected response format", response.json())
            return None
    else:
        print(f"Error: {response.status_code}, {response.json()}")
        return None

# Example usage
text_to_summarize = (
    "Osmosis is a vital process in biological systems, as biological membranes are semipermeable. "
    "In general, these membranes are impermeable to large and polar molecules, such as ions, proteins, "
    "and polysaccharides, while being permeable to non-polar or hydrophobic molecules like lipids as well as "
    "to small molecules like oxygen, carbon dioxide, nitrogen, and nitric oxide. Permeability depends on "
    "solubility, charge, or chemistry, as well as solute size. Water molecules travel through the plasma "
    "membrane, tonoplast membrane (vacuole) or organelle membranes by diffusing across the phospholipid bilayer "
    "via aquaporins (small transmembrane proteins similar to those responsible for facilitated diffusion and "
    "ion channels). Osmosis provides the primary means by which water is transported into and out of cells. "
    "The turgor pressure of a cell is largely maintained by osmosis across the cell membrane between the cell "
    "interior and its relatively hypotonic environment."
)

# Call the summarize_text function to generate the summary
summary = summarize_text(text_to_summarize)
print("Summary:", summary)