from flask import Flask, render_template, request
import json
from peopledatalabs import PDLPY

app = Flask(__name__)

# Create a client, specifying your API key
CLIENT = PDLPY(api_key="c68df9c92a576cd79c91d7b037221ba0c5e9e90b194c9ba03529b2352dc68ed6")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enrich", methods=["POST"])
def enrich():
    # Get user input for email
    email = request.form["email"]

    # Create a parameters JSON object
    PARAMS = {"email": [email]}

    # Pass the parameters object to the Person Enrichment API
    json_response = CLIENT.person.enrichment(**PARAMS).json()

    # Check for successful response
    if json_response["status"] == 200:
        record = json_response['data']

        # Print selected fields
        print(
            record['work_email'],
            record['full_name'],
            record['job_title'],
            record['job_company_name']
        )

        print(f"Successfully enriched profile with PDL data.")

        # Save enrichment data to JSON file
        with open("my_pdl_enrichment.jsonl", "w") as out:
            out.write(json.dumps(record, indent=4) + "\n")
    else:
        print("Enrichment unsuccessful. See error and try again.")
        print("error:", json_response)

    return render_template("result.html", json_response=json.dumps(record, indent=4))


if __name__ == "__main__":
    app.run(debug=True)
