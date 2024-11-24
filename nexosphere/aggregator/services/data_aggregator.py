# TODO: Implement a more sophisticated aggregation algorithm

from typing import List, Dict, Any

def aggregate_data_naively(data_sources: List[Any], source_names: List[str]) -> Dict[str, Any]:
    """
    Aggregates data from multiple sources into a dictionary using provided source names as keys.

    Args:
        data_sources (List[Any]): A list of data sources to be aggregated.
        source_names (List[str]): A list of names corresponding to each data source.

    Returns:
        Dict[str, Any]: A dictionary where keys are source names and values are the corresponding data sources.
    """

    aggregated_data = {}
    for source, name in zip(data_sources, source_names):
        aggregated_data[name] = source
    return aggregated_data