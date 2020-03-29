# Sirum

Repository to experiment with SIR-like models. The purpose 
is not to develop new SIR-models but rather to create a thin wrapper around
existing SIR-implementations to allow for easy experimentation. 

To start with:
1. We take the minimal SIR-model and combine it with a blackbox-optimiser like Optuna or Hyperopt
2. Expand the complexity of the SIR-model (SEIR, SEIRSPLUS, SIRF, SIS, SIRD, etc.)

Research questions:
1. what is the required immunity 

I.e. we have the following basic components: {{intial conditions}-> {SIR-model}} <-> {Optimisation/fitting}


# Compartmental models 

## SIR 
In epidemiology *compartmental* refers to the state a person is in with regard to a viral disease. 
The most well-known model is the SIR-model that contains:
* S: susceptible, referring to those who can get infected
* I: infectious, referring to those that are infected and can infect others
* R: removed, referring to those that are recovered/removed because of death or because recovery is associated with immunity

## SEIR
A variant with a higher granularity is the SEIR-model where those that are infected are split in the latent infected (or exposed)
and active infected (or infectious) i.e.
* S: susceptible, referring to those who can get infected
* E: exposed, referring to those that are infected and cannot yet infect others
* I: infectious, referring to those that are infected and can infect others
* R: removed, referring to those that are recovered/removed because of death or because recovery is associated with immunity

## SEIRS
Moving up in granularity we can also add the idea that an individual might become re-susceptible, this
leads to the SEIRS-model:
* S: susceptible, referring to those who can get infected
* E: exposed, referring to those that are infected and cannot yet infect others
* I: infectious, referring to those that are infected and can infect others
* R: removed, referring to those that are recovered/removed because of death or because recovery is associated with immunity
* S: re-susceptible; indicated with a parameter $$\xi$$ 

```math
a^2+b^2=c^2
```


$$\begin{aligned}
\dot{S} &= \frac{-\beta S I}{N} + \xi R \\
\dot{E} &= \frac{\beta S I}{N} - \sigma E \\
\dot{I} &= \sigma E - \gamma I - \mu_I I \\
\dot{R} &= \gamma I - \xi R \\ dot{F} &= \mu_I I \\
\quad\quad N = S + E + I + R
\end{aligned}$$

## SEIRS with testing



## SEIRS with testing and vital dynamics



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

Literature sources:

- [https://pages.semanticscholar.org/coronavirus-research](https://pages.semanticscholar.org/coronavirus-research)
- [https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology)

Data sources:

- [https://github.com/CSSEGISandData/COVID-19](https://github.com/CSSEGISandData/COVID-19)
- [http://ncov.bii.virginia.edu/dashboard/](http://ncov.bii.virginia.edu/dashboard/)
- [https://datasetsearch.research.google.com/search?query=coronavirus covid-19&docid=g3oiDuHtkLygNkWHAAAAAA%3D%3D](https://datasetsearch.research.google.com/search?query=coronavirus%20covid-19&docid=g3oiDuHtkLygNkWHAAAAAA%3D%3D)

Specific papers:

- [https://statmodeling.stat.columbia.edu/2020/03/09/coronavirus-model-update-background-assumptions-and-room-for-improvement/](https://statmodeling.stat.columbia.edu/2020/03/09/coronavirus-model-update-background-assumptions-and-room-for-improvement/)
- [https://statmodeling.stat.columbia.edu/2020/03/07/coronavirus-age-specific-fatality-ratio-estimated-using-stan/](https://statmodeling.stat.columbia.edu/2020/03/07/coronavirus-age-specific-fatality-ratio-estimated-using-stan/)

Explanations:

- [https://www.youtube.com/watch?v=NKMHhm2Zbkw](https://www.youtube.com/watch?v=NKMHhm2Zbkw)
- [https://www.youtube.com/watch?v=uSLFudKBnBI](https://www.youtube.com/watch?v=uSLFudKBnBI)
