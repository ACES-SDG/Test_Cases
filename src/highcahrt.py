from highcharts_core.options.series.scatter import ScatterSeries
# Create a new ScatterSeries instance plotting df['actual']
actual_series = ScatterSeries.from_pandas(df,
                                          property_map={
                                              'x': 'idx',
                                              'y': 'actual',
                                              'id': 'actual',
                                              'name': 'Observed Value for Metric'
                                          },
                                          series_type='scatter'
                                          )
# Create a new ScatterSeries instance plotting df['forecast']
actual_series = ScatterSeries.from_pandas(df,
                                          property_map={
                                              'x': 'idx',
                                              'y': 'forecast',
                                              'id': 'forecast',
                                              'name': 'Forecast Value for Metric'
                                          }
                                          )
