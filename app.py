from flask import Flask
from flask_restful import Api, Resource, reqparse, request

# Optimizely
import azurepipelines_optimizely_sdk as aps

# Values to modify
PROJECT_ID = "12098094739"
EXPERIMENT_KEY = "Model_experiment"


apOptimizelySdk = aps.AzurePipelinesOptimizelySdk(PROJECT_ID, EXPERIMENT_KEY)

app = Flask(__name__)

@app.route("/azurepipelinesoptimizely/variation")
def variations():
    uid = request.args.get('uid')
    print(uid)
    variationKey = apOptimizelySdk.getVariationKey(uid)
    print(variationKey)
    if variationKey is None:
        variationKey = ""

    return variationKey

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

