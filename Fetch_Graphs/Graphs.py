import datetime
import json

import plotly.graph_objects as go
import requests

testdata = [{'country': 'UK', 'total': 124743, 'new': 4676, 'total_death': 16509, 'new_death': 449, 'recovered': ''}, \
            {'country': 'USA', 'total': 777854, 'new': 13218, 'total_death': 41397, 'new_death': 822,
             'recovered': 71770}]

API_ADDR = ""  # replace the api address

class VirusGraphic():
    def barchar(self, virus_data):
        country_names = []
        recovered_values = []
        total_values = []
        death_values = []

        # scan the list and fetch country names
        for country in virus_data:
            country_names.append(country['country'])

        # collect go bar data
        for country in virus_data:

            recovered_values.append(country['new_death'])
            total_values.append(country['total'])
            death_values.append(country['total_death'])

        # print(new_values)
        fig = go.Figure(
            data=[
                go.Bar(name='recovered', x=country_names,
                       y=recovered_values
                       ),
                go.Bar(name='total cases', x=country_names,
                       y=total_values
                       ),
                go.Bar(name='total death', x=country_names,
                       y=death_values
                       )
            ]
        )

        fig.write_html('./figures/'+str(datetime.datetime.now().date())+'.html', auto_open=True)
        # fig.write_html('test.html')


if __name__ == '__main__':
    r = requests.get(API_ADDR)

    jsondata = json.loads(str(r.text))

    VirusGraphic().barchar(jsondata)
