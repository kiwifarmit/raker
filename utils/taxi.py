class Taxi:
	# def __init__(self, val):
	# 	self.val = val

    def features_create(data):
        # resample timeseries to hourly
        data = data.resample('H').sum()

        # create features from date
        data['day'] = [i.day for i in data.index]
        data['day_name'] = [i.day_name() for i in data.index]
        data['day_of_year'] = [i.dayofyear for i in data.index]
        data['week_of_year'] = [i.weekofyear for i in data.index]
        data['hour'] = [i.hour for i in data.index]
        data['is_weekday'] = [i.isoweekday() for i in data.index]

        return data

    def resample_hourly(data):
        data = data.resample('H').sum()

        return data