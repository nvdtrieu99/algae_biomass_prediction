from sklearn.preprocessing import PolynomialFeatures
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from fastapi.responses import HTMLResponse

file = open(r"model/model.pkl", "rb")
model = pickle.load(file)
file.close()

poly = PolynomialFeatures(8)


class Factors(BaseModel):
    light: float
    temper: float
    turbidity: float
    airflow: float

app = FastAPI()



@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>Smart microalgae farming system</title>
        </head>
        <body>
            <h2>Smart microalgae farming system</h2>
            <div>Executor:</div>
            <h5>Nguyen Van Duong Trieu</h5>
            <h5>Doan Van Tinh</h5>
        </body>
    </html>
    """

@app.post("/algae_biomass_prediction")
async def prediction(factors: Factors):
    X = poly.fit_transform([[factors.light, factors.temper, factors.turbidity, factors.airflow]])
    y = model.predict(X)
    return y[0]

import uvicorn

if __name__ == '__main__':
    uvicorn.run('api:app', host="0.0.0.0", port=8080, reload=True)