# Customer Churn Prediction

Tämä projekti ennustaa asiakaspoistumaa koneoppimismallilla, joka on rakennettu Kerasin avulla.

## Projektirakenne
- `data/`: Sisältää raakadatana Telco churn datasetin.
- `notebooks/`: Esikäsittely, mallin koulutus ja arviointi (Jupyter).
- `src/`: Esiprosessointi, mallin koulutus ja ennustus.
- `api/`: FastAPI-palvelu ennustuksille.
- `azureml/`: AzureML pipeline määrittely.
- `model/`: Tallennetut mallit.

## Käyttöohjeet

### 1. Asenna riippuvuudet
```bash
pip install -r requirements.txt
