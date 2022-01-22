from rest_framework import permissions


class IsOwnerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj) -> bool:
        # オブジェクト操作系は所有者のみ有効
        return obj.owner == request.user
