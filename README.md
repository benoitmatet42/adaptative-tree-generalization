# Synthetic travel demand with surveys and OD matrices

This repositery contains the code used to generate synthetic travel demand for the region of Lyon and its surrounding, as described in:
> Matet, B., Côme, E., Furno, A. et al. Improving the generation of synthetic travel demand using origin–destination matrices from mobile phone data. Transportation (2024). https://doi.org/10.1007/s11116-024-10524-2

## Data
The synthetic travel demand relies on multiples sources. 

#### Census
Used to generate a population with realistic socio-economic composition. Available at https://www.insee.fr/fr/statistiques/3625223

#### IRIS
Zoning used for all geographic information in this work. Available at https://insee.fr/fr/information/2383182

#### Lyon HTS
Used to get agendas. Referenced as: doi:10.13144/lil-1023
Available upon request at https://data.progedo.fr/studies/doi/10.13144/lil-1023

#### Mobpro and mobsco
Used to complete census in the outskirts of Lyon. Referenced as: doi:10.13144/lil-1475 and doi:10.13144/lil-1476
Available upon request at https://data.progedo.fr/studies/doi/10.13144/lil-1475 
and https://data.progedo.fr/studies/doi/10.13144/lil-1476

#### OD matrices
The sharing of OD matrices is heavily discouraged under GDPR. The OD matrices used in this work are from ANR project PROMENADE (ANR-18-CE22-0008).

## How to use
Collect all the necessary data in a folder. Set the path to the folder in `config.json`. Run each notebook in order.