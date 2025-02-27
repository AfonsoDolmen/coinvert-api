from fastapi import APIRouter, Path, Query
from converter import async_converter
from schemas import ConverterInput, ConverterOutput


router = APIRouter()


@router.get('/converter/{from_currency}')
async def converter(
    from_currency: str = Path(max_length=3, regex='^[A-Z]{3}$'),
    to_currencies: str = Query(max_length=50, regex='^[A-Z]{3}(,[A-Z]{3})*$'),
    price: float = Query(gt=0)
):
    to_currencies = to_currencies.split(',')

    result = []

    for currency in to_currencies:
        response = await async_converter(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )

        result.append(response)
    
    return result


@router.get('/converter/v2/{from_currency}', response_model=ConverterOutput)
async def converter(
    body: ConverterInput,
    from_currency: str = Path(max_length=3, regex='^[A-Z]{3}$')
):
    to_currencies = body.to_currencies
    price = body.price

    result = []

    for currency in to_currencies:
        response = await async_converter(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )

        result.append(response)
    
    return ConverterOutput(
        message='success',
        data=result
    )
