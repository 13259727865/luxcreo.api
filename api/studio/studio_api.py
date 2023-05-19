from api.login import Login
from base import mainpage, readyaml
from logs_config import root_log


class StudioApi(mainpage.HttpClient):

    # 历史记录api
    def history(self, page=1, size=10):
        root_log.info(f"开始调用历史记录api")
        # 历史记录接口
        url = self.api_url["history"]

        params = {'page': page,
                  'size': size}
        response = self.session.get(url=url, params=params)
        return response

    # 获取应用领域列表
    def fields(self):
        root_log.info(f"开始调用获取应用领域列表api")
        url = self.api_url["fields"]

        response = self.session.get(url=url)
        return response

    # 获取应用领域详情&下属晶格
    def fields_info(self, id, extends='lattice-list'):
        root_log.info(f"开始调用获取应用领域详情&下属晶格api")
        url = self.api_url["fields_info"]
        params = {
            'id': id,
            'extends': extends
        }
        response = self.session.get(url=url, params=params)
        return response

    #创建规则晶格生成任务
    def task_lattice(self,id):
        root_log.info(f"开始调用创建规则晶格生成任务api")
        url = self.api_url["task_lattice"]
        data = {
            "id":id
        }
        response = self.session.post(url=url,data=data)
        return response

    #创建渐变晶格生成任务
    def task_gradient(self, id):
        root_log.info(f"开始调用创建渐变晶格生成任务api")
        url = self.api_url["task_gradient"]
        data = {
            "id": id
        }
        response = self.session.post( url=url, data=data)
        return response

    #创建工作区
    def ws_create(self,extends="sources"):
        root_log.info(f"开始调用创建工作区api")
        url = self.api_url["ws_create"]
        data = {
            "extends":extends
        }

        response = self.session.post( url=url, data=data)
        return response

    #获取工作区详细内容
    def history_workspace(self,id):
        root_log.info(f"开始调用创建工作区api")
        url = self.api_url["history_workspace"]
        parames = {
            "id": id
        }
        response = self.session.post(url=url, parames=parames)
        return response

    #删除工作区
    def delete_workspace(self,id):
        root_log.info(f"开始调用删除工作区api")
        url = self.api_url["delete_workspace"]
        parames = {
            "id": id
        }
        response = self.session.delete(url=url, parames=parames)
        return response

    #给工作区添加文件
    def workspace_create_model(self):
        root_log.info(f"开始调用删除工作区api")
        url = self.api_url["workspace_create_model"]

        response = self.session.post(url=url)
        return response

    #获取渐变晶格列表
    def grayscale(self):
        root_log.info(f"开始调用获取渐变晶格列表api")
        url = self.api_url["grayscale"]

        response = self.session.get(url=url)
        return response

    #文件上传接口
    def upload_file(self):
        root_log.info(f"开始文件上传接口")
        url = self.api_url["upload_file"]

        files = [
            ('file', ('testfile', open('D:\play\pony-api-requests-master\model\样块-1.stl', 'rb'), 'application/octet-stream'))
        ]

        response = self.session.post(url=url, files=files)
        print(response.json())
        return response



if __name__ == '__main__':
    login = Login().auth_sign('13259727865', '1234qwer')
    history = StudioApi()
    history.upload_file()
