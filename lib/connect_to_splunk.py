import splunklib.client as client
import splunklib.results as results
import json


def connect_to_splunk_ftg(
    username,
    password,
    app,
    host="127.0.0.1",
    port="8089",
    owner="admin",
    sharing="user",
):
    try:
        service = client.connect(
            host=host,
            port=port,
            username=username,
            password=password,
            owner=owner,
            app=app,
            sharing=sharing,
        )
        if service:
            print("Splunk service created successfully")
            print("------------------------------------")
        return service
    except Exception as e:
        print(e)


def run_normal_mode_search_ftg(splunk_service, search_string, payload={}):
    try:
        job = splunk_service.jobs.create(search_string, **payload)
        # print(job.content)
        while True:
            while not job.is_ready():
                pass
            if job["isDone"] == "1":
                break
        for result in results.ResultsReader(job.results()):
            return result

    except Exception as e:
        print(e)


def main():
    try:
        splunk_service = connect_to_splunk(username="admin", password="Admin@123!")
        search_string = '| ftgblockip group_name="test" hostname="192.168.135.55" ip="9.9.9.9 255.255.255.255" '
        payload = {"exec_mode": "normal"}
        run_normal_mode_search(splunk_service, search_string, payload)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
