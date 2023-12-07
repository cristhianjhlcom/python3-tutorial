class Invoice:
    def __init__(self, invoice_number, seller_name, buyer_name, created_at, items):
        self.invoice_number = invoice_number
        self.seller_name = seller_name
        self.buyer_name = buyer_name
        self.created_at = created_at
        self.items = items

    def get_total(self):
        return sum([item['price'] for item in self.items])

    def print_details(self):
        print(f"Invoice Nro. {self.invoice_number}")
        print(f"Seller Name - {self.seller_name}")
        print(f"Buyer Name - {self.buyer_name}")
        print("Details")
        for item in self.items:
            print(f"Item {item['description']} ${item['price']}")
        print(f"Total ${self.get_total()}")

items = [
    {"description": "Camisa", "price": 20},
    {"description": "Zapatos", "price": 30},
    {"description": "Medias", "price": 10},
    {"description": "Pantalon", "price": 50},
]

class StandardInvoice(Invoice):
    pass

class CommercialInvoice(Invoice):
    def __init__(self, invoice_number, seller_name, buyer_name, created_at, items, shipping_address):
        super().__init__(invoice_number, seller_name, buyer_name, created_at, items)
        self.shipping_address = shipping_address

    def print_details(self):
        print("Commercial Invoice")
        super().print_details()
        print(f"Shipping Addres {self.shipping_address}")

class ElectronicInvoice(Invoice):
    def __init__(self, invoice_number, seller_name, buyer_name, created_at, items, format):
        super().__init__(invoice_number, seller_name, buyer_name, created_at, items)
        self.format = format

    def print_details(self):
        print("Electronic Invoice")
        super().print_details()
        print(f"Format to Download {self.format}")

standar = StandardInvoice('1', 'Cristhian', 'Victor', '2023-11-06', items)

commercial = CommercialInvoice(
        invoice_number='123j12',
        seller_name='Cristhian',
        buyer_name='Victor',
        created_at='2023-11-06',
        items=items,
        shipping_address="Lima",
)

electronic = ElectronicInvoice(
    invoice_number="akj23",
    seller_name="Edith",
    buyer_name="Katherine",
    items=items,
    created_at="2023-11-06",
    format="PDF",
)

