# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:38:28 2019

@author: Brian
"""

import wx
import wx.html2
import time
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta

class MicrosoftCatalog(wx.Dialog):
    def _init_(self,*args,**kwds):
        wx.Dialog._init_(self,*args,**kwds)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.browser = wx.html2.WebView.New(self)
        sizer.add(self.browser, 1, wx.EXPAND, 10)
        self.Bind(wx.html2.EVT_WEBVIEW_LOADED, self.OnWebViewLoaded, self.browser)
        self.Bind(wx.EVT_CLOSE, self.onClose)
        self.SetSizer(sizer)
        self.SetSize((1600,900))
        self.Show()
        self.SleepTime = 0
        
        