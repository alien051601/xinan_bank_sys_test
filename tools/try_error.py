

def request_error(error_info):
    print("捕获的异常为:", error_info)
    dict_str = {"code": "failed", "msg": error_info, "model": "检查接口完整url或数据是否有误"}
    return dict_str


def read_excel_error(error_info):
    print("捕获的异常为:", error_info)
    dict_str = {"code": "failed", "msg": error_info, "model": "从excel里面读取的数据有误"}
    return dict_str