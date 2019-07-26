from django.conf.urls import url
from meiduo_admin.views import users,statistical,channels,image,sku,spu,orders,goods,permission_user_manage,brands,specs


urlpatterns = [
    url(r'^authorizations/$', users.AdminAuthorizeView.as_view()),  # 后台登录
    url(r'^statistical/total_count/$', statistical.UserTotalCountView.as_view()),  # 总用户量
    url(r'^statistical/day_increment/$', statistical.UserDayIncrementView.as_view()),  # 日新增用户量
    url(r'^statistical/day_active/$', statistical.UserDayActiveView.as_view()),  # 日活跃
    url(r'^statistical/day_orders/$', statistical.UserDayOrderView.as_view()),  # 日订单
    url(r'^statistical/month_increment/$', statistical.UserMonthIncrementView.as_view()),  # 月用户量
    url(r'^statistical/goods_day_views/$', statistical.GoodView.as_view()),  # 日分类商品访问量

    url(r'^users/$', users.UserInfoView.as_view()),  # 用户信息
    url(r'^goods/channel_types/$', channels.ChannelTypeView.as_view()),  # 商品分组
    url(r'^goods/categories/$', channels.ChannelCategoryView.as_view()),  # 商品分组

    url(r'^skus/simple/$', image.ImageSKUView.as_view()),  # 图片中的sku
    url(r'^goods/simple/$', image.SPUView.as_view()),  # sku 中的spu下拉栏
    url(r'^skus/categories/$', sku.SKUSCategoriesView.as_view()),  #sku中的分类下拉栏


    url(r'^permission/content_types/$', permission_user_manage.PermissionViewSet.as_view({
        'get': 'content_type'
    })),  # 权限类型序列化器

    url(r'^permission/simple/$', permission_user_manage.GroupViewSet.as_view({
        'get': 'simple'
    })),  # 组管理

    url(r'^permission/groups/simple/$', permission_user_manage.UserManageViewSet.as_view({
        'get': 'admins'
    })),  # 管理员组管理

    url(r'^goods/brands/simple/$', goods.GoodsViewSite.as_view({
        'get': 'brands'
    })),  # 品牌




    url(r'^goods/channel/categories/$', spu.SPUCategoriesView.as_view()),  # 一级分类
    url(r'^goods/channel/categories/(?P<pk>\d+)/$', spu.SPUCategories1View.as_view()),  # 二级分类

    url(r'^goods/specs/simple/$', specs.SpecsOptionViewSet.as_view({'get': 'simple'})),  # 规格选项


]



from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('goods/channels', channels.ChannelsView, base_name='channels')
urlpatterns += router.urls

router = DefaultRouter()
router.register('goods/brands', brands.BrandViewSet, base_name='brands')
urlpatterns += router.urls

router = DefaultRouter()
router.register('goods/specs', specs.SpecsViewSet, base_name='specs')
urlpatterns += router.urls

router = DefaultRouter()
router.register('specs/options', specs.SpecsOptionViewSet, base_name='options')
urlpatterns += router.urls

router = DefaultRouter()
router.register('skus/images', image.ImageViewSet, base_name='images')
urlpatterns += router.urls

router = DefaultRouter()
router.register('skus', image.SKUViewSite, base_name='skus')
urlpatterns += router.urls

router = DefaultRouter()
router.register('orders', orders.OrdersViewSite, base_name='orders')
urlpatterns += router.urls

router = DefaultRouter()
router.register('goods', goods.GoodsViewSite, base_name='goods')
urlpatterns += router.urls

router = DefaultRouter()
router.register('permission/perms', permission_user_manage.PermissionViewSet, base_name='perms')
urlpatterns += router.urls


router = DefaultRouter()
router.register('permission/groups', permission_user_manage.GroupViewSet, base_name='groups')
urlpatterns += router.urls

router = DefaultRouter()
router.register('permission/admins', permission_user_manage.UserManageViewSet, base_name='admins')
urlpatterns += router.urls



