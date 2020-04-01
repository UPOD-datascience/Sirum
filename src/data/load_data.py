import pandas as pd
import src.config as cfg

class CovidDataSelection:

    def __init__(self,
                 country: str):
        self.country = country
        self.url_cases = cfg.URL_CASES
        self.url_deaths = cfg.URL_DEATHS
        self.url_recovered = cfg.URL_RECOVERED

    def create_data(self):
        self.data = self._load_cases()
        self.data = self.data.append([self._load_deaths(), self._load_recovered()],
                         ignore_index=True)

    def _load_cases(self):
        cases = pd.read_csv(self.url_cases)
        cases = cases.loc[cases['Country/Region'] == self.country]
        cases['type'] = 'cases'
        return cases

    def _load_deaths(self):
        deaths = pd.read_csv(self.url_deaths)
        deaths = deaths.loc[deaths['Country/Region'] == self.country]
        deaths['type'] = 'deaths'
        return deaths

    def _load_recovered(self):
        recovered = pd.read_csv(self.url_recovered)
        recovered = recovered.loc[recovered['Country/Region'] == self.country]
        recovered['type'] = 'recovered'
        return recovered
