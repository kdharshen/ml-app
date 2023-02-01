# Simple ML-app as a rest API using Flask 
## Overview
This API is used to run a ML model in REST API.

## Model
Model used in this version is trained with the IRIS Dataset and Decision Tree algorithm.
Model input parameters - [Sepal_Length --> Float, Sepal_Width --> Float, Petal_Length --> Float, Petal_Width --> FLoat]

Model predicts the *Species* for the given parameters.

## API
List of the API :

`[POST]` `/predict` json `{ "input": [Sepal_Length, Sepal_Width, Petal_Length, Petal_Width]}` - returns the predicted output value for the given input parameters.
