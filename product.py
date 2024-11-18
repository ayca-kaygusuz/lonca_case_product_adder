# ©️ Ayça Kaygusuz 2024

class Product:
    def __init__(self, stock_code, name, color, price, discounted_price, images, quantity, fabric, product_measurements, model_measurements, sample_size, series, created_at, updated_at):
        self.stock_code = stock_code
        self.name = name
        self.color = color  # This will be a list
        self.price = price
        self.discounted_price = discounted_price
        self.images = images
        self.quantity = quantity
        self.fabric = fabric
        self.product_measurements = product_measurements
        self.model_measurements = model_measurements
        self.sample_size = sample_size
        self.series = series
        self.created_at = created_at
        self.updated_at = updated_at