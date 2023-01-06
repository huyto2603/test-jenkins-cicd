import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from msteam import msteamipexpireftg
from connect_to_splunk import connect_to_splunk_ftg
from utils import get_ip_local
from typing import Union
from fastapi import FastAPI, Request, status, Response
from fastapi.responses import JSONResponse, HTMLResponse
import uvicorn
from pydantic import BaseModel


app = FastAPI()


class ItemFTG(BaseModel):
    host: str
    ip: str
    subnet: str
    group: str


@app.post("/sendmsteams/ftg/expire/")
def splunk_send_to_msteam(item: ItemFTG):
    try:

        ip4 = item.ip + " " + item.subnet

        result = msteamipexpireftg(item.host, ip4, item.group)
    except Exception as e:
        print(e)

    return result


@app.get("/blocklist_ip_local")
def getiplocal():
    splunk_service = connect_to_splunk_ftg(
        username="admin", password="Admin@123!", app="fortigate-adaptive-response"
    )
    print(splunk_service)
    html_content = """
    <html>
        <head>
            <title>Block List IP Local</title>
        </head>
        <body>
         <br> 
        <div>   <div>
    """
    # print(html_content)
    # iplocallist = get_ip_local(splunk_service)
    # print(iplocallist)
    # for item in iplocallist:
    #     if str(item["ip_addrs"]).find(",") > -1:
    #         for i in item["ip_addrs"]:
    #             # iplocal+=str(item["ip_addrs"])+"\n"
    #             html_content += f"""<div>{i.split(" ")[0]}/32<div>"""
    #     else:
    #         html_content += f"""<div>{str(item["ip_addrs"]).split(" ")[0]}/32<div>"""

    # html_content += """</body>
    #         </html>"""
    return HTMLResponse(content=html_content, status_code=200)


if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8081),
