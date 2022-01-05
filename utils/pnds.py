import pandas as pd

class Pnds:
	# def __init__(self, val):
	# 	self.val = val

    def timestamp_to_index(data):
        data['timestamp'] = pd.to_datetime(data['timestamp'])
        # set timestamp to index
        data.set_index('timestamp', drop=True, inplace=True)

        return data