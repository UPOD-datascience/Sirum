import pandas as pd
import numpy as np
import sirum.config as cfg

class CovidDataSelection:

    def __init__(self,
                 country: str):
        self.country = country
        self.url_cases = cfg.URL_CASES
        self.url_deaths = cfg.URL_DEATHS
        self.url_recovered = cfg.URL_RECOVERED

    def create_data(self):
        data = self._load_cases()
        data = data.append([self._load_deaths(), self._load_recovered()],
                         ignore_index=True)
        data = data.drop(['Lat','Long','Country/Region','Province/State'],axis = 1).T
        data.columns = data.loc['type']
        data = data.drop('type',axis = 0)
        data.index = pd.to_datetime(data.index)
        data = data.apply(lambda x:x.astype(int))
        return data

    def _load_cases(self):
        cases = pd.read_csv(self.url_cases)
        cases = cases.loc[(cases['Country/Region'] == self.country) &
                          (cases['Province/State'].isnull())]
        cases['type'] = 'cases'
        return cases

    def _load_deaths(self):
        deaths = pd.read_csv(self.url_deaths)
        deaths = deaths.loc[(deaths['Country/Region'] == self.country) &
                            (deaths['Province/State'].isnull())]
        deaths['type'] = 'deaths'
        return deaths

    def _load_recovered(self):
        recovered = pd.read_csv(self.url_recovered)
        recovered = recovered.loc[(recovered['Country/Region'] == self.country) &
                                  (recovered['Province/State'].isnull())]
        recovered['type'] = 'recovered'
        return recovered
