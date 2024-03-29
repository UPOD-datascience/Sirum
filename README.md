# Sirum

![Python package](https://github.com/UPOD-datascience/Sirum/workflows/Python%20package/badge.svg)

Repository to experiment with SIR-like models. The purpose 
is not to develop new SIR-models but rather to create a thin wrapper around
existing SIR-implementations to allow for easy experimentation. 

To start with:
1. We take the minimal SIR-model and combine it with a blackbox-optimiser like Optuna or Hyperopt
2. Expand the complexity of the SIR-model (SEIR, SEIRSPLUS, SIRF, SIS, SIRD, etc.)
3. Try different model paradigms?

Research questions:
1. what is the required immunity
2. how to include/extract the required IC-capacity in/from the model?

I.e. we have the following basic components: {{intial conditions}-> {SIR-model}} <-> {Optimisation/fitting}


Problems:
* the population is either assumed perfectly mixed or the parameters are identical over all stratifications -> this will lead to a gross over-estimation of the number of death/critically ill if the mildly affected patients are separated from the weak patients: **SEIRSplus** handles this.
* it does not have spatially separated population hubs that interact
* it does not have spatially centrally connected points where people interact


Suggestions for improvement:
* the mild, moderate and clinical patients should be physically separated in 3 models that interact
* those 3 models should operate in individual population hubs
* those population hubs should have central connection points


online calculators and dashboards:

- [https://alhill.shinyapps.io/COVID19seir/](https://alhill.shinyapps.io/COVID19seir/)  (SEIR)
- [https://gabgoh.github.io/COVID/index.html](https://gabgoh.github.io/COVID/index.html) (SEIR)
- [https://github.com/ryansmcgee/seirsplus](https://github.com/ryansmcgee/seirsplus) ****(SEIR)
- [https://covid19dashboards.com/covid-overview/](https://covid19dashboards.com/covid-overview/)

Crowd initiatives:

- [https://crowdfightcovid19.org/](https://crowdfightcovid19.org/)

Kaggle competitions: [https://www.kaggle.com/covid19](https://www.kaggle.com/covid19)

Good notebooks:

- [https://www.kaggle.com/saga21/covid-global-forecast-sir-model-ml-regressions](https://www.kaggle.com/saga21/covid-global-forecast-sir-model-ml-regressions)
- [https://www.kaggle.com/lisphilar/covid-19-data-with-sir-model](https://www.kaggle.com/lisphilar/covid-19-data-with-sir-model)
- [https://www.kaggle.com/super13579/covid-19-global-forecast-seir-visualize](https://www.kaggle.com/super13579/covid-19-global-forecast-seir-visualize)
- [https://doktormike.gitlab.io/ai-blogga/2020/03/17/covid-19/](https://doktormike.gitlab.io/ai-blogga/2020/03/17/covid-19/)
- [https://github.com/bsanderse/UQ_COVID](https://github.com/bsanderse/UQ_COVID)
- [example with PyMC3](https://colab.research.google.com/drive/13Ka-KV4HQMMRpdVYNJ3s_BkXg8ns8TnK#scrollTo=o22Tu93XJFTT)

Literature sources:

- [https://pages.semanticscholar.org/coronavirus-research](https://pages.semanticscholar.org/coronavirus-research)
- [https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology)

Data sources:

- [https://github.com/CSSEGISandData/COVID-19](https://github.com/CSSEGISandData/COVID-19)
- [http://ncov.bii.virginia.edu/dashboard/](http://ncov.bii.virginia.edu/dashboard/)
- https://github.com/fontastark/covid19nl
- [https://datasetsearch.research.google.com/search?query=coronavirus covid-19&docid=g3oiDuHtkLygNkWHAAAAAA%3D%3D](https://datasetsearch.research.google.com/search?query=coronavirus%20covid-19&docid=g3oiDuHtkLygNkWHAAAAAA%3D%3D)
- https://databronnencovid19.nl/

Specific papers:

- [https://statmodeling.stat.columbia.edu/2020/03/09/coronavirus-model-update-background-assumptions-and-room-for-improvement/](https://statmodeling.stat.columbia.edu/2020/03/09/coronavirus-model-update-background-assumptions-and-room-for-improvement/)
- [https://statmodeling.stat.columbia.edu/2020/03/07/coronavirus-age-specific-fatality-ratio-estimated-using-stan/](https://statmodeling.stat.columbia.edu/2020/03/07/coronavirus-age-specific-fatality-ratio-estimated-using-stan/)

Explanations:

- [https://www.youtube.com/watch?v=NKMHhm2Zbkw](https://www.youtube.com/watch?v=NKMHhm2Zbkw)
- [https://www.youtube.com/watch?v=uSLFudKBnBI](https://www.youtube.com/watch?v=uSLFudKBnBI)
