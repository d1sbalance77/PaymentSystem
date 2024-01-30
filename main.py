from fastapi import FastAPI

from currency.currency_api import currency_router
from database import Base,engine
from card.card_api import card_router
from transfers.transfers_api import transaction_router
from user.user_api import user_router
from starlette.templating import Jinja2Templates

Base.metadata.create_all(bind=engine)


app = FastAPI(title='Payment System', docs_url='/')

# HTML
template = Jinja2Templates(directory='templates')

from HTML_example.html_show import html_router
# ROUTER FOR HTML
app.include_router(html_router)

# ROUTERS
app.include_router(card_router)
app.include_router(transaction_router)
app.include_router(user_router)
app.include_router(currency_router)