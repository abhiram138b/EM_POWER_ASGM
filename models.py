from pydantic import BaseModel, Field
from typing import Optional


class Asset(BaseModel):
    AssetID: int
    AssetName: Optional[str] = Field(None, title="Name of the asset")
    AssetType: Optional[str] = Field(None, title="Type of the asset")
    Location: Optional[str] = Field(None, title="Location of the asset")
    PurchaseDate: Optional[str] = Field(None, title="Date of asset purchase")
    InitialCost: Optional[float] = Field(None, title="Initial cost of the asset")
    OperationalStatus: Optional[str] = Field(None, title="Operational status of the asset")


class PerformanceMetrics(BaseModel):
    AssetID: int
    Uptime: Optional[float] = Field(None, title="Uptime of the asset")
    Downtime: Optional[float] = Field(None, title="Downtime of the asset")
    MaintenanceCosts: Optional[float] = Field(None, title="Maintenance costs of the asset")
    FailureRate: Optional[float] = Field(None, title="Failure rate of the asset")
    Efficiency: Optional[float] = Field(None, title="Efficiency of the asset")
