#!/usr/bin/env python3
"""
A simple pagination system for a dataset.
"""

import csv
from typing import List, Tuple

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
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load and cache dataset."""
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
