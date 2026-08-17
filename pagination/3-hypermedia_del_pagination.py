#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a deletion-resilient page of the dataset.

        Args:
            index: The start index of the page to return.
            page_size: The number of items to return in the page.

        Returns:
            A dictionary containing index, next_index, page_size and
            data for the requested page, unaffected by items that may
            have been removed from the dataset between two queries.
        """
        data = self.indexed_dataset()
        assert index is not None and 0 <= index < len(self.dataset())

        page_data = []
        data_index = index
        while len(page_data) < page_size and data_index < len(self.dataset()):
            row = data.get(data_index)
            if row is not None:
                page_data.append(row)
            data_index += 1

        return {
            'index': index,
            'next_index': data_index,
            'page_size': len(page_data),
            'data': page_data,
        }
