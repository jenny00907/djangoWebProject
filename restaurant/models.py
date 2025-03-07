from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    preview_image = models.ImageField(upload_to="article", null=True, blank=True)
    content = models.TextField()
    show_at_index = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Restaurant(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    branch_name = models.CharField(max_length=100, db_index=True)
    address = models.CharField(max_length=255, db_index=True)
    feature = models.CharField(max_length=255)
    is_closed = models.BooleanField(default=False)
    latitude = models.DecimalField(max_digits=16, decimal_places=12, db_index=True)
    logitude = models.DecimalField(max_digits=16, decimal_places=12, db_index=True)
    phone = models.CharField(max_length=16, help_text="E.164 포맷으로")
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    rating_count = models.PositiveIntegerField(default=0)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    last_order_time = models.TimeField(null=True, blank=True)
    category = models.ForeignKey(
        "RestaurantCategory", on_delete=models.SET_NULL, blank=True, null=True
    )

    tags = models.ManyToManyField("Tag", blank=True)


class CuisineType(models.Model):
    name = models.CharField("이름", max_length=20)

    class Meta:
        verbose_name = "음식 종류"
        verbose_name_plural = "음식 종류"


class RestaurantCategory(models.Model):
    name = models.CharField("이름", max_length=20)
    cuisine_type = models.ForeignKey(
        "CuisineType", on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        verbose_name = "가게 카테고리"
        verbose_name_plural = "가게 카테고리"


class RestaurantImage(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    is_representative = models.BooleanField(default=False)
    order = models.PositiveIntegerField(null=True, blank=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(max_length=100, upload_to="restaurant_image")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        verbose_name = "가게 이미지"
        verbose_name_plural = "가게 이미지"


class RestaurantMenu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        verbose_name = "가게 메뉴"
        verbose_name_plural = "가게 메뉴"


class Review(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    social_channel = models.ForeignKey(
        "SocialChannel", on_delete=models.SET_NULL, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        verbose_name = "리뷰"
        verbose_name_plural = "리뷰"
        ordering = ["-created_at"]


class ReviewImage(models.Model):
    image = models.ImageField(max_length=100, upload_to="review_images")
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        verbose_name = "리뷰 이미지"
        verbose_name_plural = "리뷰 이미지"


class SocialChannel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "소셜 채널"
        verbose_name_plural = "소셜 채널"


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "태그"
