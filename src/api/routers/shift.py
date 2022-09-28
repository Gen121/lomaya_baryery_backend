from http import HTTPStatus

from fastapi import APIRouter, Depends

from src.api.request_models.shift import ShiftCreateRequest
from src.api.response_models.shift import ShiftResponse
from src.core.services.shift_service import ShiftService, get_shift_service

router = APIRouter(prefix="/shift", tags=["Shift"])


@router.post("/", response_model=ShiftResponse, response_model_exclude_none=True, status_code=HTTPStatus.CREATED)
async def create_new_shift(
    shift: ShiftCreateRequest,
    shift_service: ShiftService = Depends(get_shift_service),
) -> ShiftResponse:
    return await shift_service.create_new_shift(shift)
