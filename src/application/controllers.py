from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException, Request, responses, status
from fastapi.templating import Jinja2Templates

from src import settings
from src.container import Container
from src.domain.model import URL
from src.domain.services.urls import UrlLookup, UrlStore

router = APIRouter()
templates = Jinja2Templates(directory="src/application/templates")


@router.get("/", response_class=responses.HTMLResponse)
@inject
async def index(
    request: Request,
    url: str = None,
    url_store: UrlStore = Depends(Provide[Container.url_store]),
):
    if url is None:
        return templates.TemplateResponse("index.html", context={"request": {}})
    url_hash = await url_store(url=url)
    return templates.TemplateResponse(
        "index.html",
        context={"request": request, "url_hash": f"{settings.BASE_URL}/{url_hash}"},
    )


@router.get("/{code}")
@inject
async def get_url(
    code: str,
    url_lookup: UrlLookup = Depends(Provide[Container.url_lookup]),
):
    if code == "favicon.ico":
        return

    url = await url_lookup(url_hash=code)
    if url:
        return responses.RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL hash not found")


@router.post("/", response_model=URL)
@inject
async def submit_url(
    data: URL,
    url_store: UrlStore = Depends(Provide[Container.url_store]),
):
    url = data.url
    url_hash = await url_store(url=url)
    return URL(url=url, url_hash=url_hash)
