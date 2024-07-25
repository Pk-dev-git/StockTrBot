class DataModel:
    def __init__(self):
        self.itemList=[]
        self.stockBalanceList= []

    class ItemInfo:
        def __init__(self, itemCode, itemName):
            self.itemCode = itemCode
            self.itemName = itemName

