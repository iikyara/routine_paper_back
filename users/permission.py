from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        # アカウント作成は認証なしで提供
        if view.action == "create":
            return True
        # 閲覧はスーパーユーザに制限
        elif view.action == "list":
            return request.user.is_authenticated and request.user.is_superuser
        # それ以外のアクションは認証済みユーザに提供
        else:
            return request.user.is_authenticated

    def has_object_permission(self, request, view, obj) -> bool:
        # オブジェクト操作系は本人のみ有効
        return obj == request.user
