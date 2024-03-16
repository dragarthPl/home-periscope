import enum

from attrs import define
from pyplumio.const import DeviceState


@define
class StoveState:
    PL_STATUS_MAP = {
        DeviceState.OFF: "Wyłączony",
        DeviceState.STABILIZATION: "Stabilizacja",
        DeviceState.KINDLING: "Rozpalanie",
        DeviceState.WORKING: "Praca",
        DeviceState.SUPERVISION: "Nadzór",
        DeviceState.PAUSED: "Pauza",
        DeviceState.STANDBY: "Gotowość",
        DeviceState.BURNING_OFF: "Spalanie",
        DeviceState.ALERT: "Alarm",
        DeviceState.MANUAL: "Ręczny",
        DeviceState.UNSEALING: "Otwieranie",
        DeviceState.OTHER: "Inny",
    }
    status: DeviceState

    def __str__(self):
        return self.PL_STATUS_MAP[self.status]
