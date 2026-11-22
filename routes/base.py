from fastapi  import FastAPI , APIRouter
import os 
from helper.config import get_settings

base_router=APIRouter()
@base_router.get("/welcome")

async def welcome():
    app_setting=get_settings()
    app_name=app_setting.APP_NAME
    app_version=app_setting.APP_VERSION
    return{
        "app_name":app_name,
        "app_version":app_version,
    }

