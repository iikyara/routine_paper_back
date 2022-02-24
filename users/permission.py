from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermission(BasePermission):
    def has_permission(self, request, view) -> bool:
        # 追加アクション以外は許可
        return view.action != "create"

    def has_object_permission(self, request, view, obj) -> bool:
        # 基本情報への閲覧は許可
        if request.method in SAFE_METHODS:
            return True
        # オブジェクト操作系は本人のみ有効
        return obj == request.user
