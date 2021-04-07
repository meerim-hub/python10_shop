from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, primary_key=True)

    def __str__(self):
        return self.name


#     варианты on_delete :
#     CASCADE - удалятся все продукты этой категории
#     SET_NULL - при удалении категории, значение поля catergory для связанных продуктов станет NUll
#     SET_DEFAULT - при удалении категории, значение поля catergory для связанных продуктах заменяет на дефолтное
#
#     PROTECT -
#     RESTRICT -
# не дает удалить при наличии товаров

#     DO_NOTHING


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')

    def __str__(self):
        return self.title


# ORM(Object-Relation-Mapping)
# TODO: Заполнить товары
# TODO: Сделать список товаров на сайте
# TODO: Добавить возможность