# -- coding: UTF-8 --

from abc import ABC, abstractmethod
from common.helper import Helper


class LabelValueBase(ABC):
    @abstractmethod
    def parse(self, rom_elem):
        pass


# 取 export-config\\*-roms.xml 中 <Rom en> 的值
class EnLabelValue(LabelValueBase):
    def parse(self, rom_elem):
        return Helper.remove_region(rom_elem.get("en"))


# 取 export-config\\*-roms.xml 中 <Rom zhcn> 的值
class ZhcnLabelValue:
    def parse(self, rom_elem):
        return Helper.remove_region(rom_elem.get("zhcn"))
