# -*- coding: utf-8 -*-
import wx

class mainWindow(wx.Frame):
    def OnAbout(self,event):
        # 创建一个带"OK"按钮的对话框。wx.OK是wxWidgets提供的标准ID
        dlg = wx.MessageDialog(self, "A small text editor.", "About Sample Editor", wx.OK)    # 语法是(self, 内容, 标题, ID)
        dlg.ShowModal()    # 显示对话框
        dlg.Destroy()    # 当结束之后关闭对话框
        
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(200,200))
        self.control = wx.TextCtrl(self,style=wx.TE_MULTILINE)
        self.CreateStatusBar() #创建位于窗口的底部的状态栏

        #设置菜单
        fileMenu = wx.Menu()
        #wx.ID_ABOUT和wx.ID_EXIT是wxWidgets提供的标准ID
        menuItem = fileMenu.Append(wx.ID_ABOUT,"&About","关于程序信息")
        fileMenu.AppendSeparator()
        fileMenu.Append(wx.ID_EXIT,"退出","终止程序")
       
        #创建菜单栏
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&file")
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnAbout, menuItem)
        self.Show(True)

    

app = wx.App(False)

frm = mainWindow(None,"hello world")

app.MainLoop()