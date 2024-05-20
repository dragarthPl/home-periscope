import enum

from attrs import define
from pyplumio.const import DeviceState


@define
class StoveState:
    PL_STATUS_MAP = {
        DeviceState.OFF.value: "Wyłączony",
        DeviceState.STABILIZATION.value: "Stabilizacja",
        DeviceState.KINDLING.value: "Rozpalanie",
        DeviceState.WORKING.value: "Praca",
        DeviceState.SUPERVISION.value: "Nadzór",
        DeviceState.PAUSED.value: "Postój",
        DeviceState.STANDBY.value: "Czyszczenie",
        DeviceState.BURNING_OFF.value: "Wygaszanie",
        DeviceState.ALERT.value: "Alarm",
        DeviceState.MANUAL.value: "Ręczny",
        DeviceState.UNSEALING.value: "Otwieranie",
        DeviceState.OTHER.value: "Inny",
    }
    status: int

    def __str__(self) -> str:
        return self.PL_STATUS_MAP[self.status]
