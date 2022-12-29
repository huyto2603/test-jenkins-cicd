from const import REALM

import splunklib.results as results
import splunklib.client as client


def get_credential(service, realm, account_name):
    secrets = service.storage_passwords
    for secret in secrets:
        if secret.content.username == account_name and secret.content.realm == realm:
            return secret.clear_password
    return None


def splunk_query(service, query):
    jobs = service.jobs
    kwargs_blockingsearch = {"exec_mode": "blocking"}
    job = jobs.create(query, **kwargs_blockingsearch)
    return job


def get_search_result(job):
    return [elemt for elemt in results.ResultsReader(job.results())]


def splunk_query_oneshot(service, query):
    kwargs_oneshot = {
        "earliest_time": "0",
        "latest_time": "now",
        "output_mode": "json",
        "count": 0,
    }

    oneshotsearch_results = service.jobs.oneshot(query, **kwargs_oneshot)

    # Get the results and display them using the JSONResultsReader
    reader = results.JSONResultsReader(oneshotsearch_results)

    return [elemt for elemt in reader]
