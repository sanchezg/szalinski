from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException, responses, status

from src.container import Container
from src.domain.model import URL
from src.domain.services.urls import UrlLookup, UrlStore

router = APIRouter()


@router.get("/")
async def index():
    return "Hello world, I'm Szalinski URL shortener"


@router.get("/{code}")
@inject
async def get_url(
    code: str,
    url_lookup: UrlLookup = Depends(Provide[Container.url_lookup]),
):
    url = await url_lookup(url_hash=code)
    if url:
        return responses.RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="URL hash not found"
    )


@router.post("/", response_model=URL)
@inject
async def submit_url(
    data: URL,
    url_store: UrlStore = Depends(Provide[Container.url_store]),
):
    url = data.url
    url_hash = await url_store(url=url)
    return URL(url=url, url_hash=url_hash)
