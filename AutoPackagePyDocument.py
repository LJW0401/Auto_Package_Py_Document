import tkinter as tk
import tkinter.ttk
import tkinter.messagebox
# import PyInstaller
# from PyInstaller import __main__ as pyi_main
import subprocess
import sys
import io

import AutoPackagePyDocument_lib as appdl


ENTRY_LENGTH = 70 #输入框长度
PACKAGE_PARAM_IPADY = 5 #打包参数组件的ipady


class AutoPackagePyDocument():
    def __init__(self) -> None:
        '''初始化'''
        self.root = tk.Tk()
        self.version = 'V1.0.1'
        self.auto_package_py_document_module = appdl.PackagePyDocument()
        self.py_document_path = tk.StringVar()
        # self.py_document_path.set('E:\#LJW\#Python_APPs\AutoPackagePyDocument\AutoPackagePyDocument.py')
        self.icon_path = tk.StringVar()
        self.py_document_path.trace('w', self.MonitoringPyDocumentPathChanges)
        # self.icon_path.set('E:\#LJW\#Python_APPs\AutoPackagePyDocument\AutoPackagePyDocument.ico')
        self.packaged_document_name = tk.StringVar()
        # self.packaged_document_name.set('packaged_script')
        
        
    def InitUI(self):
        '''初始化UI'''
        self.root.title('Package Py Document  ' + self.version)
        self.root.geometry('720x550')
        self.root.resizable(0,0)
        # self.root.iconbitmap('E:\#LJW\#Python_APPs\AutoPackagePyDocument\AutoPackagePyDocument.ico')
        
        self.InitMenu()
        self.InitFrame()
        
    
    def InitMenu(self):
        '''初始化菜单栏'''
        #菜单栏
        MenuBar = tk.Menu(self.root)
        self.root.config(menu=MenuBar)
        #菜单栏/文件
        # Menu_File = tk.Menu(MenuBar, tearoff=0)
        # MenuBar.add_cascade(label='文件', menu=Menu_File)
        #菜单栏/文件/打开
        # Menu_File.add_command(label='打开', command=self.BlankFunction)
        #菜单栏/文件/保存
        # Menu_File.add_command(label='保存输入波形图', command=self.SaveInputWaveform_Click)
        #菜单栏/文件/退出
        # Menu_File.add_command(label='退出', command=self.Quit_App)
        #菜单栏/帮助
        Menu_Help = tk.Menu(MenuBar, tearoff=0)
        MenuBar.add_cascade(label='帮助', menu=Menu_Help)
        #菜单栏/帮助/如何使用
        Menu_Help.add_command(label='注意事项', command=self.PayAttentionTo_Click)
        #菜单栏/帮助/关于
        # Menu_Help.add_command(label='关于程序', command=hw.RunAbout)
        #菜单栏/帮助/历史版本
        # Menu_Help.add_command(label='历史版本', command=self.BlankFunction)
    
    
    def InitFrame(self):
        '''初始化内部组件'''
        Frame_PackageParam = tk.Frame(
            self.root,
            #relief='groove',bd=1
        )
        Frame_PackageParam.pack(side=tk.TOP)
        
        Frame_PyDocumentPath = tk.Frame(
            Frame_PackageParam,
            #relief='groove',bd=1
        )
        Frame_PyDocumentPath.pack(side=tk.TOP,ipady=PACKAGE_PARAM_IPADY)
        
        Label_PyDocumentPath = tk.Label(
            Frame_PyDocumentPath,
            text='Python文件路径:',
            font=('黑体', 12),
            anchor='e',
            width=15,height=1
        )
        Label_PyDocumentPath.pack(side=tk.LEFT)
        
        self.Entry_PyDocumentPath = tk.Entry(
            Frame_PyDocumentPath,
            textvariable=self.py_document_path,
            font=('黑体', 12),
            width=ENTRY_LENGTH,
        )
        self.Entry_PyDocumentPath.pack(side=tk.RIGHT)
        
        Frame_SavePackagedDocumentPath = tk.Frame(
            Frame_PackageParam,
            #relief='groove',bd=1
        )
        # Frame_SavePackagedDocumentPath.pack(side=tk.TOP,ipady=PACKAGE_PARAM_IPADY)
        
        Label_SavePackagedDocumentPath = tk.Label(
            Frame_SavePackagedDocumentPath,
            text='保存文件路径:',
            font=('黑体', 12),
            anchor='e',
            width=15,height=1
        )
        Label_SavePackagedDocumentPath.pack(side=tk.LEFT)
        
        self.Entry_SavePackagedDocumentPath = tk.Entry(
            Frame_SavePackagedDocumentPath,
            textvariable=self.packaged_document_name,
            font=('黑体', 12),
            width=ENTRY_LENGTH,
        )
        self.Entry_SavePackagedDocumentPath.pack(side=tk.RIGHT)
        
        Frame_ShowConsole = tk.Frame(
            Frame_PackageParam,
            #relief='groove',bd=1
        )
        Frame_ShowConsole.pack(side=tk.TOP,fill=tk.X,ipady=PACKAGE_PARAM_IPADY)
        
        Label_ShowConsole = tk.Label(
            Frame_ShowConsole,
            text='是否显示控制台:',
            font=('黑体', 12),
            anchor='e',
            width=15,height=1
        )
        Label_ShowConsole.pack(side=tk.LEFT)
        
        self.Combobox_ShowConsole = tkinter.ttk.Combobox(
            Frame_ShowConsole,
            width=12,height=1,
            font=('黑体', 12),
            values=['不显示','显示'],
            state='readonly'
        )
        self.Combobox_ShowConsole.bind("<<ComboboxSelected>>", self.Combobox_ShowConsole_Selected)
        self.Combobox_ShowConsole.pack(side=tk.LEFT)
        self.Combobox_ShowConsole.current(0)
        
        Frame_IconPath = tk.Frame(
            Frame_PackageParam,
            #relief='groove',bd=1
        )
        Frame_IconPath.pack(side=tk.TOP,ipady=PACKAGE_PARAM_IPADY)
        
        Label_IconPath = tk.Label(
            Frame_IconPath,
            text='图标路径:',
            font=('黑体', 12),
            anchor='e',
            width=15,height=1
        )
        Label_IconPath.pack(side=tk.LEFT)
        
        self.Entry_IconPath = tk.Entry(
            Frame_IconPath,
            textvariable=self.icon_path,
            font=('黑体', 12),
            width=ENTRY_LENGTH
        )
        self.Entry_IconPath.pack(side=tk.RIGHT)
        
        Frame_PackagedDocumentName = tk.Frame(
            Frame_PackageParam,
            #relief='groove',bd=1
        )
        Frame_PackagedDocumentName.pack(side=tk.TOP,ipady=PACKAGE_PARAM_IPADY)
        
        Label_PackagedDocumentName = tk.Label(
            Frame_PackagedDocumentName,
            text='打包后的文件名:',
            font=('黑体', 12),
            anchor='e',
            width=15,height=1
        )
        Label_PackagedDocumentName.pack(side=tk.LEFT)
        
        self.Entry_PackagedDocumentName = tk.Entry(
            Frame_PackagedDocumentName,
            textvariable=self.packaged_document_name,
            font=('黑体', 12),
            width=ENTRY_LENGTH,
        )
        self.Entry_PackagedDocumentName.pack(side=tk.RIGHT)
        
        Frame_PackageDocument = tk.Frame(
            self.root
        )
        Frame_PackageDocument.pack(side=tk.TOP)
        
        self.Button_PackageDocument = tk.Button(
            Frame_PackageDocument,
            text='打包python文件为exe',
            command=self.PackageDocument_Click,
            width=20,height=1,
        )
        self.Button_PackageDocument.pack(side=tk.TOP,pady=10)
        
        Frame_OutputLog = tk.Frame(
            self.root,
        )
        Frame_OutputLog.pack(side=tk.TOP,ipady=PACKAGE_PARAM_IPADY)
        
        Label_OutputLog = tk.Label(
            Frame_OutputLog,
            text='输出日志:',
            font=('黑体', 12),
            width=80,height=1,
            anchor='w',
        )
        Label_OutputLog.pack(side=tk.TOP)
        
        self.Text_OutputLog = tk.Text(
            Frame_OutputLog,
            font=('黑体', 12),
            width=80,height=20,
        )
        self.Text_OutputLog.pack(side=tk.TOP)
            
    
    def MonitoringPyDocumentPathChanges(self,*args):
        self.icon_path.set(self.py_document_path.get().replace('.py','.ico'))
    
    
    def PayAttentionTo_Click(self):
        tkinter.messagebox.showinfo('提示','使用前请保证已经安装了pyinstaller库')
        
        
    def PackageDocument_Click(self):
        self.Button_PackageDocument.config(state=tk.DISABLED)
        py_document_path = self.py_document_path.get() if self.py_document_path.get() !='' else None
        icon_path = self.icon_path.get() if self.icon_path.get() !='' else None
        packaged_document_name = self.packaged_document_name.get() if self.packaged_document_name.get() !='' else None

        self.auto_package_py_document_module.InitPackageParam(
            py_document_path = py_document_path,
            show_console = bool(self.Combobox_ShowConsole.current()),
            icon_path = icon_path,
            packaged_document_name = packaged_document_name,
            save_packaged_document_path = None
        )
        
        PackagePyDocumentParam = self.auto_package_py_document_module.AddPackagePyDocumentParam()
        
        # 使用 subprocess 执行命令并捕获输出
        process = subprocess.Popen(PackagePyDocumentParam, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self.Text_OutputLog.delete('1.0',tk.END)#清空文本框
        for line in iter(process.stdout.readline, b''):#将输出信息显示在文本框中
            self.Text_OutputLog.insert(tk.END, line.decode())  # 在文本框中插入输出内容
            self.Text_OutputLog.see(tk.END)  # 滚动到文本框的末尾
            self.Text_OutputLog.update()  # 更新文本框显示
        # 等待命令执行完成
        process.wait()
        self.auto_package_py_document_module.InitPackageParam(None, False, None, None, None)# 重置打包参数为空
        
        #弹出弹窗，提示打包完成了
        tkinter.messagebox.showinfo('提示','打包完成\n查看日志以了解打包是否成功')
        self.Button_PackageDocument.config(state=tk.NORMAL)
        

    def Combobox_ShowConsole_Selected(self,event):
        return
    
        
    def RunApp(self):
        '''运行程序'''
        self.root.mainloop()
        
appd = AutoPackagePyDocument()
appd.InitUI()
appd.RunApp()