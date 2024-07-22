#!/usr/bin/env python3
"""
A simple helper function for pagination.
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing the start and end indices for the pagination parameters.

    Parameters:
    - page (int): The current page number (1-indexed).
    - page_size (int): The number of items per page.

    Returns:
    - Tuple[int, int]: A tuple containing the start index and the end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
