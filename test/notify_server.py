import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from msteam import msteamipexpireftg

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


if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8081),
