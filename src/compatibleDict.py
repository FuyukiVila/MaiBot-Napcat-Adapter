import re
from typing import List, Dict, Any


class CompatibleDict(dict):
    """
    兼容蛇形命名和驼峰命名的字典类
    自动支持 snake_case 和 camelCase 之间的转换
    """

    @staticmethod
    def snake_to_camel(snake_str: str) -> str:
        """将蛇形命名转换为驼峰命名"""
        if "_" not in snake_str:
            return snake_str
        components = snake_str.split("_")
        return components[0] + "".join(word.capitalize() for word in components[1:])

    @staticmethod
    def camel_to_snake(camel_str: str) -> str:
        """将驼峰命名转换为蛇形命名"""
        # 在大写字母前插入下划线，然后转换为小写
        snake_str = re.sub(r"(?<!^)(?=[A-Z])", "_", camel_str).lower()
        return snake_str

    def get(self, key, default=None):
        """
        重写 get 方法，支持蛇形命名和驼峰命名的自动转换
        """
        # 先尝试原始 key
        value = super().get(key)
        if value is not None:
            return value

        # 如果原始 key 不存在，尝试转换格式
        if "_" in key:
            # snake_case -> camelCase
            camel_key = self.snake_to_camel(key)
            value = super().get(camel_key)
            if value is not None:
                return value
        else:
            # 可能是 camelCase，尝试转换为 snake_case
            snake_key = self.camel_to_snake(key)
            value = super().get(snake_key)
            if value is not None:
                return value

        return default


def make_compatible(data: Any) -> Any:
    """
    递归地将普通字典转换为 CompatibleDict
    """
    if isinstance(data, dict):
        compatible_dict = CompatibleDict()
        for key, value in data.items():
            compatible_dict[key] = make_compatible(value)
        return compatible_dict
    elif isinstance(data, list):
        return [make_compatible(item) for item in data]
    else:
        return data
