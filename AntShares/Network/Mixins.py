
from AntShares.Core.Mixins import VerifiableMixin

class InventoryMixin(VerifiableMixin):

    hash = None
    inventory_type = None

    def Verify(self):
        pass

