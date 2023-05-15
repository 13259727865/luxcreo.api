import json
import os


class JsonIO:
    main_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # 读取json文件内容
    def read_json(self, filename=rf"{main_path}\config.json"):
        # json.load(open(file=r"E:\LuxFlow_front\config.json",encoding="utf-8"))
        with open(file=filename, encoding="utf-8") as f:
            return json.load(f)

    def test(self):
        print()


if __name__ == '__main__':
    print(JsonIO().read_json())