from pydantic import AnyHttpUrl, BaseModel


class SummaryPayloadSchema(BaseModel):
    url: AnyHttpUrl


class SummaryResponseSchema(BaseModel):
    id: int
    url: str


class SummaryUpdatePayloadSchema(SummaryPayloadSchema):
    summary: str
