# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class myapp
###########################################################################

class myapp ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Download Video Youtube", pos = wx.DefaultPosition, size = wx.Size( 500,356 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Selamat Datang Di Aplikasi Untuk Mendownload Video Youtube", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer4.Add( self.m_staticText1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Masukan Link Video Youtube : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer4.Add( self.m_staticText2, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.link = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.link, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.sss = wx.StaticText( self, wx.ID_ANY, u"Pilih resolusi : \n1. 144p\n2. 360p\n3. 720p", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sss.Wrap( -1 )
		bSizer4.Add( self.sss, 0, wx.ALL, 5 )
		
		self.res = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.res.SetMaxLength( 1 ) 
		bSizer4.Add( self.res, 0, wx.ALL, 5 )
		
		self.unduh = wx.Button( self, wx.ID_ANY, u"Unduh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.unduh, 0, wx.ALL, 5 )
		
		self.loading = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.loading.SetValue( 0 ) 
		bSizer4.Add( self.loading, 0, wx.ALL, 5 )
		
		self.info = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.info, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.unduh.Bind( wx.EVT_BUTTON, self.download )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def download( self, event ):
		event.Skip()
