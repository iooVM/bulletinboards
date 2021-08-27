class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    _like = models.IntegerField(default = 1, db_column = 'amount')

    @property
    def like(self):
        return self._like

    @like.setter
    def like(self):
        self._like +1
        self.save()



