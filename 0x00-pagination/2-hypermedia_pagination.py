#!/usr/bin/env python3
"""
A simple pagination system for a dataset with hypermedia metadata.
"""

import csv
import math
from typing import List, Tuple, Dict, Any

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing the start and end indices for the pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index

class Server:
    """Server class to paginate a dataset of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the Server with the dataset set to None initially.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache dataset if it hasn't been loaded already.

        Returns:
        - List[List]: The dataset loaded from the CSV file, excluding the header.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page from the dataset.

        Parameters:
        - page (int): The current page number (1-indexed).
        - page_size (int): The number of items per page.

        Returns:
        - List[List]: A list of rows corresponding to the page.
        """
        assert isinstance(page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"
        
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        
        if start_index >= len(dataset):
            return []
        
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Get a page from the dataset with hypermedia metadata.

        Parameters:
        - page (int): The current page number (1-indexed).
        - page_size (int): The number of items per page.

        Returns:
        - Dict[str, Any]: A dictionary containing the hypermedia metadata.
        """
        data = self.get_page(page, page_size)
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)
        
        hypermedia = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
        
        return hypermedia
