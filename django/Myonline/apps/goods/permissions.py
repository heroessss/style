from rest_framework import permissions
class CustomerAccessPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # 任何请求都允许读取权限，
        # 所以我们总是允许GET，HEAD或OPTIONS 请求.
        if request.method  == "PATCH":
            return False

        # 示例必须要有一个名为`owner`的属性
        return True