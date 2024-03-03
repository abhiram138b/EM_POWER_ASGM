from pydantic import BaseModel, Field
from typing import Optional


class Asset(BaseModel):
    AssetID: int
    AssetName: Optional[str]
    AssetType: Optional[str]
    Location: Optional[str]
    PurchaseDate: Optional[str]
    InitialCost: Optional[float]
    OperationalStatus: Optional[str]


class PerformanceMetrics(BaseModel):
    AssetID: int
    Uptime: Optional[float]
    Downtime: Optional[float]
    MaintenanceCosts: Optional[float]
    FailureRate: Optional[float]
    Efficiency: Optional[float]
