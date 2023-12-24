from pathlib import Path

import pandas as pd
import numpy as np


class Data():
    """
    A class representing a dataset.

    Attributes:
    - scale_path (str): The path to the scale file.
    - scale_name (str): The name of the scale.
    - df (pandas.DataFrame): The dataset as a pandas DataFrame.
    - split_point (tuple): The split points for categorizing scores.
    """

    def __init__(self, scale_path) -> None:
        """
        Initialize the Data class.

        Parameters:
        scale_path (str): The path to the scale file.

        Returns:
        None
        """
        self.scale_path = Path(f'~/proj/rt-dataset/src/data/{scale_path}.csv')
        self.scale_name = Path(self.scale_path).stem
        self.df = pd.read_csv(self.scale_path)
        self.df['is_careless_response'] = self.df.apply(self._is_careless_response, axis=1)
        self.df['total_response_time'] = self.df.apply(self._get_total_response_time, axis=1)
        self.split_point = self._get_split_point()
        self.df['label'] = self.df['score'] >= self.split_point[0]
    
    def sever_prop(self):
        """
        Calculate the severity proportions of each category based on the score and breakpoints.

        Returns:
            result (pandas.DataFrame): DataFrame containing the count, proportion, CR count, and CR \
            proportion of each category.
        """
        
        df = self.df
        breakpoints = self.split_point
        labels = list(range(0, len(breakpoints) + 1))

        def classify(score, breakpoints, labels):
            for bp, label in zip(breakpoints, labels):
                if score < bp:
                    return label
            return labels[-1]

        df['category'] = df['score'].apply(lambda x: classify(x, breakpoints, labels))
        # cal count
        category_counts = df.groupby('category').size()
        category_cr_counts = df.groupby('category')['is_careless_response'].sum()
        # cal ratio
        total = len(df)
        category_proportions = (category_counts / total * 100).map("{:.2f}%".format)
        # save result
        result = pd.DataFrame({'Count': category_counts, 'Proportion': category_proportions, 
                                'CR_Count': category_cr_counts})
        result['CR_Proportion'] = (result['CR_Count'] / result['Count'] * 100).map("{:.2f}%".format)
        return result

    def _get_total_response_time(self, row):
        """
        Calculates the total response time by summing up the values in the columns that start with 'time'.

        Parameters:
        row (pandas.Series): The row containing the data.

        Returns:
        float: The total response time.
        """

        # get rt columns
        arr = row.filter(regex='.*time.*').values

        return np.sum(arr)
    
    def _is_careless_response(self, row):
        """
        Checks if a response is considered careless based on the given row.

        Parameters:
        - row: pandas.Series
            The row containing the response data.

        Returns:
        - bool
            True if the response is considered careless, False otherwise.
        """
        # get rt columns
        arr = row.filter(regex='.*time.*').values

        if np.mean(arr) <= 1.5:
            return True
        elif np.max(arr) > 40:
            return True
        else:
            return False
        
    def _get_split_point(self):
        """
        Returns the split points for different scales based on the scale name.

        Returns:
            tuple or int: The split points for the scale. If the scale name is 'bss', returns an integer.
                          Otherwise, returns a tuple of integers representing the split points.
        """
        name = self.scale_name
        if name == 'phq9':
            return (5, 10, 15, 20)
        elif name == 'isi':
            return (8, 15, 22)
        elif name == 'gad7':
            return (5, 10, 14, 19)
        elif name == 'pss':
            return (15, 29, 43, 57)
        elif name == 'dass-yiyu':
            return (10, 14, 21, 28)
        elif name == 'dass-jiaolv':
            return (8, 10, 15, 20)
        elif name == 'dass-yali':
            return (15, 19, 26, 34)
        elif name == 'bss':
            return 1

    def __str__(self) -> str:
        return f'{self.scale_name} scale'

if __name__ == '__main__':
    data = Data('isi')