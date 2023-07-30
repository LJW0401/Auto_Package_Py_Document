import sys
import os
import PyInstaller
# from PyInstaller import __main__ as pyi_main
import subprocess


def App_path():
    """获得主程序的路径"""
    """Returns the base application path."""
    if hasattr(sys, 'frozen'):
        return os.path.dirname(sys.executable)  #使用pyinstaller打包后的exe目录
    return os.path.dirname(__file__)            #没打包前的py目录


def file_check(file_path:str):
    file_path = format_file_path(file_path)
    if os.path.exists(file_path):
        # print("文件存在")
        return True
    else:
        # print("文件不存在")
        return False
        
        
def format_file_path(oringinal_file_path:str) -> str:
    return '/'.join(oringinal_file_path.split('\\'))

        
class PackagePyDocument():
    def __init__(self):
        self.py_document_path = None
        self.show_console = False
        self.icon_path = None
        self.packaged_document_name = None
        self.save_packaged_document_path = None
        

    def InitPackageParam(self, py_document_path:str, show_console:bool, icon_path:str, packaged_document_name:str, save_packaged_document_path:str):
        self.py_document_path = py_document_path
        self.show_console = show_console
        self.icon_path = icon_path
        self.packaged_document_name = packaged_document_name
        self.save_packaged_document_path = save_packaged_document_path
        
        
    def AddPackagePyDocumentParam(self):
        # 获取源文件所在的目录
        script_dir = os.path.dirname(os.path.abspath(self.py_document_path))
        
        # # 设置 PyInstaller 的参数
        # args = [
        #     'pyinstaller',
        #     '-F',  # 生成单个可执行文件
        #     '-w',  # 无控制台窗口
        #     '-i', icon_path,  # 设置图标文件的路径
        #     '--distpath=' + script_dir,  # 设置生成文件的保存路径为源文件所在的目录
        #     '--workpath=' + script_dir,  # 设置工作目录为源文件所在的目录
        #     script_path  # 要打包的 Python 文件路径
        # ]
    
        # 设置 PyInstaller 的参数
        args = [
            'pyinstaller',
            '--onefile',  # 生成单个可执行文件
        ]
        
        if not self.show_console:
            args.append('--noconsole')# 不显示控制台
        
        if self.packaged_document_name != None:
            args.append(f'--name={self.packaged_document_name}')# 可执行文件的名称
        
        if self.icon_path != None:
            args.append(f'--icon={self.icon_path}')# 设置图标文件的路径
        
        args+=[
               '--specpath=' + script_dir,  # 设置生成的 spec 文件的保存路径为源文件所在的目录
               '--distpath=' + script_dir,  # 设置生成文件的保存路径为源文件所在的目录
               '--workpath=' + script_dir,  # 设置工作目录为源文件所在的目录
        ]
            
        args.append(self.py_document_path)  # 要打包的 Python 文件路径
        return args
        
        
    def PackagePyDocument(self,PackagePyDocumentParam):
        # 执行 PyInstaller 打包命令
        sys.argv = PackagePyDocumentParam
        # PyInstaller.__main__.run()
        # pyi_main.run()
        process = subprocess.Popen(PackagePyDocumentParam, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        
        self.InitPackageParam(None, False, None, None, None)# 重置打包参数为空
        
        print('打包完成')
        return process
        



if __name__ == '__main__':
    file_check('E:\\#LJW\\#Python_APPs\\AutoPackagePyDocument\\PackageTest\\HelloWorld.py')
    ppd = PackagePyDocument()
    ppd.InitPackageParam(
        py_document_path='E:/#LJW/#Python_APPs/AutoPackagePyDocument/PackageTest/HelloWorld.py',
        show_console=False,
        icon_path='E:/#LJW/#PolarBear_RM/Electric_Control/APPs/SerialPortAssistant/SerialPortAssistant.ico',
        packaged_document_name='packaged_script',
        save_packaged_document_path=None
    )
    
    args = ppd.AddPackagePyDocumentParam()
    
    process = ppd.PackagePyDocument(args)
    
    for line in iter(process.stdout.readline, b''):
        print('process out : ',line.decode())