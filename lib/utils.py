from const import APP_INDEX, FORTIGATE_ACTION_RESULTS_SOURCETYPE
from splunk_handler.interact import (
    splunk_query,
    get_search_result,
    splunk_query_oneshot,
)


def get_ip_local(service):
    query = f"""
        | search index="{APP_INDEX}" sourcetype="{FORTIGATE_ACTION_RESULTS_SOURCETYPE}" type="private" earliest=0 latest=now
        | dedup ip
        | stats values(ip)  as ip_addrs by ftg_fw_host
    """

    job = splunk_query(service, query)

    iplocallist = get_search_result(job)

    job.cancel()

    return iplocallist
